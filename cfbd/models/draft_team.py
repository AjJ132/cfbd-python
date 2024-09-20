# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.3
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class DraftTeam(BaseModel):
    """
    DraftTeam
    """
    location: StrictStr = Field(...)
    nickname: Optional[StrictStr] = Field(...)
    display_name: Optional[StrictStr] = Field(default=..., alias="displayName")
    logo: Optional[StrictStr] = Field(...)
    __properties = ["location", "nickname", "displayName", "logo"]

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
    def from_json(cls, json_str: str) -> DraftTeam:
        """Create an instance of DraftTeam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if nickname (nullable) is None
        # and __fields_set__ contains the field
        if self.nickname is None and "nickname" in self.__fields_set__:
            _dict['nickname'] = None

        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if logo (nullable) is None
        # and __fields_set__ contains the field
        if self.logo is None and "logo" in self.__fields_set__:
            _dict['logo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DraftTeam:
        """Create an instance of DraftTeam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DraftTeam.parse_obj(obj)

        _obj = DraftTeam.parse_obj({
            "location": obj.get("location"),
            "nickname": obj.get("nickname"),
            "display_name": obj.get("displayName"),
            "logo": obj.get("logo")
        })
        return _obj


