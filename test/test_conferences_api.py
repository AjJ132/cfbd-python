# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\").  # noqa: E501

    OpenAPI spec version: 3.1.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.conferences_api import ConferencesApi  # noqa: E501
from cfbd.rest import ApiException


class TestConferencesApi(unittest.TestCase):
    """ConferencesApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.conferences_api.ConferencesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_conferences(self):
        """Test case for get_conferences

        Conferences  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
