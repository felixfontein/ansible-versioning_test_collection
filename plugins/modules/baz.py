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
module: baz
short_description: Make a HEAD
version_added: '1.0.0'
description:
  - Makes a HEAD to a URL.
  - This is really only a test.
author:
  - "Felix Fontein (@felixfontein)"
requirements:
  - An internet connection
options:
  url:
    description:
      - The URL to POST to.
    required: yes
    type: str
'''

EXAMPLES = r'''
- name: Do something
  felixfontein.versioning_test_collection.baz:
    url: https://example.com
  register: result
- debug:
    msg: '{{ result.status }}'
'''

RETURN = r'''
status:
  description:
    - The status code of the HEAD request.
  returned: always
  type: int
  sample: 200
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
        method='HEAD',
    )

    module.exit_json(
        status=i["status"],
    )


if __name__ == '__main__':
    main()
