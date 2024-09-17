# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.1.2
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, conlist
from cfbd.models.team_explosiveness import TeamExplosiveness
from cfbd.models.team_field_position import TeamFieldPosition
from cfbd.models.team_havoc import TeamHavoc
from cfbd.models.team_ppa import TeamPPA
from cfbd.models.team_rushing_stats import TeamRushingStats
from cfbd.models.team_scoring_opportunities import TeamScoringOpportunities
from cfbd.models.team_success_rates import TeamSuccessRates

class AdvancedBoxScoreTeams(BaseModel):
    """
    AdvancedBoxScoreTeams
    """
    field_position: conlist(TeamFieldPosition) = Field(default=..., alias="fieldPosition")
    scoring_opportunities: conlist(TeamScoringOpportunities) = Field(default=..., alias="scoringOpportunities")
    havoc: conlist(TeamHavoc) = Field(...)
    rushing: conlist(TeamRushingStats) = Field(...)
    explosiveness: conlist(TeamExplosiveness) = Field(...)
    success_rates: conlist(TeamSuccessRates) = Field(default=..., alias="successRates")
    cumulative_ppa: conlist(TeamPPA) = Field(default=..., alias="cumulativePpa")
    ppa: conlist(TeamPPA) = Field(...)
    __properties = ["fieldPosition", "scoringOpportunities", "havoc", "rushing", "explosiveness", "successRates", "cumulativePpa", "ppa"]

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
    def from_json(cls, json_str: str) -> AdvancedBoxScoreTeams:
        """Create an instance of AdvancedBoxScoreTeams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in field_position (list)
        _items = []
        if self.field_position:
            for _item in self.field_position:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fieldPosition'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in scoring_opportunities (list)
        _items = []
        if self.scoring_opportunities:
            for _item in self.scoring_opportunities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scoringOpportunities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in havoc (list)
        _items = []
        if self.havoc:
            for _item in self.havoc:
                if _item:
                    _items.append(_item.to_dict())
            _dict['havoc'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rushing (list)
        _items = []
        if self.rushing:
            for _item in self.rushing:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rushing'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in explosiveness (list)
        _items = []
        if self.explosiveness:
            for _item in self.explosiveness:
                if _item:
                    _items.append(_item.to_dict())
            _dict['explosiveness'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in success_rates (list)
        _items = []
        if self.success_rates:
            for _item in self.success_rates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['successRates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cumulative_ppa (list)
        _items = []
        if self.cumulative_ppa:
            for _item in self.cumulative_ppa:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cumulativePpa'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ppa (list)
        _items = []
        if self.ppa:
            for _item in self.ppa:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ppa'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdvancedBoxScoreTeams:
        """Create an instance of AdvancedBoxScoreTeams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdvancedBoxScoreTeams.parse_obj(obj)

        _obj = AdvancedBoxScoreTeams.parse_obj({
            "field_position": [TeamFieldPosition.from_dict(_item) for _item in obj.get("fieldPosition")] if obj.get("fieldPosition") is not None else None,
            "scoring_opportunities": [TeamScoringOpportunities.from_dict(_item) for _item in obj.get("scoringOpportunities")] if obj.get("scoringOpportunities") is not None else None,
            "havoc": [TeamHavoc.from_dict(_item) for _item in obj.get("havoc")] if obj.get("havoc") is not None else None,
            "rushing": [TeamRushingStats.from_dict(_item) for _item in obj.get("rushing")] if obj.get("rushing") is not None else None,
            "explosiveness": [TeamExplosiveness.from_dict(_item) for _item in obj.get("explosiveness")] if obj.get("explosiveness") is not None else None,
            "success_rates": [TeamSuccessRates.from_dict(_item) for _item in obj.get("successRates")] if obj.get("successRates") is not None else None,
            "cumulative_ppa": [TeamPPA.from_dict(_item) for _item in obj.get("cumulativePpa")] if obj.get("cumulativePpa") is not None else None,
            "ppa": [TeamPPA.from_dict(_item) for _item in obj.get("ppa")] if obj.get("ppa") is not None else None
        })
        return _obj


