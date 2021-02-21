# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DriveStartTime(object):
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
        'minutes': 'int',
        'seconds': 'int'
    }

    attribute_map = {
        'minutes': 'minutes',
        'seconds': 'seconds'
    }

    def __init__(self, minutes=None, seconds=None):  # noqa: E501
        """DriveStartTime - a model defined in Swagger"""  # noqa: E501

        self._minutes = None
        self._seconds = None
        self.discriminator = None

        if minutes is not None:
            self.minutes = minutes
        if seconds is not None:
            self.seconds = seconds

    @property
    def minutes(self):
        """Gets the minutes of this DriveStartTime.  # noqa: E501


        :return: The minutes of this DriveStartTime.  # noqa: E501
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, minutes):
        """Sets the minutes of this DriveStartTime.


        :param minutes: The minutes of this DriveStartTime.  # noqa: E501
        :type: int
        """

        self._minutes = minutes

    @property
    def seconds(self):
        """Gets the seconds of this DriveStartTime.  # noqa: E501


        :return: The seconds of this DriveStartTime.  # noqa: E501
        :rtype: int
        """
        return self._seconds

    @seconds.setter
    def seconds(self, seconds):
        """Sets the seconds of this DriveStartTime.


        :param seconds: The seconds of this DriveStartTime.  # noqa: E501
        :type: int
        """

        self._seconds = seconds

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
        if issubclass(DriveStartTime, dict):
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
        if not isinstance(other, DriveStartTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
