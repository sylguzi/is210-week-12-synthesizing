#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 03."""


# Import Python libs
import datetime
import unittest


# Import user libs
import task_03


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""

    def test_no_error(self):
        """Tests proper operation when there is no error."""
        caught = task_03.exception_test(['apple'], 0, 'p')
        self.assertFalse(caught)

    def test_value_error(self):
        """Tests proper operation when an uncaught error occurs."""
        with self.assertRaises(Exception):
            task_03.exception_test(['apple'], 0, 'x')

    def test_type_error(self):
        """Tests proper operation when there a type error."""
        caught = task_03.exception_test(43, 1, 1)
        self.assertTrue(caught)

    def test_key_error(self):
        """Tests proper operation when there a key error."""
        caught = task_03.exception_test({}, 'key', 1)
        self.assertTrue(caught)

    def test_index_error(self):
        """Tests proper operation when there is no error."""
        caught = task_03.exception_test([], 0, 1)
        self.assertTrue(caught)


if __name__ == '__main__':
    unittest.main()
