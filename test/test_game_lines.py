# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.13
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.game_lines import GameLines  # noqa: E501
from cfbd.rest import ApiException


class TestGameLines(unittest.TestCase):
    """GameLines unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGameLines(self):
        """Test GameLines"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.game_lines.GameLines()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
