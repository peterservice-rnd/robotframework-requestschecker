# -*- coding: utf-8 -*-

from json import loads

from robot.libraries.BuiltIn import BuiltIn
from robot.utils import PY2

"""
Library for checking HTTP response status code, based on [ http://docs.python-requests.org/en/latest| requests ] library.
"""


def check_response_status(response, code=200):
    """Check status code in HTTP response.

    *Args:*\n
        _response_: object [ http://docs.python-requests.org/en/latest/api/#requests.Response | "Response" ]\n
        _code_: expected response status code.\n

    *Example:*\n
        | *Test cases* | *Action*                              | *Argument*            | *Argument*                | *Argument* |
        | Simple Test  | RequestsLibrary.Create session        | Alias                 | http://www.example.com    |            |
        |              | ${response}=                          | RequestsLibrary.Get request       | Alias         | /          |
        |              | RequestsChecker.Check Response Status | ${response}           | 204                       |            |
    """
    if response.status_code != int(code):
        msg_template = ('URL: {url}\nResponse status code is not equal '
                        '{code}: {code} != {resp_code}({reason})'.format(url=response.url, code=code,
                                                                         resp_code=response.status_code,
                                                                         reason=response.reason))
        # attempt to parse response to JSON for better readability
        try:
            err_info_json = loads(response.text)
            err_info = u'\n'.join(u'{0}:\t"{1}"'.format(k, v) for k, v in sorted(err_info_json.items()) if v)
            msg_template += '\n' + err_info
        except ValueError:
            pass
        if PY2:
            msg_template = msg_template.encode('utf-8')
        BuiltIn().fail(msg_template)
