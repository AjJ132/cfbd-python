# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.2
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class TeamEloRating(object):
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
        'elo': 'float'
    }

    attribute_map = {
        'year': 'year',
        'team': 'team',
        'conference': 'conference',
        'elo': 'elo'
    }

    def __init__(self, year=None, team=None, conference=None, elo=None, _configuration=None):  # noqa: E501
        """TeamEloRating - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._year = None
        self._team = None
        self._conference = None
        self._elo = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if elo is not None:
            self.elo = elo

    @property
    def year(self):
        """Gets the year of this TeamEloRating.  # noqa: E501


        :return: The year of this TeamEloRating.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamEloRating.


        :param year: The year of this TeamEloRating.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def team(self):
        """Gets the team of this TeamEloRating.  # noqa: E501


        :return: The team of this TeamEloRating.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamEloRating.


        :param team: The team of this TeamEloRating.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this TeamEloRating.  # noqa: E501


        :return: The conference of this TeamEloRating.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this TeamEloRating.


        :param conference: The conference of this TeamEloRating.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def elo(self):
        """Gets the elo of this TeamEloRating.  # noqa: E501


        :return: The elo of this TeamEloRating.  # noqa: E501
        :rtype: float
        """
        return self._elo

    @elo.setter
    def elo(self, elo):
        """Sets the elo of this TeamEloRating.


        :param elo: The elo of this TeamEloRating.  # noqa: E501
        :type: float
        """

        self._elo = elo

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
        if issubclass(TeamEloRating, dict):
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
        if not isinstance(other, TeamEloRating):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamEloRating):
            return True

        return self.to_dict() != other.to_dict()
