# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.2.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cfbd.api.rankings_api import RankingsApi  # noqa: E501


class TestRankingsApi(unittest.TestCase):
    """RankingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RankingsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_rankings(self) -> None:
        """Test case for get_rankings

        """
        pass


if __name__ == '__main__':
    unittest.main()
