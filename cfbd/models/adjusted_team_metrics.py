# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.3.0
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
from cfbd.models.adjusted_team_metrics_epa import AdjustedTeamMetricsEpa
from cfbd.models.adjusted_team_metrics_rushing import AdjustedTeamMetricsRushing
from cfbd.models.adjusted_team_metrics_success_rate import AdjustedTeamMetricsSuccessRate

class AdjustedTeamMetrics(BaseModel):
    """
    AdjustedTeamMetrics
    """
    year: StrictInt = Field(...)
    team_id: StrictInt = Field(default=..., alias="teamId")
    team: StrictStr = Field(...)
    conference: StrictStr = Field(...)
    epa: AdjustedTeamMetricsEpa = Field(...)
    epa_allowed: AdjustedTeamMetricsEpa = Field(default=..., alias="epaAllowed")
    success_rate: AdjustedTeamMetricsSuccessRate = Field(default=..., alias="successRate")
    success_rate_allowed: AdjustedTeamMetricsSuccessRate = Field(default=..., alias="successRateAllowed")
    rushing: AdjustedTeamMetricsRushing = Field(...)
    rushing_allowed: AdjustedTeamMetricsRushing = Field(default=..., alias="rushingAllowed")
    explosiveness: Union[StrictFloat, StrictInt] = Field(...)
    explosiveness_allowed: Union[StrictFloat, StrictInt] = Field(default=..., alias="explosivenessAllowed")
    __properties = ["year", "teamId", "team", "conference", "epa", "epaAllowed", "successRate", "successRateAllowed", "rushing", "rushingAllowed", "explosiveness", "explosivenessAllowed"]

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
    def from_json(cls, json_str: str) -> AdjustedTeamMetrics:
        """Create an instance of AdjustedTeamMetrics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of epa
        if self.epa:
            _dict['epa'] = self.epa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of epa_allowed
        if self.epa_allowed:
            _dict['epaAllowed'] = self.epa_allowed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of success_rate
        if self.success_rate:
            _dict['successRate'] = self.success_rate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of success_rate_allowed
        if self.success_rate_allowed:
            _dict['successRateAllowed'] = self.success_rate_allowed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rushing
        if self.rushing:
            _dict['rushing'] = self.rushing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rushing_allowed
        if self.rushing_allowed:
            _dict['rushingAllowed'] = self.rushing_allowed.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdjustedTeamMetrics:
        """Create an instance of AdjustedTeamMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdjustedTeamMetrics.parse_obj(obj)

        _obj = AdjustedTeamMetrics.parse_obj({
            "year": obj.get("year"),
            "team_id": obj.get("teamId"),
            "team": obj.get("team"),
            "conference": obj.get("conference"),
            "epa": AdjustedTeamMetricsEpa.from_dict(obj.get("epa")) if obj.get("epa") is not None else None,
            "epa_allowed": AdjustedTeamMetricsEpa.from_dict(obj.get("epaAllowed")) if obj.get("epaAllowed") is not None else None,
            "success_rate": AdjustedTeamMetricsSuccessRate.from_dict(obj.get("successRate")) if obj.get("successRate") is not None else None,
            "success_rate_allowed": AdjustedTeamMetricsSuccessRate.from_dict(obj.get("successRateAllowed")) if obj.get("successRateAllowed") is not None else None,
            "rushing": AdjustedTeamMetricsRushing.from_dict(obj.get("rushing")) if obj.get("rushing") is not None else None,
            "rushing_allowed": AdjustedTeamMetricsRushing.from_dict(obj.get("rushingAllowed")) if obj.get("rushingAllowed") is not None else None,
            "explosiveness": obj.get("explosiveness"),
            "explosiveness_allowed": obj.get("explosivenessAllowed")
        })
        return _obj


