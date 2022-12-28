#!/usr/bin/env python

import os
import sys
import requests
import json

def main(obj, expires=None):
    url = 'https://file.io'
    if expires:
        url = '%s?expires=%s' % (url, expires)
        print (url)
        print (url)
    if os.path.exists(obj):
        with open(obj, 'rb') as f:
            res = requests.post(url, files={'file': f})
    else:
        res = requests.post(
            url,
            files={'file': ('file', obj)}
        )

    try:
        res.raise_for_status()
    except:
        link = sys.stderr.write(res.text)
        link1 = json.loads(link)
        print (link1["link"])
        raise
    else:
        da = res.text
        daa = json.loads(da)
        return daa["link"]


if __name__ == '__main__':
    sys.stdout.write(main(*sys.argv[1:]))
