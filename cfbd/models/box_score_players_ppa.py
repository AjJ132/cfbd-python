# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.6
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BoxScorePlayersPpa(object):
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
        'player': 'str',
        'team': 'str',
        'position': 'str',
        'average': 'BoxScorePlayersAverage',
        'cumulative': 'BoxScorePlayersAverage'
    }

    attribute_map = {
        'player': 'player',
        'team': 'team',
        'position': 'position',
        'average': 'average',
        'cumulative': 'cumulative'
    }

    def __init__(self, player=None, team=None, position=None, average=None, cumulative=None):  # noqa: E501
        """BoxScorePlayersPpa - a model defined in Swagger"""  # noqa: E501

        self._player = None
        self._team = None
        self._position = None
        self._average = None
        self._cumulative = None
        self.discriminator = None

        if player is not None:
            self.player = player
        if team is not None:
            self.team = team
        if position is not None:
            self.position = position
        if average is not None:
            self.average = average
        if cumulative is not None:
            self.cumulative = cumulative

    @property
    def player(self):
        """Gets the player of this BoxScorePlayersPpa.  # noqa: E501


        :return: The player of this BoxScorePlayersPpa.  # noqa: E501
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this BoxScorePlayersPpa.


        :param player: The player of this BoxScorePlayersPpa.  # noqa: E501
        :type: str
        """

        self._player = player

    @property
    def team(self):
        """Gets the team of this BoxScorePlayersPpa.  # noqa: E501


        :return: The team of this BoxScorePlayersPpa.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScorePlayersPpa.


        :param team: The team of this BoxScorePlayersPpa.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def position(self):
        """Gets the position of this BoxScorePlayersPpa.  # noqa: E501


        :return: The position of this BoxScorePlayersPpa.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this BoxScorePlayersPpa.


        :param position: The position of this BoxScorePlayersPpa.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def average(self):
        """Gets the average of this BoxScorePlayersPpa.  # noqa: E501


        :return: The average of this BoxScorePlayersPpa.  # noqa: E501
        :rtype: BoxScorePlayersAverage
        """
        return self._average

    @average.setter
    def average(self, average):
        """Sets the average of this BoxScorePlayersPpa.


        :param average: The average of this BoxScorePlayersPpa.  # noqa: E501
        :type: BoxScorePlayersAverage
        """

        self._average = average

    @property
    def cumulative(self):
        """Gets the cumulative of this BoxScorePlayersPpa.  # noqa: E501


        :return: The cumulative of this BoxScorePlayersPpa.  # noqa: E501
        :rtype: BoxScorePlayersAverage
        """
        return self._cumulative

    @cumulative.setter
    def cumulative(self, cumulative):
        """Sets the cumulative of this BoxScorePlayersPpa.


        :param cumulative: The cumulative of this BoxScorePlayersPpa.  # noqa: E501
        :type: BoxScorePlayersAverage
        """

        self._cumulative = cumulative

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
        if issubclass(BoxScorePlayersPpa, dict):
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
        if not isinstance(other, BoxScorePlayersPpa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
