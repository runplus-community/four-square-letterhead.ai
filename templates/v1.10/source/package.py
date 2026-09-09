#!/usr/bin/env python3
"""Create a checked FSL ZIP locally; no remote writes or execution."""
import argparse, hashlib, shutil, sys, zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from verify import verify_documents, verify_policy, verify_checksums

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
a=p.parse_args();root=a.root.resolve()
verify_policy(root);verify_documents(root)
files=sorted(x.relative_to(root).as_posix() for x in root.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.name not in ('MANIFEST.txt','SHA256SUMS.txt'))
(root/'MANIFEST.txt').write_text('\n'.join(files)+'\n')
(root/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in files+['MANIFEST.txt']))
print('PASS',verify_checksums(root),'checksum entries')
archive=root.with_suffix('.zip')
# with_suffix would treat .10 as a suffix, so preserve the full directory name.
archive=root.parent/(root.name+'.zip')
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name in files+['MANIFEST.txt','SHA256SUMS.txt']:
  z.write(root/name,root.name+'/'+name)
with TemporaryDirectory(prefix='fsl-release-verify-') as tmp:
 with zipfile.ZipFile(archive) as z:z.extractall(tmp)
 clean=Path(tmp)/root.name
 verify_policy(clean);verify_documents(clean);verify_checksums(clean)
 victim=clean/'VERSION';victim.write_text('damaged\n')
 try:verify_checksums(clean)
 except ValueError:print('PASS altered payload rejected')
 else:raise RuntimeError('Altered payload accepted')
print('PASS clean extraction verified')
digest=hashlib.sha256(archive.read_bytes()).hexdigest()
archive.with_name(archive.name+'.sha256').write_text(digest+'  '+archive.name+'\n')
print(digest,archive.name)
