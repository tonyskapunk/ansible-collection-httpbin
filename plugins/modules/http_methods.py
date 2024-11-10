# -*- coding: utf-8 -*-
#
#    Copyright (C) 2024 Tony Garcia
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: http_methods

short_description: HTTP methods module for httpbin service.

version_added: "1.0.0"

description: A module to interact with httpbin service.

options:
    server:
        description: HTTPBin server URL.
        required: false
        type: str
        default: "https://httpbin.org"
    method:
        description: Type of method to use. GET, POST, PATCH, PUT, DELETE.
        required: false
        type: str
        default: GET
    data:
        description: Data to send in the request.
        required: false
        type: dict
    headers:
        description: Headers to send in the request.
        required: false
        type: dict
        default: {'accept: application/json'}
    ignore_certs:
        description: Ignore SSL certificates.
        required: false
        type: bool
    query:
        description: Query parameters to send in the request.
        required: false
        type: dict
    timeout:
        description: Timeout for the request in seconds.
        required: false
        type: int
        default: 15

author:
    - Tony Garcia (@tonyskapunk)
"""

EXAMPLES = r"""
# Get request (default)
- name: Get request
  tonyskapunk.httpbin.http_methods:

# Post request
- name: Post request
  tonyskapunk.httpbin.http_methods:
    method: POST
    server: httpbin.local
    data:
      key: value

# Patch request
- name: Patch request
  tonyskapunk.httpbin.http_methods:
    method: PATCH

# Put request
- name: Put request
  tonyskapunk.httpbin.http_methods:
    method: PUT
    data:
      key1: value1
    timeout: 1

# Delete request
- name: Put request
  tonyskapunk.httpbin.http_methods:
    method: DELETE
    data:
      key: value
"""

RETURN = r"""
body:
  description: The body of the response.
  type: dict
  returned: always
  sample:
    args: {}
    data: {}
    files: {}
    form:
      key1: value1
    headers:
       Accept: application/json
       Accept-Encoding": identity
       Content-Length: 11
       Content-Type: application/x-www-form-urlencoded
       Host: httpbin.org
       User-Agent: python-urllib3/1.26.19
    json": null,
    origin: 10.20.30.40
    url: https://httpbin.org/put
headers:
  description: The headers of the response.
  type: dict
  returned: always
  sample:
    accept: application/json
    host: httpbin.local
invocation:
  description: The arguments the module was invoked with.
  type: dict
  returned: always
  sample:
    module_args:
      data:
        key1: value1
      headers":
        accept: application/json
      ignore_certs: false
      method: PUT
      query: null
      server: https://httpbin.org
      timeout: 1
msg:
  description: A human-readable message indicating the result.
  type: str
  returned: always
  sample: All good...
status:
  description: The status code of the response.
  type: int
  returned: always
  sample: 200
response:
    description: The response from the httpbin service.
    type: dict
    returned: always
    sample:
      headers:
        accept: application/json
        host: httpbin.local
      body:
        key: value
      status: 200
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import missing_required_lib


try:
    from requests import Request, Session, exceptions
except ImportError:
    HAS_REQUESTS = False
    REQUESTS_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_REQUESTS = True
    REQUESTS_IMPORT_ERROR = None

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        server=dict(type="str", required=False, default="https://httpbin.org"),
        method=dict(
            type="str",
            required=False,
            default="GET",
            choices=["GET", "POST", "PATCH", "PUT", "DELETE"],
        ),
        headers=dict(
            type="dict", required=False, default={"accept": "application/json"}
        ),
        data=dict(type="dict", required=False),
        query=dict(type="dict", required=False),
        ignore_certs=dict(type="bool", required=False, default=False),
        timeout=dict(type="int", required=False, default=15),
    )

    # Fail if requests is not installed
    module.fail_json(msg=missing_required_lib('requests'), exception=REQUESTS_IMPORT_ERROR)

    result = {}

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if module.check_mode:
        module.exit_json(**result)

    # Implementation
    query = ""
    if module.params["query"]:
        query += "?"
        query += "&".join([f"{k}={v}" for k, v in module.params["query"].items()])

    if module.params["data"]:
        request = Request(
            module.params["method"],
            module.params["server"] + "/" + module.params["method"].lower() + query,
            data=module.params["data"],
            headers=module.params["headers"],
        )
    else:
        request = Request(
            module.params["method"],
            module.params["server"] + "/" + module.params["method"].lower() + query,
            headers=module.params["headers"],
        )

    s = Session()
    r = request
    response = s.send(
        r.prepare(),
        verify=not module.params["ignore_certs"],
        timeout=module.params["timeout"],
    )

    result["status"] = response.status_code
    result["headers"] = dict(response.headers)

    try:
        result["body"] = response.json()
    except exceptions.JSONDecodeError:
        result["body"] = {"content": response.text}

    if response.status_code == 200:
        result["changed"] = False
    else:
        module.fail_json(msg="Error in the request", **result)

    module.exit_json(msg="All good...", **result)

    # Debugging
    # raise Exception(result)


def main():
    run_module()


if __name__ == "__main__":
    main()
