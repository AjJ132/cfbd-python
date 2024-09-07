# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.20
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class MatchupGame(BaseModel):
    """
    MatchupGame
    """
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: StrictStr = Field(default=..., alias="seasonType")
    var_date: StrictStr = Field(default=..., alias="date")
    neutral_site: StrictBool = Field(default=..., alias="neutralSite")
    venue: StrictStr = Field(...)
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_score: StrictInt = Field(default=..., alias="homeScore")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_score: StrictInt = Field(default=..., alias="awayScore")
    winner: Optional[StrictStr] = Field(...)
    __properties = ["season", "week", "seasonType", "date", "neutralSite", "venue", "homeTeam", "homeScore", "awayTeam", "awayScore", "winner"]

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
    def from_json(cls, json_str: str) -> MatchupGame:
        """Create an instance of MatchupGame from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if winner (nullable) is None
        # and __fields_set__ contains the field
        if self.winner is None and "winner" in self.__fields_set__:
            _dict['winner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatchupGame:
        """Create an instance of MatchupGame from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatchupGame.parse_obj(obj)

        _obj = MatchupGame.parse_obj({
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "var_date": obj.get("date"),
            "neutral_site": obj.get("neutralSite"),
            "venue": obj.get("venue"),
            "home_team": obj.get("homeTeam"),
            "home_score": obj.get("homeScore"),
            "away_team": obj.get("awayTeam"),
            "away_score": obj.get("awayScore"),
            "winner": obj.get("winner")
        })
        return _obj


