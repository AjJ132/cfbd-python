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


class BoxScoreTeamsSuccessRates(object):
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
        'overall': 'BoxScoreTeamsOverall',
        'standard_downs': 'BoxScoreTeamsOverall',
        'passing_downs': 'BoxScoreTeamsOverall'
    }

    attribute_map = {
        'team': 'team',
        'overall': 'overall',
        'standard_downs': 'standardDowns',
        'passing_downs': 'passingDowns'
    }

    def __init__(self, team=None, overall=None, standard_downs=None, passing_downs=None, _configuration=None):  # noqa: E501
        """BoxScoreTeamsSuccessRates - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._team = None
        self._overall = None
        self._standard_downs = None
        self._passing_downs = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if overall is not None:
            self.overall = overall
        if standard_downs is not None:
            self.standard_downs = standard_downs
        if passing_downs is not None:
            self.passing_downs = passing_downs

    @property
    def team(self):
        """Gets the team of this BoxScoreTeamsSuccessRates.  # noqa: E501


        :return: The team of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this BoxScoreTeamsSuccessRates.


        :param team: The team of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def overall(self):
        """Gets the overall of this BoxScoreTeamsSuccessRates.  # noqa: E501


        :return: The overall of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this BoxScoreTeamsSuccessRates.


        :param overall: The overall of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._overall = overall

    @property
    def standard_downs(self):
        """Gets the standard_downs of this BoxScoreTeamsSuccessRates.  # noqa: E501


        :return: The standard_downs of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._standard_downs

    @standard_downs.setter
    def standard_downs(self, standard_downs):
        """Sets the standard_downs of this BoxScoreTeamsSuccessRates.


        :param standard_downs: The standard_downs of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._standard_downs = standard_downs

    @property
    def passing_downs(self):
        """Gets the passing_downs of this BoxScoreTeamsSuccessRates.  # noqa: E501


        :return: The passing_downs of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :rtype: BoxScoreTeamsOverall
        """
        return self._passing_downs

    @passing_downs.setter
    def passing_downs(self, passing_downs):
        """Sets the passing_downs of this BoxScoreTeamsSuccessRates.


        :param passing_downs: The passing_downs of this BoxScoreTeamsSuccessRates.  # noqa: E501
        :type: BoxScoreTeamsOverall
        """

        self._passing_downs = passing_downs

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
        if issubclass(BoxScoreTeamsSuccessRates, dict):
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
        if not isinstance(other, BoxScoreTeamsSuccessRates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BoxScoreTeamsSuccessRates):
            return True

        return self.to_dict() != other.to_dict()
