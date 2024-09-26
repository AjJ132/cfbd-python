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



from pydantic import BaseModel, Field
from cfbd.models.advanced_box_score_game_info import AdvancedBoxScoreGameInfo
from cfbd.models.advanced_box_score_players import AdvancedBoxScorePlayers
from cfbd.models.advanced_box_score_teams import AdvancedBoxScoreTeams

class AdvancedBoxScore(BaseModel):
    """
    AdvancedBoxScore
    """
    game_info: AdvancedBoxScoreGameInfo = Field(default=..., alias="gameInfo")
    teams: AdvancedBoxScoreTeams = Field(...)
    players: AdvancedBoxScorePlayers = Field(...)
    __properties = ["gameInfo", "teams", "players"]

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
    def from_json(cls, json_str: str) -> AdvancedBoxScore:
        """Create an instance of AdvancedBoxScore from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of game_info
        if self.game_info:
            _dict['gameInfo'] = self.game_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of teams
        if self.teams:
            _dict['teams'] = self.teams.to_dict()
        # override the default output from pydantic by calling `to_dict()` of players
        if self.players:
            _dict['players'] = self.players.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedBoxScore:
        """Create an instance of AdvancedBoxScore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedBoxScore.parse_obj(obj)

        _obj = AdvancedBoxScore.parse_obj({
            "game_info": AdvancedBoxScoreGameInfo.from_dict(obj.get("gameInfo")) if obj.get("gameInfo") is not None else None,
            "teams": AdvancedBoxScoreTeams.from_dict(obj.get("teams")) if obj.get("teams") is not None else None,
            "players": AdvancedBoxScorePlayers.from_dict(obj.get("players")) if obj.get("players") is not None else None
        })
        return _obj


