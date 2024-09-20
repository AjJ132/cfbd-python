# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cfbd.models.draft_pick_hometown_info import DraftPickHometownInfo  # noqa: E501

class TestDraftPickHometownInfo(unittest.TestCase):
    """DraftPickHometownInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DraftPickHometownInfo:
        """Test DraftPickHometownInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DraftPickHometownInfo`
        """
        model = DraftPickHometownInfo()  # noqa: E501
        if include_optional:
            return DraftPickHometownInfo(
                county_fips = '',
                longitude = '',
                latitude = '',
                country = '',
                state = '',
                city = ''
            )
        else:
            return DraftPickHometownInfo(
                county_fips = '',
                longitude = '',
                latitude = '',
                country = '',
                state = '',
                city = '',
        )
        """

    def testDraftPickHometownInfo(self):
        """Test DraftPickHometownInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
