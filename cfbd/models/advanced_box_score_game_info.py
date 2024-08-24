# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.13
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class AdvancedBoxScoreGameInfo(BaseModel):
    """
    AdvancedBoxScoreGameInfo
    """
    excitement: Union[StrictFloat, StrictInt] = Field(...)
    home_winner: StrictBool = Field(default=..., alias="homeWinner")
    away_win_prob: Union[StrictFloat, StrictInt] = Field(default=..., alias="awayWinProb")
    away_points: StrictInt = Field(default=..., alias="awayPoints")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    home_win_prob: Union[StrictFloat, StrictInt] = Field(default=..., alias="homeWinProb")
    home_points: StrictInt = Field(default=..., alias="homePoints")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    __properties = ["excitement", "homeWinner", "awayWinProb", "awayPoints", "awayTeam", "homeWinProb", "homePoints", "homeTeam"]

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
    def from_json(cls, json_str: str) -> AdvancedBoxScoreGameInfo:
        """Create an instance of AdvancedBoxScoreGameInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedBoxScoreGameInfo:
        """Create an instance of AdvancedBoxScoreGameInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedBoxScoreGameInfo.parse_obj(obj)

        _obj = AdvancedBoxScoreGameInfo.parse_obj({
            "excitement": obj.get("excitement"),
            "home_winner": obj.get("homeWinner"),
            "away_win_prob": obj.get("awayWinProb"),
            "away_points": obj.get("awayPoints"),
            "away_team": obj.get("awayTeam"),
            "home_win_prob": obj.get("homeWinProb"),
            "home_points": obj.get("homePoints"),
            "home_team": obj.get("homeTeam")
        })
        return _obj


