mkdir medial && mkdir static

Touch 'settings_local.py' in root folder.

requirements:
 - memcached
 - postgresql
 - python 2.7
 - pip

pip install -r requirements.txt

## Build static
npm i

gulp style - build static style

gulp watch
