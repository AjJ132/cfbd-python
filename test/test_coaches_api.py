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

from cfbd.api.coaches_api import CoachesApi  # noqa: E501


class TestCoachesApi(unittest.TestCase):
    """CoachesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CoachesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_coaches(self) -> None:
        """Test case for get_coaches

        """
        pass


if __name__ == '__main__':
    unittest.main()
