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

from cfbd.models.drive import Drive  # noqa: E501

class TestDrive(unittest.TestCase):
    """Drive unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Drive:
        """Test Drive
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Drive`
        """
        model = Drive()  # noqa: E501
        if include_optional:
            return Drive(
                offense = '',
                offense_conference = '',
                defense = '',
                defense_conference = '',
                game_id = 56,
                id = '',
                drive_number = 56,
                scoring = True,
                start_period = 56,
                start_yardline = 56,
                start_yards_to_goal = 56,
                start_time = cfbd.models.play_clock.Play_clock(
                    seconds = 56, 
                    minutes = 56, ),
                end_period = 56,
                end_yardline = 56,
                end_yards_to_goal = 56,
                end_time = cfbd.models.play_clock.Play_clock(
                    seconds = 56, 
                    minutes = 56, ),
                plays = 56,
                yards = 56,
                drive_result = '',
                is_home_offense = True,
                start_offense_score = 56,
                start_defense_score = 56,
                end_offense_score = 56,
                end_defense_score = 56
            )
        else:
            return Drive(
                offense = '',
                offense_conference = '',
                defense = '',
                defense_conference = '',
                game_id = 56,
                id = '',
                drive_number = 56,
                scoring = True,
                start_period = 56,
                start_yardline = 56,
                start_yards_to_goal = 56,
                start_time = cfbd.models.play_clock.Play_clock(
                    seconds = 56, 
                    minutes = 56, ),
                end_period = 56,
                end_yardline = 56,
                end_yards_to_goal = 56,
                end_time = cfbd.models.play_clock.Play_clock(
                    seconds = 56, 
                    minutes = 56, ),
                plays = 56,
                yards = 56,
                drive_result = '',
                is_home_offense = True,
                start_offense_score = 56,
                start_defense_score = 56,
                end_offense_score = 56,
                end_defense_score = 56,
        )
        """

    def testDrive(self):
        """Test Drive"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
