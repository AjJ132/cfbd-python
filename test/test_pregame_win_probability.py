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

from cfbd.models.pregame_win_probability import PregameWinProbability  # noqa: E501

class TestPregameWinProbability(unittest.TestCase):
    """PregameWinProbability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PregameWinProbability:
        """Test PregameWinProbability
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PregameWinProbability`
        """
        model = PregameWinProbability()  # noqa: E501
        if include_optional:
            return PregameWinProbability(
                season = 56,
                season_type = 'regular',
                week = 56,
                game_id = 56,
                home_team = '',
                away_team = '',
                spread = 1.337,
                home_win_probability = 1.337
            )
        else:
            return PregameWinProbability(
                season = 56,
                season_type = 'regular',
                week = 56,
                game_id = 56,
                home_team = '',
                away_team = '',
                spread = 1.337,
                home_win_probability = 1.337,
        )
        """

    def testPregameWinProbability(self):
        """Test PregameWinProbability"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
