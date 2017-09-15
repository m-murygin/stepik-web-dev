"""
simple web server to send response
"""

import sys

version = sys.version_info[0]

if version == 2:
    from urlparse import parse_qsl
else:
    from urllib.parse import parse_qsl

def app(environ, start_response):
    """Simplest possible application object"""
    print environ['PATH_INFO'] + environ['QUERY_STRING']
    string_arr = parse_qsl(environ['QUERY_STRING'])
    result = ''
    for var_tuple in string_arr:
        result = result + var_tuple[0] + '=' + var_tuple[1] + '\n'

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(result)))
    ]
    start_response(status, response_headers)
    if version == 2:
        return [result]
    else:
        return [bytes(result, 'utf-8')]
