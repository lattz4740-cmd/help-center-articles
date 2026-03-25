#!/usr/bin/env python3
"""Print the translation keys extracted from English source files."""

import sys
sys.path.insert(0, 'scripts')
from verify_translations import _get_required_keys

print('code.json keys:')
for k in sorted(_get_required_keys('code.json')):
    print(f'  {k}')

print()
print('current.json keys:')
for k in sorted(_get_required_keys('current.json')):
    print(f'  {k}')

print()
print('navbar.json keys:')
for k in sorted(_get_required_keys('navbar.json')):
    print(f'  {k}')
