# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TransferEligibility(str, Enum):
    """
    TransferEligibility
    """

    """
    allowed enum values
    """
    WITHDRAWN = 'Withdrawn'
    TBD = 'TBD'
    PENDINGAPPEAL = 'PendingAppeal'
    SITTINGONE = 'SittingOne'
    IMMEDIATE = 'Immediate'

    @classmethod
    def from_json(cls, json_str: str) -> TransferEligibility:
        """Create an instance of TransferEligibility from a JSON string"""
        return TransferEligibility(json.loads(json_str))


