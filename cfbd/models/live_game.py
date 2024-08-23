# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.12
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from cfbd.models.live_game_drive import LiveGameDrive
from cfbd.models.live_game_team import LiveGameTeam

class LiveGame(BaseModel):
    """
    LiveGame
    """
    id: StrictInt = Field(...)
    status: StrictStr = Field(...)
    period: Optional[StrictInt] = Field(...)
    clock: StrictStr = Field(...)
    possession: StrictStr = Field(...)
    down: Optional[StrictInt] = Field(...)
    distance: Optional[StrictInt] = Field(...)
    yards_to_goal: Optional[StrictInt] = Field(default=..., alias="yardsToGoal")
    teams: conlist(LiveGameTeam) = Field(...)
    drives: conlist(LiveGameDrive) = Field(...)
    __properties = ["id", "status", "period", "clock", "possession", "down", "distance", "yardsToGoal", "teams", "drives"]

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
    def from_json(cls, json_str: str) -> LiveGame:
        """Create an instance of LiveGame from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in teams (list)
        _items = []
        if self.teams:
            for _item in self.teams:
                if _item:
                    _items.append(_item.to_dict())
            _dict['teams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in drives (list)
        _items = []
        if self.drives:
            for _item in self.drives:
                if _item:
                    _items.append(_item.to_dict())
            _dict['drives'] = _items
        # set to None if period (nullable) is None
        # and __fields_set__ contains the field
        if self.period is None and "period" in self.__fields_set__:
            _dict['period'] = None

        # set to None if down (nullable) is None
        # and __fields_set__ contains the field
        if self.down is None and "down" in self.__fields_set__:
            _dict['down'] = None

        # set to None if distance (nullable) is None
        # and __fields_set__ contains the field
        if self.distance is None and "distance" in self.__fields_set__:
            _dict['distance'] = None

        # set to None if yards_to_goal (nullable) is None
        # and __fields_set__ contains the field
        if self.yards_to_goal is None and "yards_to_goal" in self.__fields_set__:
            _dict['yardsToGoal'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LiveGame:
        """Create an instance of LiveGame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LiveGame.parse_obj(obj)

        _obj = LiveGame.parse_obj({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "period": obj.get("period"),
            "clock": obj.get("clock"),
            "possession": obj.get("possession"),
            "down": obj.get("down"),
            "distance": obj.get("distance"),
            "yards_to_goal": obj.get("yardsToGoal"),
            "teams": [LiveGameTeam.from_dict(_item) for _item in obj.get("teams")] if obj.get("teams") is not None else None,
            "drives": [LiveGameDrive.from_dict(_item) for _item in obj.get("drives")] if obj.get("drives") is not None else None
        })
        return _obj


