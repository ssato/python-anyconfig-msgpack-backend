==================================
python-anyconfig-msgpack-backend
==================================

.. image:: https://img.shields.io/pypi/v/anyconfig-msgpack-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-msgpack-backend/
   :alt: [Latest Version]

.. image:: https://img.shields.io/pypi/pyversions/anyconfig.svg
   :target: https://pypi.python.org/pypi/anyconfig/
   :alt: [Python versions]

.. image:: https://img.shields.io/pypi/l/anyconfig.svg
   :target: https://pypi.python.org/pypi/anyconfig/
   :alt: MIT License

.. image:: https://github.com/ssato/python-anyconfig-msgpack-backend/workflows/Tests/badge.svg
   :target: https://github.com/ssato/python-anyconfig-msgpack-backend/actions?query=workflow%3ATests
   :alt: [Github Actions: Test status]


.. image:: https://dev.azure.com/satorusatoh0471/python-anyconfig-msgpack-backend/_apis/build/status%2Fssato.python-anyconfig-msgpack-backend?branchName=next
   :target: https://dev.azure.com/satorusatoh0471/python-anyconfig-msgpack-backend/_build/latest?definitionId=1
   :alt: [Azure Pipelines Status]

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-msgpack-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-msgpack-backend
   :alt: Coverage Status

.. image:: https://scrutinizer-ci.com/g/ssato/python-anyconfig-msgpack-backend/badges/quality-score.png?b=next
   :target: https://scrutinizer-ci.com/g/ssato/python-anyconfig-msgpack-backend
   :alt: [Code Quality by Scrutinizer]

This is a backend module for python-anyconfig to support to load and dump
MessagePack data files.

- Author: Satoru SATOH <ssato@redhat.com>
- License: MIT

SEE ALSO:

- python-anyconfig: https://pypi.python.org/pypi/anyconfig
- MessagePack: http://msgpack.org
- Download:

  - PyPI: https://pypi.python.org/pypi/anyconfig-msgpack-backend
  - Copr RPM repos: https://copr.fedoraproject.org/coprs/ssato/python-anyconfig/

Build & Install
================

If you're Fedora or Red Hat Enterprise Linux user, try::

  $ python setup.py srpm && mock dist/<package>-<ver_dist>.src.rpm
  
or::

  $ python setup.py rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:
