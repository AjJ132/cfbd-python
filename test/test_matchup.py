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

from cfbd.models.matchup import Matchup  # noqa: E501

class TestMatchup(unittest.TestCase):
    """Matchup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Matchup:
        """Test Matchup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Matchup`
        """
        model = Matchup()  # noqa: E501
        if include_optional:
            return Matchup(
                team1 = '',
                team2 = '',
                start_year = 56,
                end_year = 56,
                team1_wins = 56,
                team2_wins = 56,
                ties = 56,
                games = [
                    cfbd.models.matchup_game.MatchupGame(
                        season = 56, 
                        week = 56, 
                        season_type = '', 
                        date = '', 
                        neutral_site = True, 
                        venue = '', 
                        home_team = '', 
                        home_score = 56, 
                        away_team = '', 
                        away_score = 56, 
                        winner = '', )
                    ]
            )
        else:
            return Matchup(
                team1 = '',
                team2 = '',
                team1_wins = 56,
                team2_wins = 56,
                ties = 56,
                games = [
                    cfbd.models.matchup_game.MatchupGame(
                        season = 56, 
                        week = 56, 
                        season_type = '', 
                        date = '', 
                        neutral_site = True, 
                        venue = '', 
                        home_team = '', 
                        home_score = 56, 
                        away_team = '', 
                        away_score = 56, 
                        winner = '', )
                    ],
        )
        """

    def testMatchup(self):
        """Test Matchup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
