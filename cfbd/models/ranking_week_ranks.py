# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.4
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RankingWeekRanks(object):
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
        'rank': 'int',
        'school': 'str',
        'conference': 'str',
        'first_place_votes': 'int',
        'points': 'int'
    }

    attribute_map = {
        'rank': 'rank',
        'school': 'school',
        'conference': 'conference',
        'first_place_votes': 'firstPlaceVotes',
        'points': 'points'
    }

    def __init__(self, rank=None, school=None, conference=None, first_place_votes=None, points=None):  # noqa: E501
        """RankingWeekRanks - a model defined in Swagger"""  # noqa: E501

        self._rank = None
        self._school = None
        self._conference = None
        self._first_place_votes = None
        self._points = None
        self.discriminator = None

        if rank is not None:
            self.rank = rank
        if school is not None:
            self.school = school
        if conference is not None:
            self.conference = conference
        if first_place_votes is not None:
            self.first_place_votes = first_place_votes
        if points is not None:
            self.points = points

    @property
    def rank(self):
        """Gets the rank of this RankingWeekRanks.  # noqa: E501


        :return: The rank of this RankingWeekRanks.  # noqa: E501
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """Sets the rank of this RankingWeekRanks.


        :param rank: The rank of this RankingWeekRanks.  # noqa: E501
        :type: int
        """

        self._rank = rank

    @property
    def school(self):
        """Gets the school of this RankingWeekRanks.  # noqa: E501


        :return: The school of this RankingWeekRanks.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this RankingWeekRanks.


        :param school: The school of this RankingWeekRanks.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def conference(self):
        """Gets the conference of this RankingWeekRanks.  # noqa: E501


        :return: The conference of this RankingWeekRanks.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this RankingWeekRanks.


        :param conference: The conference of this RankingWeekRanks.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def first_place_votes(self):
        """Gets the first_place_votes of this RankingWeekRanks.  # noqa: E501


        :return: The first_place_votes of this RankingWeekRanks.  # noqa: E501
        :rtype: int
        """
        return self._first_place_votes

    @first_place_votes.setter
    def first_place_votes(self, first_place_votes):
        """Sets the first_place_votes of this RankingWeekRanks.


        :param first_place_votes: The first_place_votes of this RankingWeekRanks.  # noqa: E501
        :type: int
        """

        self._first_place_votes = first_place_votes

    @property
    def points(self):
        """Gets the points of this RankingWeekRanks.  # noqa: E501


        :return: The points of this RankingWeekRanks.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this RankingWeekRanks.


        :param points: The points of this RankingWeekRanks.  # noqa: E501
        :type: int
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
        if issubclass(RankingWeekRanks, dict):
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
        if not isinstance(other, RankingWeekRanks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
