# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.conference_sp import ConferenceSP  # noqa: E501

class TestConferenceSP(unittest.TestCase):
    """ConferenceSP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceSP:
        """Test ConferenceSP
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferenceSP`
        """
        model = ConferenceSP()  # noqa: E501
        if include_optional:
            return ConferenceSP(
                year = 56,
                conference = '',
                rating = 1.337,
                second_order_wins = 1.337,
                sos = 1.337,
                offense = cfbd.models.conference_sp_offense.ConferenceSP_offense(
                    pace = 1.337, 
                    run_rate = 1.337, 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, ),
                defense = cfbd.models.conference_sp_defense.ConferenceSP_defense(
                    havoc = cfbd.models.advanced_season_stat_offense_havoc.AdvancedSeasonStat_offense_havoc(
                        db = 1.337, 
                        front_seven = 1.337, 
                        total = 1.337, ), 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, ),
                special_teams = cfbd.models.team_sp_special_teams.TeamSP_specialTeams(
                    rating = 1.337, )
            )
        else:
            return ConferenceSP(
                year = 56,
                conference = '',
                rating = 1.337,
                second_order_wins = 1.337,
                sos = 1.337,
                offense = cfbd.models.conference_sp_offense.ConferenceSP_offense(
                    pace = 1.337, 
                    run_rate = 1.337, 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, ),
                defense = cfbd.models.conference_sp_defense.ConferenceSP_defense(
                    havoc = cfbd.models.advanced_season_stat_offense_havoc.AdvancedSeasonStat_offense_havoc(
                        db = 1.337, 
                        front_seven = 1.337, 
                        total = 1.337, ), 
                    passing_downs = 1.337, 
                    standard_downs = 1.337, 
                    passing = 1.337, 
                    rushing = 1.337, 
                    explosiveness = 1.337, 
                    success = 1.337, 
                    rating = 1.337, ),
                special_teams = cfbd.models.team_sp_special_teams.TeamSP_specialTeams(
                    rating = 1.337, ),
        )
        """

    def testConferenceSP(self):
        """Test ConferenceSP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
