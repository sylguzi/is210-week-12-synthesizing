#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Second task of the 12th week"""


class CustomError(Exception):
    """Class CustomError, Subclass of Exception"""

    def __init__(self, msg, cause):
        """constructor for CustomError
        Arguments:
            Exception: Self(for its constructor)
            msg(string): Message
            cause(string): Input
        Returns:
            A Custom Error
        Examples:
            >>> myerror = CustomError('Whoah!',
            cause='Messed up!')
            >>> print myerror.cause
            Messed up!
        """
        msg = Exception.__init__(self, msg)
        self.cause = cause
