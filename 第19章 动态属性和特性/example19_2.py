from urllib.request import urlopen
import warnings
import os
import json


URL = 'https://www.oreilly.com/pub/sc/osconfeed'
JSON = 'osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)  # <1>
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON, 'rb') as fp:
        return json.load(fp)


feed = load()
print(sorted(feed['Schedule'].keys()))
for key, value in sorted(feed['Schedule'].items()):
    print('{:3} {}'.format(len(value), key))
