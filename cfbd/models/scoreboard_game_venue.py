# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.9
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class ScoreboardGameVenue(object):
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
        'name': 'str',
        'city': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'city': 'city',
        'state': 'state'
    }

    def __init__(self, name=None, city=None, state=None, _configuration=None):  # noqa: E501
        """ScoreboardGameVenue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._city = None
        self._state = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state

    @property
    def name(self):
        """Gets the name of this ScoreboardGameVenue.  # noqa: E501


        :return: The name of this ScoreboardGameVenue.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScoreboardGameVenue.


        :param name: The name of this ScoreboardGameVenue.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """Gets the city of this ScoreboardGameVenue.  # noqa: E501


        :return: The city of this ScoreboardGameVenue.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ScoreboardGameVenue.


        :param city: The city of this ScoreboardGameVenue.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this ScoreboardGameVenue.  # noqa: E501


        :return: The state of this ScoreboardGameVenue.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ScoreboardGameVenue.


        :param state: The state of this ScoreboardGameVenue.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(ScoreboardGameVenue, dict):
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
        if not isinstance(other, ScoreboardGameVenue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScoreboardGameVenue):
            return True

        return self.to_dict() != other.to_dict()
