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


class RankingWeekPolls(object):
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
        'poll': 'str',
        'ranks': 'list[RankingWeekRanks]'
    }

    attribute_map = {
        'poll': 'poll',
        'ranks': 'ranks'
    }

    def __init__(self, poll=None, ranks=None):  # noqa: E501
        """RankingWeekPolls - a model defined in Swagger"""  # noqa: E501

        self._poll = None
        self._ranks = None
        self.discriminator = None

        if poll is not None:
            self.poll = poll
        if ranks is not None:
            self.ranks = ranks

    @property
    def poll(self):
        """Gets the poll of this RankingWeekPolls.  # noqa: E501


        :return: The poll of this RankingWeekPolls.  # noqa: E501
        :rtype: str
        """
        return self._poll

    @poll.setter
    def poll(self, poll):
        """Sets the poll of this RankingWeekPolls.


        :param poll: The poll of this RankingWeekPolls.  # noqa: E501
        :type: str
        """

        self._poll = poll

    @property
    def ranks(self):
        """Gets the ranks of this RankingWeekPolls.  # noqa: E501


        :return: The ranks of this RankingWeekPolls.  # noqa: E501
        :rtype: list[RankingWeekRanks]
        """
        return self._ranks

    @ranks.setter
    def ranks(self, ranks):
        """Sets the ranks of this RankingWeekPolls.


        :param ranks: The ranks of this RankingWeekPolls.  # noqa: E501
        :type: list[RankingWeekRanks]
        """

        self._ranks = ranks

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
        if issubclass(RankingWeekPolls, dict):
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
        if not isinstance(other, RankingWeekPolls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
