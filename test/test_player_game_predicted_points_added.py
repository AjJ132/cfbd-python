# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.player_game_predicted_points_added import PlayerGamePredictedPointsAdded  # noqa: E501

class TestPlayerGamePredictedPointsAdded(unittest.TestCase):
    """PlayerGamePredictedPointsAdded unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerGamePredictedPointsAdded:
        """Test PlayerGamePredictedPointsAdded
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerGamePredictedPointsAdded`
        """
        model = PlayerGamePredictedPointsAdded()  # noqa: E501
        if include_optional:
            return PlayerGamePredictedPointsAdded(
                season = 56,
                week = 56,
                season_type = 'regular',
                id = '',
                name = '',
                position = '',
                team = '',
                opponent = '',
                average_ppa = cfbd.models.player_game_predicted_points_added_average_ppa.PlayerGamePredictedPointsAdded_averagePPA(
                    rush = 1.337, 
                    pass = 1.337, 
                    all = 1.337, )
            )
        else:
            return PlayerGamePredictedPointsAdded(
                season = 56,
                week = 56,
                season_type = 'regular',
                id = '',
                name = '',
                position = '',
                team = '',
                opponent = '',
                average_ppa = cfbd.models.player_game_predicted_points_added_average_ppa.PlayerGamePredictedPointsAdded_averagePPA(
                    rush = 1.337, 
                    pass = 1.337, 
                    all = 1.337, ),
        )
        """

    def testPlayerGamePredictedPointsAdded(self):
        """Test PlayerGamePredictedPointsAdded"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
