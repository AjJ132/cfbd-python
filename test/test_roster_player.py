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

from cfbd.models.roster_player import RosterPlayer  # noqa: E501

class TestRosterPlayer(unittest.TestCase):
    """RosterPlayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RosterPlayer:
        """Test RosterPlayer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RosterPlayer`
        """
        model = RosterPlayer()  # noqa: E501
        if include_optional:
            return RosterPlayer(
                id = '',
                first_name = '',
                last_name = '',
                team = '',
                height = 56,
                weight = 56,
                jersey = 56,
                year = 56,
                position = '',
                home_city = '',
                home_state = '',
                home_country = '',
                home_latitude = 1.337,
                home_longitude = 1.337,
                home_county_fips = '',
                recruit_ids = [
                    ''
                    ]
            )
        else:
            return RosterPlayer(
                id = '',
                first_name = '',
                last_name = '',
                team = '',
                height = 56,
                weight = 56,
                jersey = 56,
                year = 56,
                position = '',
                home_city = '',
                home_state = '',
                home_country = '',
                home_latitude = 1.337,
                home_longitude = 1.337,
                home_county_fips = '',
                recruit_ids = [
                    ''
                    ],
        )
        """

    def testRosterPlayer(self):
        """Test RosterPlayer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
