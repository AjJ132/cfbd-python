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

from cfbd.models.play_stat import PlayStat  # noqa: E501

class TestPlayStat(unittest.TestCase):
    """PlayStat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayStat:
        """Test PlayStat
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayStat`
        """
        model = PlayStat()  # noqa: E501
        if include_optional:
            return PlayStat(
                game_id = 1.337,
                season = 1.337,
                week = 1.337,
                team = '',
                conference = '',
                opponent = '',
                team_score = 1.337,
                opponent_score = 1.337,
                drive_id = '',
                play_id = '',
                period = 1.337,
                clock = cfbd.models.play_stat_clock.PlayStat_clock(
                    seconds = 1.337, 
                    minutes = 1.337, ),
                yards_to_goal = 1.337,
                down = 1.337,
                distance = 1.337,
                athlete_id = '',
                athlete_name = '',
                stat_type = '',
                stat = 1.337
            )
        else:
            return PlayStat(
                game_id = 1.337,
                season = 1.337,
                week = 1.337,
                team = '',
                conference = '',
                opponent = '',
                team_score = 1.337,
                opponent_score = 1.337,
                drive_id = '',
                play_id = '',
                period = 1.337,
                clock = cfbd.models.play_stat_clock.PlayStat_clock(
                    seconds = 1.337, 
                    minutes = 1.337, ),
                yards_to_goal = 1.337,
                down = 1.337,
                distance = 1.337,
                athlete_id = '',
                athlete_name = '',
                stat_type = '',
                stat = 1.337,
        )
        """

    def testPlayStat(self):
        """Test PlayStat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
