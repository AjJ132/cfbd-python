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
import datetime

from cfbd.models.advanced_season_stat_offense_field_position import AdvancedSeasonStatOffenseFieldPosition  # noqa: E501

class TestAdvancedSeasonStatOffenseFieldPosition(unittest.TestCase):
    """AdvancedSeasonStatOffenseFieldPosition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvancedSeasonStatOffenseFieldPosition:
        """Test AdvancedSeasonStatOffenseFieldPosition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvancedSeasonStatOffenseFieldPosition`
        """
        model = AdvancedSeasonStatOffenseFieldPosition()  # noqa: E501
        if include_optional:
            return AdvancedSeasonStatOffenseFieldPosition(
                average_predicted_points = 1.337,
                average_start = 1.337
            )
        else:
            return AdvancedSeasonStatOffenseFieldPosition(
                average_predicted_points = 1.337,
                average_start = 1.337,
        )
        """

    def testAdvancedSeasonStatOffenseFieldPosition(self):
        """Test AdvancedSeasonStatOffenseFieldPosition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
