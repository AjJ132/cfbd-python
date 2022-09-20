# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.4
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class TeamGameTeams(object):
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
        'school': 'str',
        'conference': 'str',
        'home_away': 'bool',
        'points': 'int',
        'stats': 'list[TeamGameStats]'
    }

    attribute_map = {
        'school': 'school',
        'conference': 'conference',
        'home_away': 'homeAway',
        'points': 'points',
        'stats': 'stats'
    }

    def __init__(self, school=None, conference=None, home_away=None, points=None, stats=None, _configuration=None):  # noqa: E501
        """TeamGameTeams - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._school = None
        self._conference = None
        self._home_away = None
        self._points = None
        self._stats = None
        self.discriminator = None

        if school is not None:
            self.school = school
        if conference is not None:
            self.conference = conference
        if home_away is not None:
            self.home_away = home_away
        if points is not None:
            self.points = points
        if stats is not None:
            self.stats = stats

    @property
    def school(self):
        """Gets the school of this TeamGameTeams.  # noqa: E501


        :return: The school of this TeamGameTeams.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this TeamGameTeams.


        :param school: The school of this TeamGameTeams.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def conference(self):
        """Gets the conference of this TeamGameTeams.  # noqa: E501


        :return: The conference of this TeamGameTeams.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this TeamGameTeams.


        :param conference: The conference of this TeamGameTeams.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def home_away(self):
        """Gets the home_away of this TeamGameTeams.  # noqa: E501


        :return: The home_away of this TeamGameTeams.  # noqa: E501
        :rtype: bool
        """
        return self._home_away

    @home_away.setter
    def home_away(self, home_away):
        """Sets the home_away of this TeamGameTeams.


        :param home_away: The home_away of this TeamGameTeams.  # noqa: E501
        :type: bool
        """

        self._home_away = home_away

    @property
    def points(self):
        """Gets the points of this TeamGameTeams.  # noqa: E501


        :return: The points of this TeamGameTeams.  # noqa: E501
        :rtype: int
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this TeamGameTeams.


        :param points: The points of this TeamGameTeams.  # noqa: E501
        :type: int
        """

        self._points = points

    @property
    def stats(self):
        """Gets the stats of this TeamGameTeams.  # noqa: E501


        :return: The stats of this TeamGameTeams.  # noqa: E501
        :rtype: list[TeamGameStats]
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this TeamGameTeams.


        :param stats: The stats of this TeamGameTeams.  # noqa: E501
        :type: list[TeamGameStats]
        """

        self._stats = stats

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
        if issubclass(TeamGameTeams, dict):
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
        if not isinstance(other, TeamGameTeams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamGameTeams):
            return True

        return self.to_dict() != other.to_dict()
