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


class AdvancedGameStatOffense(object):
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
        'plays': 'int',
        'drives': 'int',
        'ppa': 'float',
        'total_ppa': 'float',
        'success_rate': 'float',
        'explosiveness': 'float',
        'power_success': 'float',
        'stuff_rate': 'float',
        'line_yards': 'float',
        'line_yards_total': 'float',
        'second_level_yards': 'float',
        'second_level_yards_total': 'int',
        'open_field_yards': 'float',
        'open_field_yards_total': 'int',
        'standard_downs': 'AdvancedGameStatOffenseStandardDowns',
        'passing_downs': 'AdvancedGameStatOffenseStandardDowns',
        'rushing_plays': 'AdvancedGameStatOffenseRushingPlays',
        'passing_plays': 'AdvancedGameStatOffenseRushingPlays'
    }

    attribute_map = {
        'plays': 'plays',
        'drives': 'drives',
        'ppa': 'ppa',
        'total_ppa': 'totalPPA',
        'success_rate': 'successRate',
        'explosiveness': 'explosiveness',
        'power_success': 'powerSuccess',
        'stuff_rate': 'stuffRate',
        'line_yards': 'lineYards',
        'line_yards_total': 'lineYardsTotal',
        'second_level_yards': 'secondLevelYards',
        'second_level_yards_total': 'secondLevelYardsTotal',
        'open_field_yards': 'openFieldYards',
        'open_field_yards_total': 'openFieldYardsTotal',
        'standard_downs': 'standardDowns',
        'passing_downs': 'passingDowns',
        'rushing_plays': 'rushingPlays',
        'passing_plays': 'passingPlays'
    }

    def __init__(self, plays=None, drives=None, ppa=None, total_ppa=None, success_rate=None, explosiveness=None, power_success=None, stuff_rate=None, line_yards=None, line_yards_total=None, second_level_yards=None, second_level_yards_total=None, open_field_yards=None, open_field_yards_total=None, standard_downs=None, passing_downs=None, rushing_plays=None, passing_plays=None):  # noqa: E501
        """AdvancedGameStatOffense - a model defined in Swagger"""  # noqa: E501

        self._plays = None
        self._drives = None
        self._ppa = None
        self._total_ppa = None
        self._success_rate = None
        self._explosiveness = None
        self._power_success = None
        self._stuff_rate = None
        self._line_yards = None
        self._line_yards_total = None
        self._second_level_yards = None
        self._second_level_yards_total = None
        self._open_field_yards = None
        self._open_field_yards_total = None
        self._standard_downs = None
        self._passing_downs = None
        self._rushing_plays = None
        self._passing_plays = None
        self.discriminator = None

        if plays is not None:
            self.plays = plays
        if drives is not None:
            self.drives = drives
        if ppa is not None:
            self.ppa = ppa
        if total_ppa is not None:
            self.total_ppa = total_ppa
        if success_rate is not None:
            self.success_rate = success_rate
        if explosiveness is not None:
            self.explosiveness = explosiveness
        if power_success is not None:
            self.power_success = power_success
        if stuff_rate is not None:
            self.stuff_rate = stuff_rate
        if line_yards is not None:
            self.line_yards = line_yards
        if line_yards_total is not None:
            self.line_yards_total = line_yards_total
        if second_level_yards is not None:
            self.second_level_yards = second_level_yards
        if second_level_yards_total is not None:
            self.second_level_yards_total = second_level_yards_total
        if open_field_yards is not None:
            self.open_field_yards = open_field_yards
        if open_field_yards_total is not None:
            self.open_field_yards_total = open_field_yards_total
        if standard_downs is not None:
            self.standard_downs = standard_downs
        if passing_downs is not None:
            self.passing_downs = passing_downs
        if rushing_plays is not None:
            self.rushing_plays = rushing_plays
        if passing_plays is not None:
            self.passing_plays = passing_plays

    @property
    def plays(self):
        """Gets the plays of this AdvancedGameStatOffense.  # noqa: E501


        :return: The plays of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: int
        """
        return self._plays

    @plays.setter
    def plays(self, plays):
        """Sets the plays of this AdvancedGameStatOffense.


        :param plays: The plays of this AdvancedGameStatOffense.  # noqa: E501
        :type: int
        """

        self._plays = plays

    @property
    def drives(self):
        """Gets the drives of this AdvancedGameStatOffense.  # noqa: E501


        :return: The drives of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: int
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this AdvancedGameStatOffense.


        :param drives: The drives of this AdvancedGameStatOffense.  # noqa: E501
        :type: int
        """

        self._drives = drives

    @property
    def ppa(self):
        """Gets the ppa of this AdvancedGameStatOffense.  # noqa: E501


        :return: The ppa of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._ppa

    @ppa.setter
    def ppa(self, ppa):
        """Sets the ppa of this AdvancedGameStatOffense.


        :param ppa: The ppa of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._ppa = ppa

    @property
    def total_ppa(self):
        """Gets the total_ppa of this AdvancedGameStatOffense.  # noqa: E501


        :return: The total_ppa of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._total_ppa

    @total_ppa.setter
    def total_ppa(self, total_ppa):
        """Sets the total_ppa of this AdvancedGameStatOffense.


        :param total_ppa: The total_ppa of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._total_ppa = total_ppa

    @property
    def success_rate(self):
        """Gets the success_rate of this AdvancedGameStatOffense.  # noqa: E501


        :return: The success_rate of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this AdvancedGameStatOffense.


        :param success_rate: The success_rate of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._success_rate = success_rate

    @property
    def explosiveness(self):
        """Gets the explosiveness of this AdvancedGameStatOffense.  # noqa: E501


        :return: The explosiveness of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this AdvancedGameStatOffense.


        :param explosiveness: The explosiveness of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._explosiveness = explosiveness

    @property
    def power_success(self):
        """Gets the power_success of this AdvancedGameStatOffense.  # noqa: E501


        :return: The power_success of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._power_success

    @power_success.setter
    def power_success(self, power_success):
        """Sets the power_success of this AdvancedGameStatOffense.


        :param power_success: The power_success of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._power_success = power_success

    @property
    def stuff_rate(self):
        """Gets the stuff_rate of this AdvancedGameStatOffense.  # noqa: E501


        :return: The stuff_rate of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._stuff_rate

    @stuff_rate.setter
    def stuff_rate(self, stuff_rate):
        """Sets the stuff_rate of this AdvancedGameStatOffense.


        :param stuff_rate: The stuff_rate of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._stuff_rate = stuff_rate

    @property
    def line_yards(self):
        """Gets the line_yards of this AdvancedGameStatOffense.  # noqa: E501


        :return: The line_yards of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._line_yards

    @line_yards.setter
    def line_yards(self, line_yards):
        """Sets the line_yards of this AdvancedGameStatOffense.


        :param line_yards: The line_yards of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._line_yards = line_yards

    @property
    def line_yards_total(self):
        """Gets the line_yards_total of this AdvancedGameStatOffense.  # noqa: E501


        :return: The line_yards_total of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._line_yards_total

    @line_yards_total.setter
    def line_yards_total(self, line_yards_total):
        """Sets the line_yards_total of this AdvancedGameStatOffense.


        :param line_yards_total: The line_yards_total of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._line_yards_total = line_yards_total

    @property
    def second_level_yards(self):
        """Gets the second_level_yards of this AdvancedGameStatOffense.  # noqa: E501


        :return: The second_level_yards of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._second_level_yards

    @second_level_yards.setter
    def second_level_yards(self, second_level_yards):
        """Sets the second_level_yards of this AdvancedGameStatOffense.


        :param second_level_yards: The second_level_yards of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._second_level_yards = second_level_yards

    @property
    def second_level_yards_total(self):
        """Gets the second_level_yards_total of this AdvancedGameStatOffense.  # noqa: E501


        :return: The second_level_yards_total of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: int
        """
        return self._second_level_yards_total

    @second_level_yards_total.setter
    def second_level_yards_total(self, second_level_yards_total):
        """Sets the second_level_yards_total of this AdvancedGameStatOffense.


        :param second_level_yards_total: The second_level_yards_total of this AdvancedGameStatOffense.  # noqa: E501
        :type: int
        """

        self._second_level_yards_total = second_level_yards_total

    @property
    def open_field_yards(self):
        """Gets the open_field_yards of this AdvancedGameStatOffense.  # noqa: E501


        :return: The open_field_yards of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: float
        """
        return self._open_field_yards

    @open_field_yards.setter
    def open_field_yards(self, open_field_yards):
        """Sets the open_field_yards of this AdvancedGameStatOffense.


        :param open_field_yards: The open_field_yards of this AdvancedGameStatOffense.  # noqa: E501
        :type: float
        """

        self._open_field_yards = open_field_yards

    @property
    def open_field_yards_total(self):
        """Gets the open_field_yards_total of this AdvancedGameStatOffense.  # noqa: E501


        :return: The open_field_yards_total of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: int
        """
        return self._open_field_yards_total

    @open_field_yards_total.setter
    def open_field_yards_total(self, open_field_yards_total):
        """Sets the open_field_yards_total of this AdvancedGameStatOffense.


        :param open_field_yards_total: The open_field_yards_total of this AdvancedGameStatOffense.  # noqa: E501
        :type: int
        """

        self._open_field_yards_total = open_field_yards_total

    @property
    def standard_downs(self):
        """Gets the standard_downs of this AdvancedGameStatOffense.  # noqa: E501


        :return: The standard_downs of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: AdvancedGameStatOffenseStandardDowns
        """
        return self._standard_downs

    @standard_downs.setter
    def standard_downs(self, standard_downs):
        """Sets the standard_downs of this AdvancedGameStatOffense.


        :param standard_downs: The standard_downs of this AdvancedGameStatOffense.  # noqa: E501
        :type: AdvancedGameStatOffenseStandardDowns
        """

        self._standard_downs = standard_downs

    @property
    def passing_downs(self):
        """Gets the passing_downs of this AdvancedGameStatOffense.  # noqa: E501


        :return: The passing_downs of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: AdvancedGameStatOffenseStandardDowns
        """
        return self._passing_downs

    @passing_downs.setter
    def passing_downs(self, passing_downs):
        """Sets the passing_downs of this AdvancedGameStatOffense.


        :param passing_downs: The passing_downs of this AdvancedGameStatOffense.  # noqa: E501
        :type: AdvancedGameStatOffenseStandardDowns
        """

        self._passing_downs = passing_downs

    @property
    def rushing_plays(self):
        """Gets the rushing_plays of this AdvancedGameStatOffense.  # noqa: E501


        :return: The rushing_plays of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: AdvancedGameStatOffenseRushingPlays
        """
        return self._rushing_plays

    @rushing_plays.setter
    def rushing_plays(self, rushing_plays):
        """Sets the rushing_plays of this AdvancedGameStatOffense.


        :param rushing_plays: The rushing_plays of this AdvancedGameStatOffense.  # noqa: E501
        :type: AdvancedGameStatOffenseRushingPlays
        """

        self._rushing_plays = rushing_plays

    @property
    def passing_plays(self):
        """Gets the passing_plays of this AdvancedGameStatOffense.  # noqa: E501


        :return: The passing_plays of this AdvancedGameStatOffense.  # noqa: E501
        :rtype: AdvancedGameStatOffenseRushingPlays
        """
        return self._passing_plays

    @passing_plays.setter
    def passing_plays(self, passing_plays):
        """Sets the passing_plays of this AdvancedGameStatOffense.


        :param passing_plays: The passing_plays of this AdvancedGameStatOffense.  # noqa: E501
        :type: AdvancedGameStatOffenseRushingPlays
        """

        self._passing_plays = passing_plays

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
        if issubclass(AdvancedGameStatOffense, dict):
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
        if not isinstance(other, AdvancedGameStatOffense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
