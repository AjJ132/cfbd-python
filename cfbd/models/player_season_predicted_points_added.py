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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.player_season_predicted_points_added_average_ppa import PlayerSeasonPredictedPointsAddedAveragePPA

class PlayerSeasonPredictedPointsAdded(BaseModel):
    """
    PlayerSeasonPredictedPointsAdded
    """
    season: StrictInt = Field(...)
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    position: StrictStr = Field(...)
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    average_ppa: PlayerSeasonPredictedPointsAddedAveragePPA = Field(default=..., alias="averagePPA")
    total_ppa: PlayerSeasonPredictedPointsAddedAveragePPA = Field(default=..., alias="totalPPA")
    __properties = ["season", "id", "name", "position", "team", "conference", "averagePPA", "totalPPA"]

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
    def from_json(cls, json_str: str) -> PlayerSeasonPredictedPointsAdded:
        """Create an instance of PlayerSeasonPredictedPointsAdded from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of average_ppa
        if self.average_ppa:
            _dict['averagePPA'] = self.average_ppa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_ppa
        if self.total_ppa:
            _dict['totalPPA'] = self.total_ppa.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerSeasonPredictedPointsAdded:
        """Create an instance of PlayerSeasonPredictedPointsAdded from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerSeasonPredictedPointsAdded.parse_obj(obj)

        _obj = PlayerSeasonPredictedPointsAdded.parse_obj({
            "season": obj.get("season"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "position": obj.get("position"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "average_ppa": PlayerSeasonPredictedPointsAddedAveragePPA.from_dict(obj.get("averagePPA")) if obj.get("averagePPA") is not None else None,
            "total_ppa": PlayerSeasonPredictedPointsAddedAveragePPA.from_dict(obj.get("totalPPA")) if obj.get("totalPPA") is not None else None
        })
        return _obj


