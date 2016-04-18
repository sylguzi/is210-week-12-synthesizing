#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""First task of the 12th week"""


class BaseError(Exception):
    """class exception"""
    pass


class StringError(BaseError, TypeError):
    """class exception"""
    pass


class NumberError(BaseError, TypeError):
    """vlass exception"""
    pass


class NonZeroError(NumberError):
    """class exception"""
    pass
