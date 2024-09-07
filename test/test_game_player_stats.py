# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.20
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_player_stats import GamePlayerStats  # noqa: E501

class TestGamePlayerStats(unittest.TestCase):
    """GamePlayerStats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GamePlayerStats:
        """Test GamePlayerStats
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GamePlayerStats`
        """
        model = GamePlayerStats()  # noqa: E501
        if include_optional:
            return GamePlayerStats(
                id = 56,
                teams = [
                    cfbd.models.game_player_stats_team.GamePlayerStatsTeam(
                        team = '', 
                        conference = '', 
                        home_away = 'home', 
                        points = 56, 
                        categories = [
                            cfbd.models.game_player_stat_categories.GamePlayerStatCategories(
                                name = '', 
                                types = [
                                    cfbd.models.game_player_stat_types.GamePlayerStatTypes(
                                        name = '', 
                                        athletes = [
                                            cfbd.models.game_player_stat_player.GamePlayerStatPlayer(
                                                id = '', 
                                                name = '', 
                                                stat = '', )
                                            ], )
                                    ], )
                            ], )
                    ]
            )
        else:
            return GamePlayerStats(
                id = 56,
                teams = [
                    cfbd.models.game_player_stats_team.GamePlayerStatsTeam(
                        team = '', 
                        conference = '', 
                        home_away = 'home', 
                        points = 56, 
                        categories = [
                            cfbd.models.game_player_stat_categories.GamePlayerStatCategories(
                                name = '', 
                                types = [
                                    cfbd.models.game_player_stat_types.GamePlayerStatTypes(
                                        name = '', 
                                        athletes = [
                                            cfbd.models.game_player_stat_player.GamePlayerStatPlayer(
                                                id = '', 
                                                name = '', 
                                                stat = '', )
                                            ], )
                                    ], )
                            ], )
                    ],
        )
        """

    def testGamePlayerStats(self):
        """Test GamePlayerStats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
