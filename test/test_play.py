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

from cfbd.models.play import Play  # noqa: E501

class TestPlay(unittest.TestCase):
    """Play unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Play:
        """Test Play
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Play`
        """
        model = Play()  # noqa: E501
        if include_optional:
            return Play(
                id = '',
                drive_id = '',
                game_id = 56,
                drive_number = 56,
                play_number = 56,
                offense = '',
                offense_conference = '',
                offense_score = 56,
                defense = '',
                home = '',
                away = '',
                defense_conference = '',
                defense_score = 56,
                period = 56,
                clock = cfbd.models.play_clock.Play_clock(
                    seconds = 56, 
                    minutes = 56, ),
                offense_timeouts = 56,
                defense_timeouts = 56,
                yardline = 56,
                yards_to_goal = 56,
                down = 56,
                distance = 56,
                yards_gained = 56,
                scoring = True,
                play_type = '',
                play_text = '',
                ppa = 1.337,
                wallclock = ''
            )
        else:
            return Play(
                id = '',
                drive_id = '',
                game_id = 56,
                drive_number = 56,
                play_number = 56,
                offense = '',
                offense_conference = '',
                offense_score = 56,
                defense = '',
                home = '',
                away = '',
                defense_conference = '',
                defense_score = 56,
                period = 56,
                clock = cfbd.models.play_clock.Play_clock(
                    seconds = 56, 
                    minutes = 56, ),
                offense_timeouts = 56,
                defense_timeouts = 56,
                yardline = 56,
                yards_to_goal = 56,
                down = 56,
                distance = 56,
                yards_gained = 56,
                scoring = True,
                play_type = '',
                play_text = '',
                ppa = 1.337,
                wallclock = '',
        )
        """

    def testPlay(self):
        """Test Play"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
