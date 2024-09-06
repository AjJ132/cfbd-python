# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.19
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.stats_api import StatsApi  # noqa: E501


class TestStatsApi(unittest.TestCase):
    """StatsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StatsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_advanced_game_stats(self) -> None:
        """Test case for get_advanced_game_stats

        """
        pass

    def test_get_advanced_season_stats(self) -> None:
        """Test case for get_advanced_season_stats

        """
        pass

    def test_get_categories(self) -> None:
        """Test case for get_categories

        """
        pass

    def test_get_player_season_stats(self) -> None:
        """Test case for get_player_season_stats

        """
        pass

    def test_get_team_stats(self) -> None:
        """Test case for get_team_stats

        """
        pass


if __name__ == '__main__':
    unittest.main()
