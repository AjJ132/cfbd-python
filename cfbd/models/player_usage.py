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


class PlayerUsage(object):
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
        'id': 'int',
        'name': 'str',
        'position': 'str',
        'team': 'str',
        'conference': 'str',
        'usage': 'PlayerUsageUsage'
    }

    attribute_map = {
        'season': 'season',
        'id': 'id',
        'name': 'name',
        'position': 'position',
        'team': 'team',
        'conference': 'conference',
        'usage': 'usage'
    }

    def __init__(self, season=None, id=None, name=None, position=None, team=None, conference=None, usage=None):  # noqa: E501
        """PlayerUsage - a model defined in Swagger"""  # noqa: E501

        self._season = None
        self._id = None
        self._name = None
        self._position = None
        self._team = None
        self._conference = None
        self._usage = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if team is not None:
            self.team = team
        if conference is not None:
            self.conference = conference
        if usage is not None:
            self.usage = usage

    @property
    def season(self):
        """Gets the season of this PlayerUsage.  # noqa: E501


        :return: The season of this PlayerUsage.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayerUsage.


        :param season: The season of this PlayerUsage.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def id(self):
        """Gets the id of this PlayerUsage.  # noqa: E501


        :return: The id of this PlayerUsage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlayerUsage.


        :param id: The id of this PlayerUsage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PlayerUsage.  # noqa: E501


        :return: The name of this PlayerUsage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerUsage.


        :param name: The name of this PlayerUsage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this PlayerUsage.  # noqa: E501


        :return: The position of this PlayerUsage.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this PlayerUsage.


        :param position: The position of this PlayerUsage.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def team(self):
        """Gets the team of this PlayerUsage.  # noqa: E501


        :return: The team of this PlayerUsage.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerUsage.


        :param team: The team of this PlayerUsage.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def conference(self):
        """Gets the conference of this PlayerUsage.  # noqa: E501


        :return: The conference of this PlayerUsage.  # noqa: E501
        :rtype: str
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this PlayerUsage.


        :param conference: The conference of this PlayerUsage.  # noqa: E501
        :type: str
        """

        self._conference = conference

    @property
    def usage(self):
        """Gets the usage of this PlayerUsage.  # noqa: E501


        :return: The usage of this PlayerUsage.  # noqa: E501
        :rtype: PlayerUsageUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this PlayerUsage.


        :param usage: The usage of this PlayerUsage.  # noqa: E501
        :type: PlayerUsageUsage
        """

        self._usage = usage

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
        if issubclass(PlayerUsage, dict):
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
        if not isinstance(other, PlayerUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
