# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 3.4.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class Week(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'season': 'int',
        'week': 'int',
        'season_type': 'str',
        'first_game_start': 'str',
        'last_game_start': 'str'
    }

    attribute_map = {
        'season': 'season',
        'week': 'week',
        'season_type': 'seasonType',
        'first_game_start': 'firstGameStart',
        'last_game_start': 'lastGameStart'
    }

    def __init__(self, season=None, week=None, season_type=None, first_game_start=None, last_game_start=None, _configuration=None):  # noqa: E501
        """Week - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._season = None
        self._week = None
        self._season_type = None
        self._first_game_start = None
        self._last_game_start = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if season_type is not None:
            self.season_type = season_type
        if first_game_start is not None:
            self.first_game_start = first_game_start
        if last_game_start is not None:
            self.last_game_start = last_game_start

    @property
    def season(self):
        """Gets the season of this Week.  # noqa: E501


        :return: The season of this Week.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Week.


        :param season: The season of this Week.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this Week.  # noqa: E501


        :return: The week of this Week.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this Week.


        :param week: The week of this Week.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def season_type(self):
        """Gets the season_type of this Week.  # noqa: E501


        :return: The season_type of this Week.  # noqa: E501
        :rtype: str
        """
        return self._season_type

    @season_type.setter
    def season_type(self, season_type):
        """Sets the season_type of this Week.


        :param season_type: The season_type of this Week.  # noqa: E501
        :type: str
        """

        self._season_type = season_type

    @property
    def first_game_start(self):
        """Gets the first_game_start of this Week.  # noqa: E501


        :return: The first_game_start of this Week.  # noqa: E501
        :rtype: str
        """
        return self._first_game_start

    @first_game_start.setter
    def first_game_start(self, first_game_start):
        """Sets the first_game_start of this Week.


        :param first_game_start: The first_game_start of this Week.  # noqa: E501
        :type: str
        """

        self._first_game_start = first_game_start

    @property
    def last_game_start(self):
        """Gets the last_game_start of this Week.  # noqa: E501


        :return: The last_game_start of this Week.  # noqa: E501
        :rtype: str
        """
        return self._last_game_start

    @last_game_start.setter
    def last_game_start(self, last_game_start):
        """Sets the last_game_start of this Week.


        :param last_game_start: The last_game_start of this Week.  # noqa: E501
        :type: str
        """

        self._last_game_start = last_game_start

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Week, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Week):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Week):
            return True

        return self.to_dict() != other.to_dict()
