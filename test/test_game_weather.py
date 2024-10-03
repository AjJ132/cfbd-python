# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.3.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.game_weather import GameWeather  # noqa: E501

class TestGameWeather(unittest.TestCase):
    """GameWeather unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GameWeather:
        """Test GameWeather
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GameWeather`
        """
        model = GameWeather()  # noqa: E501
        if include_optional:
            return GameWeather(
                id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                game_indoors = True,
                home_team = '',
                home_conference = '',
                away_team = '',
                away_conference = '',
                venue_id = 56,
                venue = '',
                temperature = 1.337,
                dew_point = 1.337,
                humidity = 1.337,
                precipitation = 1.337,
                snowfall = 1.337,
                wind_direction = 1.337,
                wind_speed = 1.337,
                pressure = 1.337,
                weather_condition_code = 1.337,
                weather_condition = ''
            )
        else:
            return GameWeather(
                id = 56,
                season = 56,
                week = 56,
                season_type = 'regular',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                game_indoors = True,
                home_team = '',
                home_conference = '',
                away_team = '',
                away_conference = '',
                venue_id = 56,
                venue = '',
                temperature = 1.337,
                dew_point = 1.337,
                humidity = 1.337,
                precipitation = 1.337,
                snowfall = 1.337,
                wind_direction = 1.337,
                wind_speed = 1.337,
                pressure = 1.337,
                weather_condition_code = 1.337,
                weather_condition = '',
        )
        """

    def testGameWeather(self):
        """Test GameWeather"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
