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

from cfbd.models.team_stat_stat_value import TeamStatStatValue  # noqa: E501

class TestTeamStatStatValue(unittest.TestCase):
    """TeamStatStatValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamStatStatValue:
        """Test TeamStatStatValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamStatStatValue`
        """
        model = TeamStatStatValue()  # noqa: E501
        if include_optional:
            return TeamStatStatValue(
            )
        else:
            return TeamStatStatValue(
        )
        """

    def testTeamStatStatValue(self):
        """Test TeamStatStatValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
