# -*- coding: utf-8 -*-

from json import loads
from typing import Union

from requests import Response
from robot.libraries.BuiltIn import BuiltIn

"""
Library for checking HTTP response status code, based on [ http://docs.python-requests.org/en/latest| requests ] library.
"""


def check_response_status(response: Response, code: Union[int, str] = 200) -> None:
    """Check status code in HTTP response.

    *Args:*
        _response_: object [ http://docs.python-requests.org/en/latest/api/#requests.Response | "Response" ]
        _code_: expected response status code.

    *Example:*
        | *Test cases* | *Action*                              | *Argument*            | *Argument*                | *Argument* |
        | Simple Test  | RequestsLibrary.Create session        | Alias                 | http://www.example.com    |            |
        |              | ${response}=                          | RequestsLibrary.Get request       | Alias         | /          |
        |              | RequestsChecker.Check Response Status | ${response}           | 204                       |            |
    """
    if response.status_code != int(code):
        msg_template = (f'URL: {response.url}\nResponse status code is not equal '
                        f'{code}: {code} != {response.status_code}({response.reason})')
        # attempt to parse response to JSON for better readability
        try:
            err_info_json = loads(response.text)
            err_info = '\n'.join(f'{k}:\t"{v}"' for k, v in sorted(err_info_json.items()) if v)
            msg_template += f'\n{err_info}'
        except ValueError:
            pass
        BuiltIn().fail(msg_template)
