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
module: echo
short_description: Echo params
version_added: '1.0.0'
description:
  - Echo module params.
author:
  - "Felix Fontein (@felixfontein)"
options:
  params:
    description:
      - Some params.
    required: yes
    type: dict
'''

EXAMPLES = r'''
- name: Do something
  felixfontein.versioning_test_collection.echo:
    params:
      foo: bar
      weee: true
      nothing: null
  register: result
- debug:
    msg: 'Echo! {{ result.status }}'
'''

RETURN = r'''
params:
  description:
    - What was passed.
  returned: always
  type: dict
  sample: {}
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url


def main():
    argument_spec = dict(params=dict(type='dict', required=True))
    module = AnsibleModule(argument_spec)
    module.exit_json(params=module.params["params"])


if __name__ == '__main__':
    main()
