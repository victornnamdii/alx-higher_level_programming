#!/usr/bin/python3
"""A script that
- fetches https://intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request as request
    with request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
