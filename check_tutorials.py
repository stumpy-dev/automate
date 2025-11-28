#!/usr/bin/env python

import re
from urllib import request

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/91.0.4472.124 Safari/537.36"
}

base_url = 'https://stumpy.readthedocs.io/en/latest'

def url_to_html(url):
    req = request.Request(
        url,
        data=None,
        headers=HEADERS
    )

    html = request.urlopen(req).read().decode("utf-8")

    return html


def get_tutorial_urls():
    url = f'{base_url}/tutorials.html'

    html = url_to_html(url)
    ul_match = re.search(r'<ul>(.*?)</ul>', html, re.DOTALL)
    tutorial_urls = []
    if ul_match:
        for tutorial in re.findall(r'href="(.*)"', ul_match.group(1)):
            tutorial_urls.append(f'{base_url}/{tutorial}')

    return tutorial_urls


def pattern_found(pattern, html):
    match = re.search(pattern, html, re.DOTALL)
    if match:
        return True
    else:
        return False

if __name__ == '__main__':
    tutorial_urls = get_tutorial_urls()
    found = False
    for url in tutorial_urls:
        html = url_to_html(url)
        # Add additional errors, warnings to this list
        patterns = [r'HTTPError', r'FutureWarning:']
        for pattern in patterns:
            if pattern_found(pattern, html):
                found = True
                print(f'"{pattern}" found in "{url}"')

    if found:
        msg = "One or more warnings/errors were found.\n"
        msg += "Please consider rebuilding the docs on readthedocs.org.\n"
        raise ValueError("One or more warnings/errors were found")
