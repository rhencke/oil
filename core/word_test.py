#!/usr/bin/env python
"""
word_test.py: Tests for word.py
"""

import unittest

from core import word  # module under test


class WordTest(unittest.TestCase):

  def testFoo(self):
    print word


if __name__ == '__main__':
  unittest.main()
