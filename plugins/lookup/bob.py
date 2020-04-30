from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
lookup: bob
author: Felix Fontein
version_added: '2.1.0'
short_description: Bob was there, too
description:
  - Adds Bob.
options:
  _terms:
    description: Strings to play with.
    type: list
    elements: str
    required: True
'''

EXAMPLES = """
- debug: msg="{{ lookup('felixfontein.versioning_test_collection.bob', 'this', 'is', 'a', 'test') }}"
"""

RETURN = """
  _raw:
    description:
      - List with Bob.
    type: list
    elements: str
"""

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):
        if not isinstance(terms, list):
            raise AnsibleError("reverse expects a list")

        return terms + ['Bob']
