# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class TeamMatchup(object):
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
        'team1': 'str',
        'team2': 'str',
        'start_year': 'int',
        'end_year': 'int',
        'team1_wins': 'int',
        'team2_wins': 'int',
        'ties': 'int',
        'games': 'list[TeamMatchupGames]'
    }

    attribute_map = {
        'team1': 'team1',
        'team2': 'team2',
        'start_year': 'startYear',
        'end_year': 'endYear',
        'team1_wins': 'team1Wins',
        'team2_wins': 'team2Wins',
        'ties': 'ties',
        'games': 'games'
    }

    def __init__(self, team1=None, team2=None, start_year=None, end_year=None, team1_wins=None, team2_wins=None, ties=None, games=None, _configuration=None):  # noqa: E501
        """TeamMatchup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team1 = None
        self._team2 = None
        self._start_year = None
        self._end_year = None
        self._team1_wins = None
        self._team2_wins = None
        self._ties = None
        self._games = None
        self.discriminator = None

        if team1 is not None:
            self.team1 = team1
        if team2 is not None:
            self.team2 = team2
        if start_year is not None:
            self.start_year = start_year
        if end_year is not None:
            self.end_year = end_year
        if team1_wins is not None:
            self.team1_wins = team1_wins
        if team2_wins is not None:
            self.team2_wins = team2_wins
        if ties is not None:
            self.ties = ties
        if games is not None:
            self.games = games

    @property
    def team1(self):
        """Gets the team1 of this TeamMatchup.  # noqa: E501


        :return: The team1 of this TeamMatchup.  # noqa: E501
        :rtype: str
        """
        return self._team1

    @team1.setter
    def team1(self, team1):
        """Sets the team1 of this TeamMatchup.


        :param team1: The team1 of this TeamMatchup.  # noqa: E501
        :type: str
        """

        self._team1 = team1

    @property
    def team2(self):
        """Gets the team2 of this TeamMatchup.  # noqa: E501


        :return: The team2 of this TeamMatchup.  # noqa: E501
        :rtype: str
        """
        return self._team2

    @team2.setter
    def team2(self, team2):
        """Sets the team2 of this TeamMatchup.


        :param team2: The team2 of this TeamMatchup.  # noqa: E501
        :type: str
        """

        self._team2 = team2

    @property
    def start_year(self):
        """Gets the start_year of this TeamMatchup.  # noqa: E501


        :return: The start_year of this TeamMatchup.  # noqa: E501
        :rtype: int
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """Sets the start_year of this TeamMatchup.


        :param start_year: The start_year of this TeamMatchup.  # noqa: E501
        :type: int
        """

        self._start_year = start_year

    @property
    def end_year(self):
        """Gets the end_year of this TeamMatchup.  # noqa: E501


        :return: The end_year of this TeamMatchup.  # noqa: E501
        :rtype: int
        """
        return self._end_year

    @end_year.setter
    def end_year(self, end_year):
        """Sets the end_year of this TeamMatchup.


        :param end_year: The end_year of this TeamMatchup.  # noqa: E501
        :type: int
        """

        self._end_year = end_year

    @property
    def team1_wins(self):
        """Gets the team1_wins of this TeamMatchup.  # noqa: E501


        :return: The team1_wins of this TeamMatchup.  # noqa: E501
        :rtype: int
        """
        return self._team1_wins

    @team1_wins.setter
    def team1_wins(self, team1_wins):
        """Sets the team1_wins of this TeamMatchup.


        :param team1_wins: The team1_wins of this TeamMatchup.  # noqa: E501
        :type: int
        """

        self._team1_wins = team1_wins

    @property
    def team2_wins(self):
        """Gets the team2_wins of this TeamMatchup.  # noqa: E501


        :return: The team2_wins of this TeamMatchup.  # noqa: E501
        :rtype: int
        """
        return self._team2_wins

    @team2_wins.setter
    def team2_wins(self, team2_wins):
        """Sets the team2_wins of this TeamMatchup.


        :param team2_wins: The team2_wins of this TeamMatchup.  # noqa: E501
        :type: int
        """

        self._team2_wins = team2_wins

    @property
    def ties(self):
        """Gets the ties of this TeamMatchup.  # noqa: E501


        :return: The ties of this TeamMatchup.  # noqa: E501
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """Sets the ties of this TeamMatchup.


        :param ties: The ties of this TeamMatchup.  # noqa: E501
        :type: int
        """

        self._ties = ties

    @property
    def games(self):
        """Gets the games of this TeamMatchup.  # noqa: E501


        :return: The games of this TeamMatchup.  # noqa: E501
        :rtype: list[TeamMatchupGames]
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this TeamMatchup.


        :param games: The games of this TeamMatchup.  # noqa: E501
        :type: list[TeamMatchupGames]
        """

        self._games = games

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
        if issubclass(TeamMatchup, dict):
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
        if not isinstance(other, TeamMatchup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamMatchup):
            return True

        return self.to_dict() != other.to_dict()
