#
# Copyright (C) 2018 - 2019 Satoru SATOH <satoru.satoh @ gmail.com>
# Copyright (C) 2015 - 2018 Satoru SATOH <ssato @ redhat.com>
# Copyright (C) 2017 Red Hat, Inc.
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
from __future__ import absolute_import

import msgpack

# import copy
import anyconfig_msgpack_backend as TT
import tests.common as TBC


class HasParserTrait(TBC.HasParserTrait):

    psr = TT.Parser()
    cnf = TBC.CNF_2
    cnf_s = msgpack.packb(cnf)


class Test_10(TBC.Test_10_dumps_and_loads, HasParserTrait):

    load_options = dict(use_single_float=True)


# pylint: disable=pointless-string-statement
"""
TODO:

    def test_40_loads_with_options(self):
        cnf = self.psr.loads(self.cnf_s, use_list=False)
        ref = copy.deepcopy(self.cnf)
        ref[_bytes("sect0")][_bytes("c")] = (_bytes("x"), _bytes("y"),
                                             _bytes("z"))
        self._assert_dicts_equal(cnf, ref)

    def test_42_dumps_with_options(self):
        cnf = self.psr.loads(self.psr.dumps(self.cnf, use_single_float=True))
        ref = copy.deepcopy(self.cnf)
        ref[_bytes("a")] = cnf[_bytes("a")]  # single float value.
        self._assert_dicts_equal(cnf, ref)


class Test_20(TBC.Test_20_dump_and_load, HasParserTrait):

    def test_40_load_with_options(self):
        cnf = self.psr.load(self.cnf_path, use_list=False)
        ref = copy.deepcopy(self.cnf)
        ref[_bytes("sect0")][_bytes("c")] = (_bytes("x"), _bytes("y"),
                                             _bytes("z"))
        self._assert_dicts_equal(cnf, ref)

    def test_42_dump_with_special_option(self):
        self.psr.dump(self.cnf, self.cnf_path, use_single_float=True)
        cnf = self.psr.load(self.cnf_path)
        ref = copy.deepcopy(self.cnf)
        ref[_bytes("a")] = cnf[_bytes("a")]  # single float value.
        self._assert_dicts_equal(cnf, ref)
"""

# vim:sw=4:ts=4:et:
