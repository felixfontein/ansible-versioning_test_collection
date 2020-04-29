#!/usr/bin/python
#
# Copyright 2020 Felix Fontein
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = r'''
---
module: foo
short_description: Makes a POST
description:
  - Makes a POST to a URL.
  - This is really only a test.
author:
  - "Felix Fontein (@felixfontein)"
requirements:
  - An internet connection
options:
  url:
    description:
      - The URL to POST to
    required: yes
    type: str
'''

EXAMPLES = r'''
- name: Do something
  felixfontein.versioning_test_collection.foo:
    url: https://example.com
  register: result
- debug:
    msg: |
      {{ result.status }} --
      {{ result.body }}
'''

RETURN = r'''
status:
  description:
    - The status code of the POST request
  returned: always
  type: int
  sample: 200
body:
  description:
    - The parsed JSON result
  returned: always
  type: dict
  sample: '{"key": "value"}'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url


def main():
    argument_spec = dict(
        url=dict(type='str', required=True),
    )
    module = AnsibleModule(argument_spec)

    r, i = fetch_url(
        module,
        module.params['url'],
        method='POST',
        data='x=42'
    )

    status = i["status"]
    try:
        body = r.read()
    except Exception as dummy:
        body = i.get('body')

    module.exit_json(
        status=status,
        body=module.from_json(body)
    )


if __name__ == '__main__':
    main()
