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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from cfbd.models.division_classification import DivisionClassification
from cfbd.models.season_type import SeasonType

class Game(BaseModel):
    """
    Game
    """
    id: StrictInt = Field(...)
    season: StrictInt = Field(...)
    week: StrictInt = Field(...)
    season_type: SeasonType = Field(default=..., alias="seasonType")
    start_date: datetime = Field(default=..., alias="startDate")
    start_time_tbd: StrictBool = Field(default=..., alias="startTimeTBD")
    completed: StrictBool = Field(...)
    neutral_site: StrictBool = Field(default=..., alias="neutralSite")
    conference_game: StrictBool = Field(default=..., alias="conferenceGame")
    attendance: Optional[StrictInt] = Field(...)
    venue_id: Optional[StrictInt] = Field(default=..., alias="venueId")
    venue: Optional[StrictStr] = Field(...)
    home_id: StrictInt = Field(default=..., alias="homeId")
    home_team: StrictStr = Field(default=..., alias="homeTeam")
    home_conference: Optional[StrictStr] = Field(default=..., alias="homeConference")
    home_classification: Optional[DivisionClassification] = Field(default=..., alias="homeClassification")
    home_points: Optional[StrictInt] = Field(default=..., alias="homePoints")
    home_line_scores: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(default=..., alias="homeLineScores")
    home_postgame_win_probability: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="homePostgameWinProbability")
    home_pregame_elo: Optional[StrictInt] = Field(default=..., alias="homePregameElo")
    home_postgame_elo: Optional[StrictInt] = Field(default=..., alias="homePostgameElo")
    away_id: StrictInt = Field(default=..., alias="awayId")
    away_team: StrictStr = Field(default=..., alias="awayTeam")
    away_conference: Optional[StrictStr] = Field(default=..., alias="awayConference")
    away_classification: Optional[DivisionClassification] = Field(default=..., alias="awayClassification")
    away_points: Optional[StrictInt] = Field(default=..., alias="awayPoints")
    away_line_scores: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(default=..., alias="awayLineScores")
    away_postgame_win_probability: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="awayPostgameWinProbability")
    away_pregame_elo: Optional[StrictInt] = Field(default=..., alias="awayPregameElo")
    away_postgame_elo: Optional[StrictInt] = Field(default=..., alias="awayPostgameElo")
    excitement_index: Optional[Union[StrictFloat, StrictInt]] = Field(default=..., alias="excitementIndex")
    highlights: Optional[StrictStr] = Field(...)
    notes: Optional[StrictStr] = Field(...)
    __properties = ["id", "season", "week", "seasonType", "startDate", "startTimeTBD", "completed", "neutralSite", "conferenceGame", "attendance", "venueId", "venue", "homeId", "homeTeam", "homeConference", "homeClassification", "homePoints", "homeLineScores", "homePostgameWinProbability", "homePregameElo", "homePostgameElo", "awayId", "awayTeam", "awayConference", "awayClassification", "awayPoints", "awayLineScores", "awayPostgameWinProbability", "awayPregameElo", "awayPostgameElo", "excitementIndex", "highlights", "notes"]

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
    def from_json(cls, json_str: str) -> Game:
        """Create an instance of Game from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if attendance (nullable) is None
        # and __fields_set__ contains the field
        if self.attendance is None and "attendance" in self.__fields_set__:
            _dict['attendance'] = None

        # set to None if venue_id (nullable) is None
        # and __fields_set__ contains the field
        if self.venue_id is None and "venue_id" in self.__fields_set__:
            _dict['venueId'] = None

        # set to None if venue (nullable) is None
        # and __fields_set__ contains the field
        if self.venue is None and "venue" in self.__fields_set__:
            _dict['venue'] = None

        # set to None if home_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.home_conference is None and "home_conference" in self.__fields_set__:
            _dict['homeConference'] = None

        # set to None if home_classification (nullable) is None
        # and __fields_set__ contains the field
        if self.home_classification is None and "home_classification" in self.__fields_set__:
            _dict['homeClassification'] = None

        # set to None if home_points (nullable) is None
        # and __fields_set__ contains the field
        if self.home_points is None and "home_points" in self.__fields_set__:
            _dict['homePoints'] = None

        # set to None if home_line_scores (nullable) is None
        # and __fields_set__ contains the field
        if self.home_line_scores is None and "home_line_scores" in self.__fields_set__:
            _dict['homeLineScores'] = None

        # set to None if home_postgame_win_probability (nullable) is None
        # and __fields_set__ contains the field
        if self.home_postgame_win_probability is None and "home_postgame_win_probability" in self.__fields_set__:
            _dict['homePostgameWinProbability'] = None

        # set to None if home_pregame_elo (nullable) is None
        # and __fields_set__ contains the field
        if self.home_pregame_elo is None and "home_pregame_elo" in self.__fields_set__:
            _dict['homePregameElo'] = None

        # set to None if home_postgame_elo (nullable) is None
        # and __fields_set__ contains the field
        if self.home_postgame_elo is None and "home_postgame_elo" in self.__fields_set__:
            _dict['homePostgameElo'] = None

        # set to None if away_conference (nullable) is None
        # and __fields_set__ contains the field
        if self.away_conference is None and "away_conference" in self.__fields_set__:
            _dict['awayConference'] = None

        # set to None if away_classification (nullable) is None
        # and __fields_set__ contains the field
        if self.away_classification is None and "away_classification" in self.__fields_set__:
            _dict['awayClassification'] = None

        # set to None if away_points (nullable) is None
        # and __fields_set__ contains the field
        if self.away_points is None and "away_points" in self.__fields_set__:
            _dict['awayPoints'] = None

        # set to None if away_line_scores (nullable) is None
        # and __fields_set__ contains the field
        if self.away_line_scores is None and "away_line_scores" in self.__fields_set__:
            _dict['awayLineScores'] = None

        # set to None if away_postgame_win_probability (nullable) is None
        # and __fields_set__ contains the field
        if self.away_postgame_win_probability is None and "away_postgame_win_probability" in self.__fields_set__:
            _dict['awayPostgameWinProbability'] = None

        # set to None if away_pregame_elo (nullable) is None
        # and __fields_set__ contains the field
        if self.away_pregame_elo is None and "away_pregame_elo" in self.__fields_set__:
            _dict['awayPregameElo'] = None

        # set to None if away_postgame_elo (nullable) is None
        # and __fields_set__ contains the field
        if self.away_postgame_elo is None and "away_postgame_elo" in self.__fields_set__:
            _dict['awayPostgameElo'] = None

        # set to None if excitement_index (nullable) is None
        # and __fields_set__ contains the field
        if self.excitement_index is None and "excitement_index" in self.__fields_set__:
            _dict['excitementIndex'] = None

        # set to None if highlights (nullable) is None
        # and __fields_set__ contains the field
        if self.highlights is None and "highlights" in self.__fields_set__:
            _dict['highlights'] = None

        # set to None if notes (nullable) is None
        # and __fields_set__ contains the field
        if self.notes is None and "notes" in self.__fields_set__:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Game:
        """Create an instance of Game from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Game.parse_obj(obj)

        _obj = Game.parse_obj({
            "id": obj.get("id"),
            "season": obj.get("season"),
            "week": obj.get("week"),
            "season_type": obj.get("seasonType"),
            "start_date": obj.get("startDate"),
            "start_time_tbd": obj.get("startTimeTBD"),
            "completed": obj.get("completed"),
            "neutral_site": obj.get("neutralSite"),
            "conference_game": obj.get("conferenceGame"),
            "attendance": obj.get("attendance"),
            "venue_id": obj.get("venueId"),
            "venue": obj.get("venue"),
            "home_id": obj.get("homeId"),
            "home_team": obj.get("homeTeam"),
            "home_conference": obj.get("homeConference"),
            "home_classification": obj.get("homeClassification"),
            "home_points": obj.get("homePoints"),
            "home_line_scores": obj.get("homeLineScores"),
            "home_postgame_win_probability": obj.get("homePostgameWinProbability"),
            "home_pregame_elo": obj.get("homePregameElo"),
            "home_postgame_elo": obj.get("homePostgameElo"),
            "away_id": obj.get("awayId"),
            "away_team": obj.get("awayTeam"),
            "away_conference": obj.get("awayConference"),
            "away_classification": obj.get("awayClassification"),
            "away_points": obj.get("awayPoints"),
            "away_line_scores": obj.get("awayLineScores"),
            "away_postgame_win_probability": obj.get("awayPostgameWinProbability"),
            "away_pregame_elo": obj.get("awayPregameElo"),
            "away_postgame_elo": obj.get("awayPostgameElo"),
            "excitement_index": obj.get("excitementIndex"),
            "highlights": obj.get("highlights"),
            "notes": obj.get("notes")
        })
        return _obj


