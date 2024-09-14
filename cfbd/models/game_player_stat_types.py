# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.1
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist
from cfbd.models.game_player_stat_player import GamePlayerStatPlayer

class GamePlayerStatTypes(BaseModel):
    """
    GamePlayerStatTypes
    """
    name: StrictStr = Field(...)
    athletes: conlist(GamePlayerStatPlayer) = Field(...)
    __properties = ["name", "athletes"]

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
    def from_json(cls, json_str: str) -> GamePlayerStatTypes:
        """Create an instance of GamePlayerStatTypes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in athletes (list)
        _items = []
        if self.athletes:
            for _item in self.athletes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['athletes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GamePlayerStatTypes:
        """Create an instance of GamePlayerStatTypes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GamePlayerStatTypes.parse_obj(obj)

        _obj = GamePlayerStatTypes.parse_obj({
            "name": obj.get("name"),
            "athletes": [GamePlayerStatPlayer.from_dict(_item) for _item in obj.get("athletes")] if obj.get("athletes") is not None else None
        })
        return _obj


