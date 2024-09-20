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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class PollRank(BaseModel):
    """
    PollRank
    """
    rank: Optional[StrictInt] = Field(...)
    school: StrictStr = Field(...)
    conference: Optional[StrictStr] = Field(...)
    first_place_votes: Optional[StrictInt] = Field(default=..., alias="firstPlaceVotes")
    points: Optional[StrictInt] = Field(...)
    __properties = ["rank", "school", "conference", "firstPlaceVotes", "points"]

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
    def from_json(cls, json_str: str) -> PollRank:
        """Create an instance of PollRank from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if rank (nullable) is None
        # and __fields_set__ contains the field
        if self.rank is None and "rank" in self.__fields_set__:
            _dict['rank'] = None

        # set to None if conference (nullable) is None
        # and __fields_set__ contains the field
        if self.conference is None and "conference" in self.__fields_set__:
            _dict['conference'] = None

        # set to None if first_place_votes (nullable) is None
        # and __fields_set__ contains the field
        if self.first_place_votes is None and "first_place_votes" in self.__fields_set__:
            _dict['firstPlaceVotes'] = None

        # set to None if points (nullable) is None
        # and __fields_set__ contains the field
        if self.points is None and "points" in self.__fields_set__:
            _dict['points'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PollRank:
        """Create an instance of PollRank from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PollRank.parse_obj(obj)

        _obj = PollRank.parse_obj({
            "rank": obj.get("rank"),
            "school": obj.get("school"),
            "conference": obj.get("conference"),
            "first_place_votes": obj.get("firstPlaceVotes"),
            "points": obj.get("points")
        })
        return _obj


