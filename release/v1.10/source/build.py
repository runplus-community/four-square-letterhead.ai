#!/usr/bin/env python3
"""Build five FSL v1.10 reading documents from their authoritative Markdown.

No network, repository write, agent dispatch or CI trigger is performed.
PDF rendering is a separate local step described in source/README.md.
"""
from __future__ import annotations
import argparse
import re
from datetime import datetime, timezone
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT

AXIOM = 'FSL owns the method. The project owns the work.'
VERSION_LINE = 'Four-Square Template v1.10'
FONT = 'Arial'
INK, NAVY, MUTED, LINE, PALE = '172B3A', '000000', '526474', 'CCD7DF', 'F2F5F7'
WIDTH = 507.28
TERMS = ('CONFORMANT WITH EXCEPTION', 'NOT YET PROVEN', 'NON-CONFORMANT',
         'MUST NOT', 'SHOULD NOT', 'SHALL NOT', 'MUST', 'SHOULD', 'SHALL',
         'MAY', 'CONFORMANT', 'EXCEPTION', 'WAIVER')
NORM = re.compile(r'(?<![A-Za-z0-9_-])(' + '|'.join(map(re.escape, TERMS)) + r')(?![A-Za-z0-9_-])')
SPECS = (
 ('FSL-v1.10-METHOD.md', 'FSL-v1.10-METHOD-3P',
  'Method project v1.10', 3, False),
 ('FSL-v1.10-PROJECT-DNA-TEMPLATE.md', 'FSL-v1.10-PROJECT-DNA-TEMPLATE-1P',
  'Project / contract [vN] · Template', 1, True),
 ('FSL-v1.10-EXAMPLE-EVIDENCE-BRIEF.md', 'FSL-v1.10-EXAMPLE-EVIDENCE-BRIEF-2P',
  'Evidence Brief v0.1 · Illustration', 2, True),
 ('FSL-v1.10-APPENDIX-DNA-LINEAGE.md', 'FSL-v1.10-APPENDIX-DNA-LINEAGE-2P',
  'FSL appendix v1.10 · Explanation', 2, False),
 ('FSL-v1.10-SKILL.md', 'FSL-v1.10-SKILL-1P',
  'Maintenance skill v1.10', 1, False),
)

def plain(text: str) -> str:
    return text.replace('**', '').replace('`', '')

def blocks(path: Path) -> list[tuple[str, str]]:
    result = []
    for block in path.read_text(encoding='utf-8').strip().split('\n\n'):
        text = ' '.join(block.splitlines()).strip()
        if text.startswith('### '): result.append(('h3', text[4:]))
        elif text.startswith('## '): result.append(('h2', text[3:]))
        elif text.startswith('# '): result.append(('title', text[2:]))
        else: result.append(('p', text))
    return result

def font(run, size: float, bold: bool = False, underline: bool = False, color: str = INK):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.bold, run.underline = bold, underline
    run.font.color.rgb = RGBColor.from_string(color)
    rf = run._element.get_or_add_rPr().get_or_add_rFonts()
    for key in ('ascii', 'hAnsi', 'eastAsia'): rf.set(qn('w:' + key), FONT)

def rich(p, text: str, size: float, bold: bool = False, color: str = INK):
    for token in re.split(r'(\*\*.*?\*\*)', text):
        strong = token.startswith('**') and token.endswith('**')
        value = token[2:-2] if strong else token
        value = value.replace('`', '')
        for chunk in NORM.split(value):
            if chunk:
                is_norm = chunk in TERMS
                font(p.add_run(chunk), size, bold or strong or is_norm, is_norm, color)

def para(d, text: str, size: float = 10.1, after: float = 4, before: float = 0,
         bold: bool = False, color: str = INK, style: str | None = None):
    p = d.add_paragraph(style=style)
    f = p.paragraph_format
    f.space_before, f.space_after = Pt(before), Pt(after)
    f.line_spacing = 1.08
    f.keep_together = True
    rich(p, text, size, bold, color)
    return p

def field(p, instr: str):
    el = OxmlElement('w:fldSimple'); el.set(qn('w:instr'), instr)
    r = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = '1'
    r.append(t); el.append(r); p._p.append(el)

def document(identity: str):
    d = Document(); s = d.sections[0]
    s.page_width, s.page_height = Pt(595.28), Pt(841.89)
    s.left_margin = s.right_margin = Pt(44)
    s.top_margin, s.bottom_margin = Pt(51), Pt(56)
    s.header_distance, s.footer_distance = Pt(23), Pt(21)
    for name in ('Normal','Title','Heading 1','Heading 2','Heading 3'):
        st = d.styles[name]; st.font.name = FONT; st.font.color.rgb = RGBColor.from_string(INK)
        st.paragraph_format.space_after = Pt(4)
    for st in d.styles:
        for border in list(st.element.iter(qn('w:pBdr'))):
            border.getparent().remove(border)
    d.styles['Normal'].font.size = Pt(10.1)
    for name in ('Heading 1','Heading 2','Heading 3'):
        d.styles[name].paragraph_format.keep_with_next = True
    cp=d.core_properties
    cp.title='FSL v1.10'; cp.author='FSL'; cp.last_modified_by='FSL'
    cp.subject='Documents govern; skills maintain; evidence verifies. Released method; project adoption remains separate.'
    cp.created=cp.modified=datetime(2026,9,9,0,0,0,tzinfo=timezone.utc)
    p=s.header.paragraphs[0]
    p.paragraph_format.tab_stops.add_tab_stop(Pt(WIDTH), WD_TAB_ALIGNMENT.RIGHT)
    p.paragraph_format.space_after=Pt(3)
    font(p.add_run('FSL / AUTHORITY & LINEAGE'),8,True,color=NAVY)
    font(p.add_run('\t'+identity),8,color=MUTED)
    pp=p._p.get_or_add_pPr(); bd=OxmlElement('w:pBdr'); b=OxmlElement('w:bottom')
    for key,val in [('val','single'),('sz','7'),('color',NAVY),('space','7')]: b.set(qn('w:'+key),val)
    bd.append(b);pp.append(bd)
    p=s.footer.paragraphs[0];p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after=Pt(4)
    font(p.add_run(AXIOM),8.5,True,color=NAVY)
    p=para(s.footer,'',8,0)
    p.paragraph_format.tab_stops.add_tab_stop(Pt(WIDTH),WD_TAB_ALIGNMENT.RIGHT)
    font(p.add_run(VERSION_LINE),8,color=MUTED)
    font(p.add_run('\t'),8)
    field(p,'PAGE'); font(p.add_run(' / '),8,color=MUTED); field(p,'NUMPAGES')
    settings=d.settings.element
    el=OxmlElement('w:updateFields');el.set(qn('w:val'),'true');settings.append(el)
    return d

def squares(d, paragraphs: list[str]):
    if len(paragraphs)!=4: raise ValueError('Exactly four source square descriptions required')
    t=d.add_table(rows=2, cols=2);t.alignment=WD_TABLE_ALIGNMENT.CENTER;t.autofit=False
    t._tbl.tblPr.find(qn('w:tblW')).set(qn('w:w'),str(round(WIDTH*20)))
    t._tbl.tblPr.find(qn('w:tblW')).set(qn('w:type'),'dxa')
    for c in t.columns:c.width=Pt(WIDTH/2)
    borders=OxmlElement('w:tblBorders')
    for side in ('top','bottom','left','right','insideH','insideV'):
        b=OxmlElement('w:'+side)
        for key,val in [('val','single'),('sz','4'),('color',LINE)]:b.set(qn('w:'+key),val)
        borders.append(b)
    t._tbl.tblPr.append(borders)
    for i,text in enumerate(paragraphs):
        row=t.rows[i//2];row._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
        cell=row.cells[i%2];cell.width=Pt(WIDTH/2)
        cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.TOP
        tcpr=cell._tc.get_or_add_tcPr();mar=OxmlElement('w:tcMar')
        for side,value in [('top','95'),('bottom','95'),('start','115'),('end','115')]:
            el=OxmlElement('w:'+side);el.set(qn('w:w'),value);el.set(qn('w:type'),'dxa');mar.append(el)
        tcpr.append(mar)
        if i in (0,3):
            el=OxmlElement('w:shd');el.set(qn('w:fill'),PALE);tcpr.append(el)
        p=cell.paragraphs[0];p.paragraph_format.space_after=Pt(0);p.paragraph_format.line_spacing=1.07
        rich(p,text,9.7)
    return t

def build(root: Path):
    for source, stem, identity, pages, grid in SPECS:
        path=root/source
        if not path.is_file():raise FileNotFoundError(path)
        d=document(identity);parts=blocks(path);i=0
        while i<len(parts):
            kind,text=parts[i]
            if plain(text)==AXIOM:
                i+=1;continue # once in the running footer, not repeated in the body
            if kind=='title':
                para(d,text,21,8,bold=True,color=NAVY,style='Title')
            elif kind=='h2':
                p=para(d,text,13.3,6,8,bold=True,color=NAVY,style='Heading 1')
                if re.match(r'[2-9]\. ',text):p.paragraph_format.page_break_before=True
            elif kind=='h3' and text=='Four squares' and grid:
                if [k for k,_ in parts[i+1:i+5]]!=['p']*4:raise ValueError('Four-square source layout changed')
                squares(d,[text for _,text in parts[i+1:i+5]])
                i+=4
            elif kind=='h3':
                para(d,text,10.6,3,6,bold=True,color=NAVY,style='Heading 2')
            else:
                small=text.startswith(('Project:', 'Project/contract:', 'This Markdown'))
                para(d,text,8.6 if small else 10.1,5 if grid else 4,color=MUTED if small else INK)
            i+=1
        # Tighten spacing for the complete method, not the body font size.
        # The letterhead and other reading documents keep their own natural layout.
        if 'METHOD-3P' in stem:
            d.sections[0].top_margin = Pt(42)
            d.sections[0].bottom_margin = Pt(45)
            for p in d.paragraphs:
                pf = p.paragraph_format
                pf.line_spacing = 1.02
                if pf.space_after is not None and pf.space_after.pt > 3:
                    pf.space_after = Pt(2.5)
                if pf.space_before is not None and pf.space_before.pt > 4:
                    pf.space_before = Pt(4)
        dest=root/(stem+'.docx');d.save(dest);print(dest.name)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args();build(args.root.resolve())
