# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.3
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.portal_player import PortalPlayer  # noqa: E501
from cfbd.rest import ApiException


class TestPortalPlayer(unittest.TestCase):
    """PortalPlayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPortalPlayer(self):
        """Test PortalPlayer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.portal_player.PortalPlayer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
