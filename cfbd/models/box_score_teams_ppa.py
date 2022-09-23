# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class BoxScoreTeamsPpa(object):
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
        'team': 'str',
        'plays': 'float',
        'overall': 'BoxScoreTeamsOverall',
        'passing': 'BoxScoreTeamsOverall',
        'rushing': 'BoxScoreTeamsOverall'
    }

    attribute_map = {
        'team': 'team',
        'plays': 'plays',
        'overall': 'overall',
        'passing': 'passing',
        'rushing': 'rushing'
    }

    def __init__(self, team=None, plays=None, overall=None, passing=None, rushing=None, _configuration=None):  # noqa: E501
        """BoxScoreTeamsPpa - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team = None
        self._plays = None
        self._overall = None
        self._passing = None
        self._rushing = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if plays is not None:
            self.plays = plays
        if overall is not None:
            self.overall = overall
        if passing is not None:
            self.passing = passing
        if rushing is not None:
            self.rushing = rushing

    @property
    def team(self):
        """Gets the team of this BoxScoreTeamsPpa.  # noqa: E501


        :return: The team of this BoxScoreTeamsPpa.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScoreTeamsPpa.


        :param team: The team of this BoxScoreTeamsPpa.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def plays(self):
        """Gets the plays of this BoxScoreTeamsPpa.  # noqa: E501


        :return: The plays of this BoxScoreTeamsPpa.  # noqa: E501
        :rtype: float
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this BoxScoreTeamsPpa.


        :param plays: The plays of this BoxScoreTeamsPpa.  # noqa: E501
        :type: float
        """

        self._plays = plays

    @property
    def overall(self):
        """Gets the overall of this BoxScoreTeamsPpa.  # noqa: E501


        :return: The overall of this BoxScoreTeamsPpa.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this BoxScoreTeamsPpa.


        :param overall: The overall of this BoxScoreTeamsPpa.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._overall = overall

    @property
    def passing(self):
        """Gets the passing of this BoxScoreTeamsPpa.  # noqa: E501


        :return: The passing of this BoxScoreTeamsPpa.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._passing

    @passing.setter
    def passing(self, passing):
        """Sets the passing of this BoxScoreTeamsPpa.


        :param passing: The passing of this BoxScoreTeamsPpa.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._passing = passing

    @property
    def rushing(self):
        """Gets the rushing of this BoxScoreTeamsPpa.  # noqa: E501


        :return: The rushing of this BoxScoreTeamsPpa.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this BoxScoreTeamsPpa.


        :param rushing: The rushing of this BoxScoreTeamsPpa.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._rushing = rushing

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
        if issubclass(BoxScoreTeamsPpa, dict):
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
        if not isinstance(other, BoxScoreTeamsPpa):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoxScoreTeamsPpa):
            return True

        return self.to_dict() != other.to_dict()
