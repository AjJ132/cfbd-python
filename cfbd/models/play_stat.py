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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cfbd.models.play_stat_clock import PlayStatClock

class PlayStat(BaseModel):
    """
    PlayStat
    """
    game_id: Union[StrictFloat, StrictInt] = Field(default=..., alias="gameId")
    season: Union[StrictFloat, StrictInt] = Field(...)
    week: Union[StrictFloat, StrictInt] = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    opponent: StrictStr = Field(...)
    team_score: Union[StrictFloat, StrictInt] = Field(default=..., alias="teamScore")
    opponent_score: Union[StrictFloat, StrictInt] = Field(default=..., alias="opponentScore")
    drive_id: StrictStr = Field(default=..., alias="driveId")
    play_id: StrictStr = Field(default=..., alias="playId")
    period: Union[StrictFloat, StrictInt] = Field(...)
    clock: PlayStatClock = Field(...)
    yards_to_goal: Union[StrictFloat, StrictInt] = Field(default=..., alias="yardsToGoal")
    down: Union[StrictFloat, StrictInt] = Field(...)
    distance: Union[StrictFloat, StrictInt] = Field(...)
    athlete_id: StrictStr = Field(default=..., alias="athleteId")
    athlete_name: StrictStr = Field(default=..., alias="athleteName")
    stat_type: StrictStr = Field(default=..., alias="statType")
    stat: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["gameId", "season", "week", "team", "conference", "opponent", "teamScore", "opponentScore", "driveId", "playId", "period", "clock", "yardsToGoal", "down", "distance", "athleteId", "athleteName", "statType", "stat"]

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
    def from_json(cls, json_str: str) -> PlayStat:
        """Create an instance of PlayStat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of clock
        if self.clock:
            _dict['clock'] = self.clock.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayStat:
        """Create an instance of PlayStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayStat.parse_obj(obj)

        _obj = PlayStat.parse_obj({
            "game_id": obj.get("gameId"),
            "season": obj.get("season"),
            "week": obj.get("week"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "opponent": obj.get("opponent"),
            "team_score": obj.get("teamScore"),
            "opponent_score": obj.get("opponentScore"),
            "drive_id": obj.get("driveId"),
            "play_id": obj.get("playId"),
            "period": obj.get("period"),
            "clock": PlayStatClock.from_dict(obj.get("clock")) if obj.get("clock") is not None else None,
            "yards_to_goal": obj.get("yardsToGoal"),
            "down": obj.get("down"),
            "distance": obj.get("distance"),
            "athlete_id": obj.get("athleteId"),
            "athlete_name": obj.get("athleteName"),
            "stat_type": obj.get("statType"),
            "stat": obj.get("stat")
        })
        return _obj


