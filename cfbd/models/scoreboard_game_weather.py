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


class ScoreboardGameWeather(object):
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
        'temperature': 'float',
        'description': 'str',
        'wind_speed': 'float',
        'wind_direction': 'float'
    }

    attribute_map = {
        'temperature': 'temperature',
        'description': 'description',
        'wind_speed': 'windSpeed',
        'wind_direction': 'windDirection'
    }

    def __init__(self, temperature=None, description=None, wind_speed=None, wind_direction=None, _configuration=None):  # noqa: E501
        """ScoreboardGameWeather - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._temperature = None
        self._description = None
        self._wind_speed = None
        self._wind_direction = None
        self.discriminator = None

        if temperature is not None:
            self.temperature = temperature
        if description is not None:
            self.description = description
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if wind_direction is not None:
            self.wind_direction = wind_direction

    @property
    def temperature(self):
        """Gets the temperature of this ScoreboardGameWeather.  # noqa: E501


        :return: The temperature of this ScoreboardGameWeather.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this ScoreboardGameWeather.


        :param temperature: The temperature of this ScoreboardGameWeather.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def description(self):
        """Gets the description of this ScoreboardGameWeather.  # noqa: E501


        :return: The description of this ScoreboardGameWeather.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ScoreboardGameWeather.


        :param description: The description of this ScoreboardGameWeather.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def wind_speed(self):
        """Gets the wind_speed of this ScoreboardGameWeather.  # noqa: E501


        :return: The wind_speed of this ScoreboardGameWeather.  # noqa: E501
        :rtype: float
        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        """Sets the wind_speed of this ScoreboardGameWeather.


        :param wind_speed: The wind_speed of this ScoreboardGameWeather.  # noqa: E501
        :type: float
        """

        self._wind_speed = wind_speed

    @property
    def wind_direction(self):
        """Gets the wind_direction of this ScoreboardGameWeather.  # noqa: E501


        :return: The wind_direction of this ScoreboardGameWeather.  # noqa: E501
        :rtype: float
        """
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, wind_direction):
        """Sets the wind_direction of this ScoreboardGameWeather.


        :param wind_direction: The wind_direction of this ScoreboardGameWeather.  # noqa: E501
        :type: float
        """

        self._wind_direction = wind_direction

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
        if issubclass(ScoreboardGameWeather, dict):
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
        if not isinstance(other, ScoreboardGameWeather):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScoreboardGameWeather):
            return True

        return self.to_dict() != other.to_dict()
