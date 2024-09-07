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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from cfbd.models.division_classification import DivisionClassification

class Conference(BaseModel):
    """
    Conference
    """
    id: StrictInt = Field(...)
    name: StrictStr = Field(...)
    short_name: Optional[StrictStr] = Field(default=..., alias="shortName")
    abbreviation: Optional[StrictStr] = Field(...)
    classification: Optional[DivisionClassification] = Field(...)
    __properties = ["id", "name", "shortName", "abbreviation", "classification"]

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
    def from_json(cls, json_str: str) -> Conference:
        """Create an instance of Conference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if short_name (nullable) is None
        # and __fields_set__ contains the field
        if self.short_name is None and "short_name" in self.__fields_set__:
            _dict['shortName'] = None

        # set to None if abbreviation (nullable) is None
        # and __fields_set__ contains the field
        if self.abbreviation is None and "abbreviation" in self.__fields_set__:
            _dict['abbreviation'] = None

        # set to None if classification (nullable) is None
        # and __fields_set__ contains the field
        if self.classification is None and "classification" in self.__fields_set__:
            _dict['classification'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Conference:
        """Create an instance of Conference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Conference.parse_obj(obj)

        _obj = Conference.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "short_name": obj.get("shortName"),
            "abbreviation": obj.get("abbreviation"),
            "classification": obj.get("classification")
        })
        return _obj


