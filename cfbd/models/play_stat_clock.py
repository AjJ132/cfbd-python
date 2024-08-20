# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.10
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class PlayStatClock(BaseModel):
    """
    PlayStatClock
    """
    seconds: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    minutes: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    __properties = ["seconds", "minutes"]

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
    def from_json(cls, json_str: str) -> PlayStatClock:
        """Create an instance of PlayStatClock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if seconds (nullable) is None
        # and __fields_set__ contains the field
        if self.seconds is None and "seconds" in self.__fields_set__:
            _dict['seconds'] = None

        # set to None if minutes (nullable) is None
        # and __fields_set__ contains the field
        if self.minutes is None and "minutes" in self.__fields_set__:
            _dict['minutes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayStatClock:
        """Create an instance of PlayStatClock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayStatClock.parse_obj(obj)

        _obj = PlayStatClock.parse_obj({
            "seconds": obj.get("seconds"),
            "minutes": obj.get("minutes")
        })
        return _obj


