# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.8
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PlayerGameTypes(object):
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
        'athletes': 'list[PlayerGameAthletes]'
    }

    attribute_map = {
        'name': 'name',
        'athletes': 'athletes'
    }

    def __init__(self, name=None, athletes=None):  # noqa: E501
        """PlayerGameTypes - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._athletes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if athletes is not None:
            self.athletes = athletes

    @property
    def name(self):
        """Gets the name of this PlayerGameTypes.  # noqa: E501


        :return: The name of this PlayerGameTypes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PlayerGameTypes.


        :param name: The name of this PlayerGameTypes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def athletes(self):
        """Gets the athletes of this PlayerGameTypes.  # noqa: E501


        :return: The athletes of this PlayerGameTypes.  # noqa: E501
        :rtype: list[PlayerGameAthletes]
        """
        return self._athletes

    @athletes.setter
    def athletes(self, athletes):
        """Sets the athletes of this PlayerGameTypes.


        :param athletes: The athletes of this PlayerGameTypes.  # noqa: E501
        :type: list[PlayerGameAthletes]
        """

        self._athletes = athletes

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
        if issubclass(PlayerGameTypes, dict):
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
        if not isinstance(other, PlayerGameTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
