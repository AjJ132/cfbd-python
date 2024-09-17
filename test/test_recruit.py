# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.recruit import Recruit  # noqa: E501

class TestRecruit(unittest.TestCase):
    """Recruit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Recruit:
        """Test Recruit
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Recruit`
        """
        model = Recruit()  # noqa: E501
        if include_optional:
            return Recruit(
                id = '',
                athlete_id = '',
                recruit_type = 'JUCO',
                year = 56,
                ranking = 56,
                name = '',
                school = '',
                committed_to = '',
                position = '',
                height = 56,
                weight = 56,
                stars = 56,
                rating = 1.337,
                city = '',
                state_province = '',
                country = '',
                hometown_info = cfbd.models.recruit_hometown_info.Recruit_hometownInfo(
                    fips_code = '', 
                    longitude = 1.337, 
                    latitude = 1.337, )
            )
        else:
            return Recruit(
                id = '',
                athlete_id = '',
                recruit_type = 'JUCO',
                year = 56,
                ranking = 56,
                name = '',
                school = '',
                committed_to = '',
                position = '',
                height = 56,
                weight = 56,
                stars = 56,
                rating = 1.337,
                city = '',
                state_province = '',
                country = '',
                hometown_info = cfbd.models.recruit_hometown_info.Recruit_hometownInfo(
                    fips_code = '', 
                    longitude = 1.337, 
                    latitude = 1.337, ),
        )
        """

    def testRecruit(self):
        """Test Recruit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
