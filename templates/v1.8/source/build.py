#!/usr/bin/env python3
"""Build FSL v1.8 DOCX from the English method and approved native Word layout.
The layout data is build-only, not an authoring or iteration schema.
"""
import argparse, io, json, re, zipfile
from pathlib import Path
from docx import Document
from lxml import etree as E
TERMS=('CONFORMANT WITH EXCEPTION','NOT YET PROVEN','NON-CONFORMANT','SHOULD NOT','SHALL NOT','MUST NOT','CONFORMANT','EXCEPTION','WAIVER','SHOULD','SHALL','MUST','MAY')
NORM=re.compile(r'(?<![A-Za-z0-9_-])('+'|'.join(map(re.escape,TERMS))+r')(?![A-Za-z0-9_-])')
AXIOM='FSL owns the method. The project owns the work.'
def blocks(md):
    return [s for s in md.split('\n\n') if s and not s.startswith('# ') and not s.startswith('Project:') and s.strip()!='**'+AXIOM+'**']
def segments(md):
    out=[]
    for b in blocks(md):
        if b.startswith('## '): out.append(b[3:]); continue
        if b.startswith('### '): out.append(b[4:]); continue
        for part in re.split(r'(\*\*.*?\*\*)',b,flags=re.S):
            if not part: continue
            if part.startswith('**'): part=part[2:-2]
            out.extend(s for s in NORM.split(part) if s)
    return out
def build(method,output):
    model=json.loads(Path(__file__).with_name('layouts.json').read_text())
    model['nodes']=[n for part in model['node_parts'] for n in json.loads(Path(__file__).with_name(part).read_text())['nodes']]
    words=segments(method.read_text())
    if len(words)!=model['method_segments']: raise ValueError('Source no longer matches this frozen layout; review instead of dropping content.')
    ns=model['namespaces']
    def q(name):
        if ':' not in name: return name
        prefix,local=name.split(':',1)
        return '{'+ns[prefix]+'}'+local
    def node(i):
        tag,attrs,text,children=model['nodes'][i]
        mapping=dict(ns)
        if tag.split(':')[0] in ('ct','rel'): mapping[None]=mapping.pop(tag.split(':')[0])
        el=E.Element(q(tag),nsmap=mapping)
        for k,v in attrs.items(): el.set(q(k),v)
        el.text=words[text] if isinstance(text,int) else text
        el.extend(node(c) for c in children)
        return el
    def xml(el): return E.tostring(el,encoding='UTF-8',xml_declaration=True,standalone=True)
    buf=io.BytesIO(); Document().save(buf)
    with zipfile.ZipFile(buf) as z: base={n:z.read(n) for n in z.namelist()}
    output.mkdir(parents=True,exist_ok=True)
    for label,record in model['documents'].items():
        parts=dict(base)
        for name,i in record['parts'].items(): parts[name]=xml(node(i))
        styles=E.fromstring(parts['word/styles.xml'])
        for i in record['styles']:
            style=node(i); key=q('w:styleId')
            for prior in list(styles):
                if prior.get(key)==style.get(key): styles.replace(prior,style); break
            else: styles.append(style)
        parts['word/styles.xml']=xml(styles)
        target=output/('FSL-v1.8-'+label+'.docx')
        with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for name in sorted(parts):
                info=zipfile.ZipInfo(name,(2026,9,9,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16
                z.writestr(info,parts[name])
        print(target.name)
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--method',type=Path,required=True); p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); build(a.method,a.output)
