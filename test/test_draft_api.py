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

from cfbd.api.draft_api import DraftApi  # noqa: E501


class TestDraftApi(unittest.TestCase):
    """DraftApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DraftApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_draft_picks(self) -> None:
        """Test case for get_draft_picks

        """
        pass

    def test_get_draft_positions(self) -> None:
        """Test case for get_draft_positions

        """
        pass

    def test_get_draft_teams(self) -> None:
        """Test case for get_draft_teams

        """
        pass


if __name__ == '__main__':
    unittest.main()
