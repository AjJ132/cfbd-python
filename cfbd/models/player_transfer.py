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

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from cfbd.models.transfer_eligibility import TransferEligibility

class PlayerTransfer(BaseModel):
    """
    PlayerTransfer
    """
    season: StrictInt = Field(...)
    first_name: StrictStr = Field(default=..., alias="firstName")
    last_name: StrictStr = Field(default=..., alias="lastName")
    position: StrictStr = Field(...)
    origin: StrictStr = Field(...)
    destination: Optional[StrictStr] = Field(...)
    transfer_date: Optional[datetime] = Field(default=..., alias="transferDate")
    rating: Optional[Union[StrictFloat, StrictInt]] = Field(...)
    stars: Optional[StrictInt] = Field(...)
    eligibility: Optional[TransferEligibility] = Field(...)
    __properties = ["season", "firstName", "lastName", "position", "origin", "destination", "transferDate", "rating", "stars", "eligibility"]

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
    def from_json(cls, json_str: str) -> PlayerTransfer:
        """Create an instance of PlayerTransfer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if destination (nullable) is None
        # and __fields_set__ contains the field
        if self.destination is None and "destination" in self.__fields_set__:
            _dict['destination'] = None

        # set to None if transfer_date (nullable) is None
        # and __fields_set__ contains the field
        if self.transfer_date is None and "transfer_date" in self.__fields_set__:
            _dict['transferDate'] = None

        # set to None if rating (nullable) is None
        # and __fields_set__ contains the field
        if self.rating is None and "rating" in self.__fields_set__:
            _dict['rating'] = None

        # set to None if stars (nullable) is None
        # and __fields_set__ contains the field
        if self.stars is None and "stars" in self.__fields_set__:
            _dict['stars'] = None

        # set to None if eligibility (nullable) is None
        # and __fields_set__ contains the field
        if self.eligibility is None and "eligibility" in self.__fields_set__:
            _dict['eligibility'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlayerTransfer:
        """Create an instance of PlayerTransfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlayerTransfer.parse_obj(obj)

        _obj = PlayerTransfer.parse_obj({
            "season": obj.get("season"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "position": obj.get("position"),
            "origin": obj.get("origin"),
            "destination": obj.get("destination"),
            "transfer_date": obj.get("transferDate"),
            "rating": obj.get("rating"),
            "stars": obj.get("stars"),
            "eligibility": obj.get("eligibility")
        })
        return _obj


