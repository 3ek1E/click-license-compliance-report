import json, hashlib, re, subprocess, zipfile
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent.parent
ev=ROOT/'evidence'
d=json.loads((ev/'scancode-results.json').read_text(encoding='utf8'))
tracked=subprocess.check_output(['git','-C',str(ev/'click-8.1.7'),'ls-files'],text=True).splitlines()
scanned={x['path'].removeprefix('click-8.1.7/') for x in d['files'] if x['type']=='file'}
images=[]
for name in ['example01.jpg','example02.jpg']:
 path=ev/'click-8.1.7/examples/imagepipe'/name
 with Image.open(path) as im: icc=im.info.get('icc_profile',b'')
 raw=path.read_bytes();needle=b'Copyright (c) 1998 Hewlett-Packard Company'
 images.append({'path':str(path.relative_to(ev)).replace('\\','/'),'icc_profile_length':len(icc),'copyright_found_in_icc_profile':needle in icc,'copyright_byte_offset_in_jpeg':raw.find(needle),'interpretation':'ICC profile copyright is not proof of photographic authorship. Image and profile licensing need separate review.'})
verfile=ev/'click-8.1.7/src/click/__init__.py'
review={'commit':subprocess.check_output(['git','-C',str(ev/'click-8.1.7'),'rev-parse','HEAD'],text=True).strip(),'source_version_line':next(x for x in verfile.read_text(encoding='utf8').splitlines() if x.startswith('__version__')),'tracked_file_count':len(tracked),'scanned_file_count':len(scanned),'not_in_scan':sorted(set(tracked)-scanned),'images':images,'scanner_package_version':d['packages'][0]['version'],'python_upstream_reference':'https://github.com/python/cpython/blob/v2.7.18/Lib/optparse.py#L40-L67','upstream_reference_caveat':'Reference for license comparison only; exact copied upstream version has not been established.'}
(ev/'manual-review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2),encoding='utf8')
paths=[p for p in ev.rglob('*') if p.is_file() and '.git' not in p.relative_to(ev).parts and p.name!='manifest-sha256.json']
manifest={p.relative_to(ev).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
(ev/'manifest-sha256.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
dest=ROOT/'Click扫描原始报告及复现材料.zip'
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
 for p in paths+[ev/'manifest-sha256.json']:z.write(p,'evidence/'+p.relative_to(ev).as_posix())
print(json.dumps(review,ensure_ascii=False,indent=2));print('ZIP',dest,dest.stat().st_size)
