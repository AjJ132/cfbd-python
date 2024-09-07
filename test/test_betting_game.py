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

from cfbd.models.betting_game import BettingGame  # noqa: E501

class TestBettingGame(unittest.TestCase):
    """BettingGame unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BettingGame:
        """Test BettingGame
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BettingGame`
        """
        model = BettingGame()  # noqa: E501
        if include_optional:
            return BettingGame(
                id = 56,
                season = 56,
                season_type = 'regular',
                week = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                home_team = '',
                home_conference = '',
                home_classification = 'fbs',
                home_score = 56,
                away_team = '',
                away_conference = '',
                away_classification = 'fbs',
                away_score = 56,
                lines = [
                    cfbd.models.game_line.GameLine(
                        provider = '', 
                        spread = 1.337, 
                        formatted_spread = '', 
                        spread_open = 1.337, 
                        over_under = 1.337, 
                        over_under_open = 1.337, 
                        home_moneyline = 1.337, 
                        away_moneyline = 1.337, )
                    ]
            )
        else:
            return BettingGame(
                id = 56,
                season = 56,
                season_type = 'regular',
                week = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                home_team = '',
                home_conference = '',
                home_classification = 'fbs',
                home_score = 56,
                away_team = '',
                away_conference = '',
                away_classification = 'fbs',
                away_score = 56,
                lines = [
                    cfbd.models.game_line.GameLine(
                        provider = '', 
                        spread = 1.337, 
                        formatted_spread = '', 
                        spread_open = 1.337, 
                        over_under = 1.337, 
                        over_under_open = 1.337, 
                        home_moneyline = 1.337, 
                        away_moneyline = 1.337, )
                    ],
        )
        """

    def testBettingGame(self):
        """Test BettingGame"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
