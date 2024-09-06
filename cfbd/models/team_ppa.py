# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.19
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.stats_by_quarter import StatsByQuarter

class TeamPPA(BaseModel):
    """
    TeamPPA
    """
    team: StrictStr = Field(...)
    plays: StrictInt = Field(...)
    overall: StatsByQuarter = Field(...)
    passing: StatsByQuarter = Field(...)
    rushing: StatsByQuarter = Field(...)
    __properties = ["team", "plays", "overall", "passing", "rushing"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TeamPPA:
        """Create an instance of TeamPPA from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of overall
        if self.overall:
            _dict['overall'] = self.overall.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passing
        if self.passing:
            _dict['passing'] = self.passing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rushing
        if self.rushing:
            _dict['rushing'] = self.rushing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TeamPPA:
        """Create an instance of TeamPPA from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TeamPPA.parse_obj(obj)

        _obj = TeamPPA.parse_obj({
            "team": obj.get("team"),
            "plays": obj.get("plays"),
            "overall": StatsByQuarter.from_dict(obj.get("overall")) if obj.get("overall") is not None else None,
            "passing": StatsByQuarter.from_dict(obj.get("passing")) if obj.get("passing") is not None else None,
            "rushing": StatsByQuarter.from_dict(obj.get("rushing")) if obj.get("rushing") is not None else None
        })
        return _obj


