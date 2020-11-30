# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.players_api import PlayersApi  # noqa: E501
from cfbd.rest import ApiException


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.players_api.PlayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_player_season_stats(self):
        """Test case for get_player_season_stats

        Player stats by season  # noqa: E501
        """
        pass

    def test_get_player_usage(self):
        """Test case for get_player_usage

        Player usage metrics broken down by season  # noqa: E501
        """
        pass

    def test_get_returning_production(self):
        """Test case for get_returning_production

        Team returning production metrics  # noqa: E501
        """
        pass

    def test_player_search(self):
        """Test case for player_search

        Search for player information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
