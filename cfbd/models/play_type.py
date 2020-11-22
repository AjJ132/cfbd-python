# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.2.17
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PlayType(object):
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
        'id': 'int',
        'text': 'str',
        'abbreviation': 'str'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'abbreviation': 'abbreviation'
    }

    def __init__(self, id=None, text=None, abbreviation=None):  # noqa: E501
        """PlayType - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._text = None
        self._abbreviation = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if abbreviation is not None:
            self.abbreviation = abbreviation

    @property
    def id(self):
        """Gets the id of this PlayType.  # noqa: E501


        :return: The id of this PlayType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlayType.


        :param id: The id of this PlayType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this PlayType.  # noqa: E501


        :return: The text of this PlayType.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PlayType.


        :param text: The text of this PlayType.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def abbreviation(self):
        """Gets the abbreviation of this PlayType.  # noqa: E501


        :return: The abbreviation of this PlayType.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this PlayType.


        :param abbreviation: The abbreviation of this PlayType.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

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
        if issubclass(PlayType, dict):
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
        if not isinstance(other, PlayType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
