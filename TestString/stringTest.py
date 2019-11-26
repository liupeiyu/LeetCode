#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019-11-25 22:06 
# @name: stringTest
# @author：peiyu
import unittest
from  Platform.LeetCode.String import string_14_2

class StringTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @staticmethod
    def test_string_14():
        object=string_14_2.Solution()
        listparams=["flower","flow","flight"]
        print(object.longestCommonPrefix(listparams))


