# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.2.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.scoreboard_game_home_team import ScoreboardGameHomeTeam  # noqa: E501

class TestScoreboardGameHomeTeam(unittest.TestCase):
    """ScoreboardGameHomeTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScoreboardGameHomeTeam:
        """Test ScoreboardGameHomeTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScoreboardGameHomeTeam`
        """
        model = ScoreboardGameHomeTeam()  # noqa: E501
        if include_optional:
            return ScoreboardGameHomeTeam(
                line_scores = [
                    56
                    ],
                points = 56,
                classification = 'fbs',
                conference = '',
                name = '',
                id = 56
            )
        else:
            return ScoreboardGameHomeTeam(
                line_scores = [
                    56
                    ],
                points = 56,
                classification = 'fbs',
                conference = '',
                name = '',
                id = 56,
        )
        """

    def testScoreboardGameHomeTeam(self):
        """Test ScoreboardGameHomeTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
