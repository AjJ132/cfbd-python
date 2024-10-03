# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.3.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_stat import TeamStat  # noqa: E501

class TestTeamStat(unittest.TestCase):
    """TeamStat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamStat:
        """Test TeamStat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamStat`
        """
        model = TeamStat()  # noqa: E501
        if include_optional:
            return TeamStat(
                season = 56,
                team = '',
                conference = '',
                stat_name = '',
                stat_value = None
            )
        else:
            return TeamStat(
                season = 56,
                team = '',
                conference = '',
                stat_name = '',
                stat_value = None,
        )
        """

    def testTeamStat(self):
        """Test TeamStat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
