#!/usr/bin/env python3
"""Verify FSL v1.7 documents or an unpacked release. Requires Poppler CLI tools.
This checks framework artifacts, not the correctness of a consuming project.
"""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

V='1.7'
AXIOM='FSL owns the method. The project owns the work.'
DOCS={f'FSL-v{V}-Template-1P':1,f'FSL-v{V}-Template-2P':2,
      f'FSL-v{V}-Template-3P':3,f'FSL-v{V}-Sample-Django-2P':2}
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
W='{'+NS['w']+'}'
NORM=re.compile(r'(?<![A-Za-z0-9_-])(CONFORMANT WITH EXCEPTION|NOT YET PROVEN|NON-CONFORMANT|MUST NOT|SHOULD NOT|SHALL NOT|MUST|SHOULD|SHALL|MAY|CONFORMANT|EXCEPTION|WAIVER)(?![A-Za-z0-9_-])')


def require(ok, message):
    if not ok: raise ValueError(message)


def command(*args):
    try:
        return subprocess.run(args,check=True,capture_output=True,text=True,timeout=60).stdout
    except FileNotFoundError as exc:
        raise RuntimeError(f'Required command not found: {args[0]} (install Poppler)') from exc


def texts(node):
    return ''.join(t.text or '' for t in node.iter(W+'t'))


def check_docx(path, sample):
    with zipfile.ZipFile(path) as z:
        require(z.testzip() is None,f'Broken DOCX: {path.name}')
        body=ET.fromstring(z.read('word/document.xml'))
        alltext=texts(body)
        require('R-01' in alltext and 'NOT RUN' in alltext,'Missing visible route/run states')
        require('iterations optional' in alltext.lower(),'Missing existing-project iteration guidance')
        first=body.find('.//w:body/w:tbl/w:tr/w:tc',NS)
        require(first is not None,'No Four-Square panel')
        paragraphs=first.findall('w:p',NS)
        require(len(paragraphs)>1 and texts(paragraphs[1]).startswith('FSL /'),'FSL must be the first SPEC item')
        require(all(k in alltext for k in ('Appendix','Errata','Amendments')),'Optional SPEC lifecycle absent')
        if not sample:
            require(all(k in alltext for k in ('system-vN','ai-vN','SPEC','SYSTEM','AI','MEMORY')),'Missing concrete default lanes')
        else:
            require('CODE / DOCS' in alltext,'Sample specialization not identified')
            require('No historical or future iteration plan is required' in alltext,'Sample wrongly requires iterations')
            require('NOT EXECUTED' in alltext,'Sample must not fabricate execution')
        count=0
        for name in z.namelist():
            if not (name=='word/document.xml' or re.fullmatch(r'word/(header|footer)\d+\.xml',name)): continue
            tree=ET.fromstring(z.read(name))
            for r in tree.iter(W+'r'):
                value=texts(r)
                if NORM.search(value):
                    props=r.find('w:rPr',NS)
                    b=props.find('w:b',NS) if props is not None else None
                    u=props.find('w:u',NS) if props is not None else None
                    require(b is not None and b.get(W+'val','true') not in ('0','false'),f'Normative term not bold: {value}')
                    require(u is not None and u.get(W+'val','single') not in ('none','0','false'),f'Normative term not underlined: {value}')
                    count+=1
        require(count>=10,'Too few normative terms validated')
    return count


def check_documents(root):
    require({p.stem for p in root.glob('FSL-v1.7-*.docx')}==set(DOCS),'Unexpected/missing DOCX set')
    require({p.stem for p in root.glob('FSL-v1.7-*.pdf')}==set(DOCS),'Unexpected/missing PDF set')
    for name,pages in DOCS.items():
        sample='Django' in name
        count=check_docx(root/(name+'.docx'),sample)
        pdf=root/(name+'.pdf')
        info=command('pdfinfo',str(pdf)); found=re.search(r'^Pages:\s+(\d+)',info,re.M)
        require(found and int(found.group(1))==pages,f'Wrong page count: {name}')
        sections=command('pdftotext','-layout',str(pdf),'-').split('\f')
        require(len([x for x in sections if x.strip()])==pages,f'PDF text page mismatch: {name}')
        for n,text in enumerate(sections[:pages],1):
            flat=' '.join(text.split())
            require(AXIOM in flat,f'Footer absent on {name} page {n}')
            require('Four-Square Template v1.7' in flat,f'Template version absent on {name} page {n}')
            require(('Sample edition v1.7' if sample else 'Project / contract version [vN]') in flat,f'Project identity absent on {name} page {n}')
            require('v1.6' not in text and 'v1.5' not in text,f'Stale identity in {name}')
            require('\ufffd' not in text,f'Broken text in {name}')
        print(f'PASS {name}: {pages} pages; per-page identities/footer; {count} emphasized normative runs')


def check_hashes(root):
    manifest=root/'MANIFEST.txt'; hashes=root/'SHA256SUMS.txt'
    require(manifest.is_file() and hashes.is_file(),'Manifest/checksums missing')
    expected=manifest.read_text().splitlines()
    require(expected==sorted(set(expected)),'Manifest must be sorted and unique')
    allowed=set(expected)|{'MANIFEST.txt','SHA256SUMS.txt'}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    require(actual==allowed,f'Payload differs from manifest: {sorted(actual^allowed)}')
    listed={}
    for line in hashes.read_text().splitlines():
        digest,rel=line.split('  ',1)
        require(re.fullmatch('[0-9a-f]{64}',digest),'Invalid SHA-256')
        p=Path(rel)
        require(not p.is_absolute() and '..' not in p.parts,'Unsafe checksum path')
        require(rel not in listed,'Duplicate checksum')
        require(hashlib.sha256((root/p).read_bytes()).hexdigest()==digest,f'Checksum mismatch: {rel}')
        listed[rel]=digest
    require(set(listed)==set(expected)|{'MANIFEST.txt'},'Checksum coverage differs from manifest')
    require(not any(Path(x).suffix.lower() in ('.zip','.yaml','.yml') for x in expected),'Nested ZIP or YAML in payload')
    require(not any(p.is_symlink() for p in root.rglob('*')),'Symlinks not accepted in release payload')
    print(f'PASS checksum coverage: {len(listed)} files')


def check_method(root):
    c=(root/'FSL-v1.7-CONSTITUTION.md').read_text()
    required=('POLICY-SQUARE-003','LAW-SPEC-001','LAW-OWN-001','LAW-REPO-001','LAW-ADOPT-001','LAW-ADOPT-002','LAW-ROUTE-002','LAW-RUN-001','LAW-LIFE-006','LAW-DEV-005','LAW-DEV-006','LAW-DEV-001 through LAW-DEV-004 are retired')
    require(all(x in c for x in required),'Constitution has missing required clauses')
    ids=re.findall(r'^\*\*([A-Z]+-[A-Z]+-\d{3})',c,re.M)
    require(len(ids)==len(set(ids)),'Duplicate constitutional clause IDs')
    for token in ('OBSERVED / AS-IS','ADOPTED / INTENDED','before execution','same workflow','Future iterations are optional','No route database'):
        require(token in c,f'Method anchor absent: {token}')
    for name in ('ROUTES','ADOPTION','LIFECYCLE','SKILL','CHECKLIST','MEMORY','CHANGELOG'):
        p=root/f'FSL-v1.7-{name}.md';require(p.is_file() and len(p.read_text())>100,f'Missing {name}')
    print(f'PASS method structure: {len(ids)} unique clauses; route, adoption and lifecycle anchors')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--documents',type=Path,help='check the four DOCX/PDF pairs only')
    p.add_argument('--root',type=Path,help='check an unpacked release payload')
    args=p.parse_args()
    require(bool(args.documents)^bool(args.root),'Supply exactly one of --documents or --root')
    root=(args.documents or args.root).resolve()
    if args.root:
        check_hashes(root);check_method(root)
    check_documents(root)
    print('PASS FSL v1.7 artifact verification; downstream projects remain outside this claim')

if __name__=='__main__':
    try: main()
    except (ValueError,RuntimeError,subprocess.SubprocessError,ET.ParseError,OSError,zipfile.BadZipFile) as exc:
        print(f'FAIL: {exc}',file=sys.stderr);sys.exit(1)
