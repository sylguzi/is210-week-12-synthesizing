####################
IS 210 Assignment 12
####################
******************
Synthesizing Tasks
******************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Points: 12
:Due-Date: YYYY-MM-DDTHH:mm:ss

Overview
========

In this exercises we'll explore exceptions in the context of custom classes.
This is an important tool for delivering meaningful error messages when your
program encounters unexpected output.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Synthesizing Tasks
==================

Task 01
-------

Creating custom exception classes is a major part of any programming project.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_04.py``

#.  Create a new exception class named ``BaseException`` which simply extends
    ``Exception``

#.  Create three additional exception classes with the following hierarchies:

    #.  ``StringError``, subclassed to ``BaseException`` and ``TypeError``

    #.  ``NumberError``, subclassed to ``BaseException` and ``TypeError``

    #.  ``NonZeroError``, subclassed to ``NumberError``

Examples
^^^^^^^^

.. code:: pycon

    >>> issubclass(StringError, TypeError)
    True
    >>> issubclass(NumberError, BaseException)
    True

Task 02
-------

A custom exception class can sometimes offer important additional functionality
in debugging errors.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_05.py``

#.  Create a custom exception class named ``CustomError`` that is subclassed
    to ``Exception``

#.  ``CustomError`` has a custom constructor that calls
    ``Exception.__init__()`` but also takes a third parameter named ``cause``
    and stores its value as ``self.cause``

Examples
^^^^^^^^

.. code:: pycon

    >>> myerr = CustomError('Whoah!', cause='Messed up!')
    >>> print myerr.cause
    Messed up!

Task 03
-------

Except clauses may match multiple types of exceptions saving unnecessary
duplication and effort.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_06.py``

#.  Alter the ``except`` clause so that it catches ``TypeError``, ``KeyError``,
    and ``IndexError``

    #.  Do not add additional except clauses!

#.  Allow any other exceptions to occur naturally (uncaught)

.. tip::

    Check out Python's exceptions documentation for a neat way to capture both
    ``KeyError`` and ``IndexError`` in the same superclass.

Examples
^^^^^^^^

.. code:: pycon

    >>> exception_test(['apple'], 0, 'p')
    False
    >>> exception_test(43, 1, 1)
    True
    >>> exception_test(['apple'], 0, x)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'x' is not defined

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ bash runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
