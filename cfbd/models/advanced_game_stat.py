# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.6
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class AdvancedGameStat(object):
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
        'game_id': 'int',
        'season': 'int',
        'week': 'int',
        'team': 'str',
        'opponent': 'str',
        'offense': 'object',
        'defense': 'object'
    }

    attribute_map = {
        'game_id': 'gameId',
        'season': 'season',
        'week': 'week',
        'team': 'team',
        'opponent': 'opponent',
        'offense': 'offense',
        'defense': 'defense'
    }

    def __init__(self, game_id=None, season=None, week=None, team=None, opponent=None, offense=None, defense=None, _configuration=None):  # noqa: E501
        """AdvancedGameStat - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._game_id = None
        self._season = None
        self._week = None
        self._team = None
        self._opponent = None
        self._offense = None
        self._defense = None
        self.discriminator = None

        if game_id is not None:
            self.game_id = game_id
        if season is not None:
            self.season = season
        if week is not None:
            self.week = week
        if team is not None:
            self.team = team
        if opponent is not None:
            self.opponent = opponent
        if offense is not None:
            self.offense = offense
        if defense is not None:
            self.defense = defense

    @property
    def game_id(self):
        """Gets the game_id of this AdvancedGameStat.  # noqa: E501


        :return: The game_id of this AdvancedGameStat.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this AdvancedGameStat.


        :param game_id: The game_id of this AdvancedGameStat.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def season(self):
        """Gets the season of this AdvancedGameStat.  # noqa: E501


        :return: The season of this AdvancedGameStat.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this AdvancedGameStat.


        :param season: The season of this AdvancedGameStat.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def week(self):
        """Gets the week of this AdvancedGameStat.  # noqa: E501


        :return: The week of this AdvancedGameStat.  # noqa: E501
        :rtype: int
        """
        return self._week

    @week.setter
    def week(self, week):
        """Sets the week of this AdvancedGameStat.


        :param week: The week of this AdvancedGameStat.  # noqa: E501
        :type: int
        """

        self._week = week

    @property
    def team(self):
        """Gets the team of this AdvancedGameStat.  # noqa: E501


        :return: The team of this AdvancedGameStat.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this AdvancedGameStat.


        :param team: The team of this AdvancedGameStat.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def opponent(self):
        """Gets the opponent of this AdvancedGameStat.  # noqa: E501


        :return: The opponent of this AdvancedGameStat.  # noqa: E501
        :rtype: str
        """
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        """Sets the opponent of this AdvancedGameStat.


        :param opponent: The opponent of this AdvancedGameStat.  # noqa: E501
        :type: str
        """

        self._opponent = opponent

    @property
    def offense(self):
        """Gets the offense of this AdvancedGameStat.  # noqa: E501


        :return: The offense of this AdvancedGameStat.  # noqa: E501
        :rtype: object
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this AdvancedGameStat.


        :param offense: The offense of this AdvancedGameStat.  # noqa: E501
        :type: object
        """

        self._offense = offense

    @property
    def defense(self):
        """Gets the defense of this AdvancedGameStat.  # noqa: E501


        :return: The defense of this AdvancedGameStat.  # noqa: E501
        :rtype: object
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this AdvancedGameStat.


        :param defense: The defense of this AdvancedGameStat.  # noqa: E501
        :type: object
        """

        self._defense = defense

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
        if issubclass(AdvancedGameStat, dict):
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
        if not isinstance(other, AdvancedGameStat):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdvancedGameStat):
            return True

        return self.to_dict() != other.to_dict()
