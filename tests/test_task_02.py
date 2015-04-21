#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import datetime
import unittest


# Import user libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""

    def test_customerror_is_exception(self):
        """Tests that CustomError exists and is subclassed to Exception"""
        with self.assertRaises(Exception):
            raise task_02.CustomError('Message', 'Cause')

    def test_customerror_stores_cause(self):
        cerr = task_02.CustomError('Message', 'Cause')
        self.assertEqual(cerr.cause, 'Cause')


if __name__ == '__main__':
    unittest.main()
