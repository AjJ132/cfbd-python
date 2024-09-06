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
import datetime

from cfbd.models.conference_sp_defense import ConferenceSPDefense  # noqa: E501

class TestConferenceSPDefense(unittest.TestCase):
    """ConferenceSPDefense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConferenceSPDefense:
        """Test ConferenceSPDefense
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConferenceSPDefense`
        """
        model = ConferenceSPDefense()  # noqa: E501
        if include_optional:
            return ConferenceSPDefense(
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
                rating = 1.337
            )
        else:
            return ConferenceSPDefense(
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
                rating = 1.337,
        )
        """

    def testConferenceSPDefense(self):
        """Test ConferenceSPDefense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
