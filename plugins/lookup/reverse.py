from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
lookup: reverse
author: Felix Fontein
version_added: '2.0.0'
short_description: reverse magic
description:
  - Given a list of strings, will do some reverse magic.
options:
  _terms:
    description: Strings to play with.
    type: list
    elements: str
    required: True
'''

EXAMPLES = """
- debug: msg="{{ lookup('felixfontein.versioning_test_collection.reverse', 'this', 'is', 'a', 'test') }}"
"""

RETURN = """
  _raw:
    description:
      - Reverse-magic'ed list.
    type: list
    elements: str
"""

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):
        if not isinstance(terms, list):
            raise AnsibleError("with_flattened expects a list")

        return [str(f)[::-1] for f in reversed(terms)]
