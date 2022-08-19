# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.1
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class TeamSPRating(object):
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
        'year': 'int',
        'team': 'str',
        'conference': 'str',
        'rating': 'float',
        'ranking': 'float',
        'second_order_wins': 'float',
        'sos': 'float',
        'offense': 'object',
        'defense': 'object',
        'special_teams': 'object'
    }

    attribute_map = {
        'year': 'year',
        'team': 'team',
        'conference': 'conference',
        'rating': 'rating',
        'ranking': 'ranking',
        'second_order_wins': 'secondOrderWins',
        'sos': 'sos',
        'offense': 'offense',
        'defense': 'defense',
        'special_teams': 'specialTeams'
    }

    def __init__(self, year=None, team=None, conference=None, rating=None, ranking=None, second_order_wins=None, sos=None, offense=None, defense=None, special_teams=None, _configuration=None):  # noqa: E501
        """TeamSPRating - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._year = None
        self._team = None
        self._conference = None
        self._rating = None
        self._ranking = None
        self._second_order_wins = None
        self._sos = None
        self._offense = None
        self._defense = None
        self._special_teams = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if rating is not None:
            self.rating = rating
        if ranking is not None:
            self.ranking = ranking
        if second_order_wins is not None:
            self.second_order_wins = second_order_wins
        if sos is not None:
            self.sos = sos
        if offense is not None:
            self.offense = offense
        if defense is not None:
            self.defense = defense
        if special_teams is not None:
            self.special_teams = special_teams

    @property
    def year(self):
        """Gets the year of this TeamSPRating.  # noqa: E501


        :return: The year of this TeamSPRating.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamSPRating.


        :param year: The year of this TeamSPRating.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def team(self):
        """Gets the team of this TeamSPRating.  # noqa: E501


        :return: The team of this TeamSPRating.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamSPRating.


        :param team: The team of this TeamSPRating.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this TeamSPRating.  # noqa: E501


        :return: The conference of this TeamSPRating.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this TeamSPRating.


        :param conference: The conference of this TeamSPRating.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def rating(self):
        """Gets the rating of this TeamSPRating.  # noqa: E501


        :return: The rating of this TeamSPRating.  # noqa: E501
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this TeamSPRating.


        :param rating: The rating of this TeamSPRating.  # noqa: E501
        :type: float
        """

        self._rating = rating

    @property
    def ranking(self):
        """Gets the ranking of this TeamSPRating.  # noqa: E501


        :return: The ranking of this TeamSPRating.  # noqa: E501
        :rtype: float
        """
        return self._ranking

    @ranking.setter
    def ranking(self, ranking):
        """Sets the ranking of this TeamSPRating.


        :param ranking: The ranking of this TeamSPRating.  # noqa: E501
        :type: float
        """

        self._ranking = ranking

    @property
    def second_order_wins(self):
        """Gets the second_order_wins of this TeamSPRating.  # noqa: E501


        :return: The second_order_wins of this TeamSPRating.  # noqa: E501
        :rtype: float
        """
        return self._second_order_wins

    @second_order_wins.setter
    def second_order_wins(self, second_order_wins):
        """Sets the second_order_wins of this TeamSPRating.


        :param second_order_wins: The second_order_wins of this TeamSPRating.  # noqa: E501
        :type: float
        """

        self._second_order_wins = second_order_wins

    @property
    def sos(self):
        """Gets the sos of this TeamSPRating.  # noqa: E501


        :return: The sos of this TeamSPRating.  # noqa: E501
        :rtype: float
        """
        return self._sos

    @sos.setter
    def sos(self, sos):
        """Sets the sos of this TeamSPRating.


        :param sos: The sos of this TeamSPRating.  # noqa: E501
        :type: float
        """

        self._sos = sos

    @property
    def offense(self):
        """Gets the offense of this TeamSPRating.  # noqa: E501


        :return: The offense of this TeamSPRating.  # noqa: E501
        :rtype: object
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this TeamSPRating.


        :param offense: The offense of this TeamSPRating.  # noqa: E501
        :type: object
        """

        self._offense = offense

    @property
    def defense(self):
        """Gets the defense of this TeamSPRating.  # noqa: E501


        :return: The defense of this TeamSPRating.  # noqa: E501
        :rtype: object
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this TeamSPRating.


        :param defense: The defense of this TeamSPRating.  # noqa: E501
        :type: object
        """

        self._defense = defense

    @property
    def special_teams(self):
        """Gets the special_teams of this TeamSPRating.  # noqa: E501


        :return: The special_teams of this TeamSPRating.  # noqa: E501
        :rtype: object
        """
        return self._special_teams

    @special_teams.setter
    def special_teams(self, special_teams):
        """Sets the special_teams of this TeamSPRating.


        :param special_teams: The special_teams of this TeamSPRating.  # noqa: E501
        :type: object
        """

        self._special_teams = special_teams

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
        if issubclass(TeamSPRating, dict):
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
        if not isinstance(other, TeamSPRating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamSPRating):
            return True

        return self.to_dict() != other.to_dict()
