# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.2.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.player_season_predicted_points_added_average_ppa import PlayerSeasonPredictedPointsAddedAveragePPA  # noqa: E501

class TestPlayerSeasonPredictedPointsAddedAveragePPA(unittest.TestCase):
    """PlayerSeasonPredictedPointsAddedAveragePPA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PlayerSeasonPredictedPointsAddedAveragePPA:
        """Test PlayerSeasonPredictedPointsAddedAveragePPA
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PlayerSeasonPredictedPointsAddedAveragePPA`
        """
        model = PlayerSeasonPredictedPointsAddedAveragePPA()  # noqa: E501
        if include_optional:
            return PlayerSeasonPredictedPointsAddedAveragePPA(
                passing_downs = 1.337,
                standard_downs = 1.337,
                third_down = 1.337,
                second_down = 1.337,
                first_down = 1.337,
                rush = 1.337,
                var_pass = 1.337,
                all = 1.337
            )
        else:
            return PlayerSeasonPredictedPointsAddedAveragePPA(
                all = 1.337,
        )
        """

    def testPlayerSeasonPredictedPointsAddedAveragePPA(self):
        """Test PlayerSeasonPredictedPointsAddedAveragePPA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
