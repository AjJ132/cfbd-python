# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.16
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.venues_api import VenuesApi  # noqa: E501
from cfbd.rest import ApiException


class TestVenuesApi(unittest.TestCase):
    """VenuesApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.venues_api.VenuesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_venues(self):
        """Test case for get_venues

        Arena and venue information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
