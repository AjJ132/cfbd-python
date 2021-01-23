# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TeamRecruitingRank(object):
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
        'rank': 'int',
        'team': 'str',
        'points': 'float'
    }

    attribute_map = {
        'year': 'year',
        'rank': 'rank',
        'team': 'team',
        'points': 'points'
    }

    def __init__(self, year=None, rank=None, team=None, points=None):  # noqa: E501
        """TeamRecruitingRank - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._rank = None
        self._team = None
        self._points = None
        self.discriminator = None

        if year is not None:
            self.year = year
        if rank is not None:
            self.rank = rank
        if team is not None:
            self.team = team
        if points is not None:
            self.points = points

    @property
    def year(self):
        """Gets the year of this TeamRecruitingRank.  # noqa: E501


        :return: The year of this TeamRecruitingRank.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamRecruitingRank.


        :param year: The year of this TeamRecruitingRank.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def rank(self):
        """Gets the rank of this TeamRecruitingRank.  # noqa: E501


        :return: The rank of this TeamRecruitingRank.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this TeamRecruitingRank.


        :param rank: The rank of this TeamRecruitingRank.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def team(self):
        """Gets the team of this TeamRecruitingRank.  # noqa: E501


        :return: The team of this TeamRecruitingRank.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamRecruitingRank.


        :param team: The team of this TeamRecruitingRank.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def points(self):
        """Gets the points of this TeamRecruitingRank.  # noqa: E501


        :return: The points of this TeamRecruitingRank.  # noqa: E501
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this TeamRecruitingRank.


        :param points: The points of this TeamRecruitingRank.  # noqa: E501
        :type: float
        """

        self._points = points

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
        if issubclass(TeamRecruitingRank, dict):
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
        if not isinstance(other, TeamRecruitingRank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
