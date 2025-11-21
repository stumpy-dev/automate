#!/usr/bin/env python

import json
import sys
from urllib import request    

def versions(pkg_name):
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    releases = json.loads(request.urlopen(url).read())['releases']
    return releases

if __name__ == '__main__':
    print(*versions(sys.argv[1]), sep='\n')
