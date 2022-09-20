# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.4
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cfbd
from cfbd.models.team_game_teams import TeamGameTeams  # noqa: E501
from cfbd.rest import ApiException


class TestTeamGameTeams(unittest.TestCase):
    """TeamGameTeams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTeamGameTeams(self):
        """Test TeamGameTeams"""
        # FIXME: construct object with mandatory attributes with example values
        # model = cfbd.models.team_game_teams.TeamGameTeams()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
