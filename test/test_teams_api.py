# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.api.teams_api import TeamsApi  # noqa: E501
from cfbd.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = cfbd.api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_fbs_teams(self):
        """Test case for get_fbs_teams

        FBS team list  # noqa: E501
        """
        pass

    def test_get_roster(self):
        """Test case for get_roster

        Team rosters  # noqa: E501
        """
        pass

    def test_get_talent(self):
        """Test case for get_talent

        Team talent composite rankings  # noqa: E501
        """
        pass

    def test_get_team_matchup(self):
        """Test case for get_team_matchup

        Team matchup history  # noqa: E501
        """
        pass

    def test_get_teams(self):
        """Test case for get_teams

        Team information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
