# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.19
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.play_clock import PlayClock  # noqa: E501

class TestPlayClock(unittest.TestCase):
    """PlayClock unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayClock:
        """Test PlayClock
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayClock`
        """
        model = PlayClock()  # noqa: E501
        if include_optional:
            return PlayClock(
                seconds = 56,
                minutes = 56
            )
        else:
            return PlayClock(
                seconds = 56,
                minutes = 56,
        )
        """

    def testPlayClock(self):
        """Test PlayClock"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
