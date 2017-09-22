"""
simple web server to send response
"""

import sys

version = sys.version_info[0]

def app(environ, start_response):
    """Simplest possible application object"""
    print('{0} {1}'.format(environ['PATH_INFO'], environ['QUERY_STRING']))
    string_arr = environ['QUERY_STRING'].split("&")
    result = "\n".join(string_arr)

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
