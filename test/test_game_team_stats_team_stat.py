# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.12
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_team_stats_team_stat import GameTeamStatsTeamStat  # noqa: E501

class TestGameTeamStatsTeamStat(unittest.TestCase):
    """GameTeamStatsTeamStat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameTeamStatsTeamStat:
        """Test GameTeamStatsTeamStat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameTeamStatsTeamStat`
        """
        model = GameTeamStatsTeamStat()  # noqa: E501
        if include_optional:
            return GameTeamStatsTeamStat(
                category = '',
                stat = ''
            )
        else:
            return GameTeamStatsTeamStat(
                category = '',
                stat = '',
        )
        """

    def testGameTeamStatsTeamStat(self):
        """Test GameTeamStatsTeamStat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
