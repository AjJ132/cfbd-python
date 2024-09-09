# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.21
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.metrics_api import MetricsApi  # noqa: E501


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_field_goal_expected_points(self) -> None:
        """Test case for get_field_goal_expected_points

        """
        pass

    def test_get_predicted_points(self) -> None:
        """Test case for get_predicted_points

        """
        pass

    def test_get_predicted_points_added_by_game(self) -> None:
        """Test case for get_predicted_points_added_by_game

        """
        pass

    def test_get_predicted_points_added_by_player_game(self) -> None:
        """Test case for get_predicted_points_added_by_player_game

        """
        pass

    def test_get_predicted_points_added_by_player_season(self) -> None:
        """Test case for get_predicted_points_added_by_player_season

        """
        pass

    def test_get_predicted_points_added_by_team(self) -> None:
        """Test case for get_predicted_points_added_by_team

        """
        pass

    def test_get_pregame_win_probabilities(self) -> None:
        """Test case for get_pregame_win_probabilities

        """
        pass

    def test_get_win_probability(self) -> None:
        """Test case for get_win_probability

        """
        pass


if __name__ == '__main__':
    unittest.main()
