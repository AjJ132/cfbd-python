# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.2.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class PlayerStat(BaseModel):
    """
    PlayerStat
    """
    season: StrictInt = Field(...)
    player_id: StrictStr = Field(default=..., alias="playerId")
    player: StrictStr = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    category: StrictStr = Field(...)
    stat_type: StrictStr = Field(default=..., alias="statType")
    stat: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["season", "playerId", "player", "team", "conference", "category", "statType", "stat"]

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
    def from_json(cls, json_str: str) -> PlayerStat:
        """Create an instance of PlayerStat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerStat:
        """Create an instance of PlayerStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerStat.parse_obj(obj)

        _obj = PlayerStat.parse_obj({
            "season": obj.get("season"),
            "player_id": obj.get("playerId"),
            "player": obj.get("player"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "category": obj.get("category"),
            "stat_type": obj.get("statType"),
            "stat": obj.get("stat")
        })
        return _obj


