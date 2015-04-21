#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import datetime
import unittest


# Import user libs
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    def test_base_exception(self):
        """Tests that BaseException exists and is subclassed to Exception"""
        with self.assertRaises(Exception):
            raise task_01.BaseException

    def test_string_error_is_base(self):
        """Tests if StringError is a BaseException"""
        with self.assertRaises(task_01.BaseException):
            raise task_01.StringError

    def test_number_error_is_base(self):
        """Tests if NumberError is a BaseException"""
        with self.assertRaises(task_01.BaseException):
            raise task_01.NumberError

    def test_string_error_is_type(self):
        """Tests if StringError is a TypeError"""
        with self.assertRaises(TypeError):
            raise task_01.StringError

    def test_number_error_is_type(self):
        """Tests if NumberError is a TypeError"""
        with self.assertRaises(TypeError):
            raise task_01.NumberError

    def test_nonzeroerror_is_numbererror(self):
        """Tests if NonZeroError is a NumberError"""
        with self.assertRaises(task_01.NumberError):
            raise task_01.NonZeroError


if __name__ == '__main__':
    unittest.main()
