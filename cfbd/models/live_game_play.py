# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.0
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator

class LiveGamePlay(BaseModel):
    """
    LiveGamePlay
    """
    id: StrictStr = Field(...)
    home_score: StrictInt = Field(default=..., alias="homeScore")
    away_score: StrictInt = Field(default=..., alias="awayScore")
    period: StrictInt = Field(...)
    clock: StrictStr = Field(...)
    wall_clock: datetime = Field(default=..., alias="wallClock")
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    down: StrictInt = Field(...)
    distance: StrictInt = Field(...)
    yards_to_goal: StrictInt = Field(default=..., alias="yardsToGoal")
    yards_gained: StrictInt = Field(default=..., alias="yardsGained")
    play_type_id: StrictInt = Field(default=..., alias="playTypeId")
    play_type: StrictStr = Field(default=..., alias="playType")
    epa: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    garbage_time: StrictBool = Field(default=..., alias="garbageTime")
    success: StrictBool = Field(...)
    rush_pash: StrictStr = Field(default=..., alias="rushPash")
    down_type: StrictStr = Field(default=..., alias="downType")
    play_text: StrictStr = Field(default=..., alias="playText")
    __properties = ["id", "homeScore", "awayScore", "period", "clock", "wallClock", "teamId", "team", "down", "distance", "yardsToGoal", "yardsGained", "playTypeId", "playType", "epa", "garbageTime", "success", "rushPash", "downType", "playText"]

    @validator('rush_pash')
    def rush_pash_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('rush', 'pass', 'other'):
            raise ValueError("must be one of enum values ('rush', 'pass', 'other')")
        return value

    @validator('down_type')
    def down_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('passing', 'standard'):
            raise ValueError("must be one of enum values ('passing', 'standard')")
        return value

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
    def from_json(cls, json_str: str) -> LiveGamePlay:
        """Create an instance of LiveGamePlay from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if epa (nullable) is None
        # and __fields_set__ contains the field
        if self.epa is None and "epa" in self.__fields_set__:
            _dict['epa'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LiveGamePlay:
        """Create an instance of LiveGamePlay from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LiveGamePlay.parse_obj(obj)

        _obj = LiveGamePlay.parse_obj({
            "id": obj.get("id"),
            "home_score": obj.get("homeScore"),
            "away_score": obj.get("awayScore"),
            "period": obj.get("period"),
            "clock": obj.get("clock"),
            "wall_clock": obj.get("wallClock"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "down": obj.get("down"),
            "distance": obj.get("distance"),
            "yards_to_goal": obj.get("yardsToGoal"),
            "yards_gained": obj.get("yardsGained"),
            "play_type_id": obj.get("playTypeId"),
            "play_type": obj.get("playType"),
            "epa": obj.get("epa"),
            "garbage_time": obj.get("garbageTime"),
            "success": obj.get("success"),
            "rush_pash": obj.get("rushPash"),
            "down_type": obj.get("downType"),
            "play_text": obj.get("playText")
        })
        return _obj


