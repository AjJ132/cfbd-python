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

from cfbd.models.matchup_game import MatchupGame  # noqa: E501

class TestMatchupGame(unittest.TestCase):
    """MatchupGame unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatchupGame:
        """Test MatchupGame
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatchupGame`
        """
        model = MatchupGame()  # noqa: E501
        if include_optional:
            return MatchupGame(
                season = 56,
                week = 56,
                season_type = '',
                var_date = '',
                neutral_site = True,
                venue = '',
                home_team = '',
                home_score = 56,
                away_team = '',
                away_score = 56,
                winner = ''
            )
        else:
            return MatchupGame(
                season = 56,
                week = 56,
                season_type = '',
                var_date = '',
                neutral_site = True,
                venue = '',
                home_team = '',
                home_score = 56,
                away_team = '',
                away_score = 56,
                winner = '',
        )
        """

    def testMatchupGame(self):
        """Test MatchupGame"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
