# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.team_rushing_stats import TeamRushingStats  # noqa: E501

class TestTeamRushingStats(unittest.TestCase):
    """TeamRushingStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TeamRushingStats:
        """Test TeamRushingStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TeamRushingStats`
        """
        model = TeamRushingStats()  # noqa: E501
        if include_optional:
            return TeamRushingStats(
                team = '',
                power_success = 1.337,
                stuff_rate = 1.337,
                line_yards = 1.337,
                line_yards_average = 1.337,
                second_level_yards = 1.337,
                second_level_yards_average = 1.337,
                open_field_yards = 1.337,
                open_field_yards_average = 1.337
            )
        else:
            return TeamRushingStats(
                team = '',
                power_success = 1.337,
                stuff_rate = 1.337,
                line_yards = 1.337,
                line_yards_average = 1.337,
                second_level_yards = 1.337,
                second_level_yards_average = 1.337,
                open_field_yards = 1.337,
                open_field_yards_average = 1.337,
        )
        """

    def testTeamRushingStats(self):
        """Test TeamRushingStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
