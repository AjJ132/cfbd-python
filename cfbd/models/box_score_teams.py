# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  It currently has a wide array of data ranging from play by play to player statistics to game scores and more.  # noqa: E501

    OpenAPI spec version: 2.3.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BoxScoreTeams(object):
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
        'ppa': 'list[BoxScoreTeamsPpa]',
        'cumulative_ppa': 'list[BoxScoreTeamsPpa]',
        'success_rates': 'list[BoxScoreTeamsSuccessRates]',
        'explosiveness': 'list[BoxScoreTeamsExplosiveness]',
        'rushing': 'list[BoxScoreTeamsRushing]',
        'havoc': 'list[BoxScoreTeamsHavoc]',
        'scoring_opportunities': 'list[BoxScoreTeamsScoringOpportunities]',
        'field_position': 'list[BoxScoreTeamsFieldPosition]'
    }

    attribute_map = {
        'ppa': 'ppa',
        'cumulative_ppa': 'cumulativePpa',
        'success_rates': 'successRates',
        'explosiveness': 'explosiveness',
        'rushing': 'rushing',
        'havoc': 'havoc',
        'scoring_opportunities': 'scoringOpportunities',
        'field_position': 'fieldPosition'
    }

    def __init__(self, ppa=None, cumulative_ppa=None, success_rates=None, explosiveness=None, rushing=None, havoc=None, scoring_opportunities=None, field_position=None):  # noqa: E501
        """BoxScoreTeams - a model defined in Swagger"""  # noqa: E501

        self._ppa = None
        self._cumulative_ppa = None
        self._success_rates = None
        self._explosiveness = None
        self._rushing = None
        self._havoc = None
        self._scoring_opportunities = None
        self._field_position = None
        self.discriminator = None

        if ppa is not None:
            self.ppa = ppa
        if cumulative_ppa is not None:
            self.cumulative_ppa = cumulative_ppa
        if success_rates is not None:
            self.success_rates = success_rates
        if explosiveness is not None:
            self.explosiveness = explosiveness
        if rushing is not None:
            self.rushing = rushing
        if havoc is not None:
            self.havoc = havoc
        if scoring_opportunities is not None:
            self.scoring_opportunities = scoring_opportunities
        if field_position is not None:
            self.field_position = field_position

    @property
    def ppa(self):
        """Gets the ppa of this BoxScoreTeams.  # noqa: E501


        :return: The ppa of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsPpa]
        """
        return self._ppa

    @ppa.setter
    def ppa(self, ppa):
        """Sets the ppa of this BoxScoreTeams.


        :param ppa: The ppa of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsPpa]
        """

        self._ppa = ppa

    @property
    def cumulative_ppa(self):
        """Gets the cumulative_ppa of this BoxScoreTeams.  # noqa: E501


        :return: The cumulative_ppa of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsPpa]
        """
        return self._cumulative_ppa

    @cumulative_ppa.setter
    def cumulative_ppa(self, cumulative_ppa):
        """Sets the cumulative_ppa of this BoxScoreTeams.


        :param cumulative_ppa: The cumulative_ppa of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsPpa]
        """

        self._cumulative_ppa = cumulative_ppa

    @property
    def success_rates(self):
        """Gets the success_rates of this BoxScoreTeams.  # noqa: E501


        :return: The success_rates of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsSuccessRates]
        """
        return self._success_rates

    @success_rates.setter
    def success_rates(self, success_rates):
        """Sets the success_rates of this BoxScoreTeams.


        :param success_rates: The success_rates of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsSuccessRates]
        """

        self._success_rates = success_rates

    @property
    def explosiveness(self):
        """Gets the explosiveness of this BoxScoreTeams.  # noqa: E501


        :return: The explosiveness of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsExplosiveness]
        """
        return self._explosiveness

    @explosiveness.setter
    def explosiveness(self, explosiveness):
        """Sets the explosiveness of this BoxScoreTeams.


        :param explosiveness: The explosiveness of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsExplosiveness]
        """

        self._explosiveness = explosiveness

    @property
    def rushing(self):
        """Gets the rushing of this BoxScoreTeams.  # noqa: E501


        :return: The rushing of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsRushing]
        """
        return self._rushing

    @rushing.setter
    def rushing(self, rushing):
        """Sets the rushing of this BoxScoreTeams.


        :param rushing: The rushing of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsRushing]
        """

        self._rushing = rushing

    @property
    def havoc(self):
        """Gets the havoc of this BoxScoreTeams.  # noqa: E501


        :return: The havoc of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsHavoc]
        """
        return self._havoc

    @havoc.setter
    def havoc(self, havoc):
        """Sets the havoc of this BoxScoreTeams.


        :param havoc: The havoc of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsHavoc]
        """

        self._havoc = havoc

    @property
    def scoring_opportunities(self):
        """Gets the scoring_opportunities of this BoxScoreTeams.  # noqa: E501


        :return: The scoring_opportunities of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsScoringOpportunities]
        """
        return self._scoring_opportunities

    @scoring_opportunities.setter
    def scoring_opportunities(self, scoring_opportunities):
        """Sets the scoring_opportunities of this BoxScoreTeams.


        :param scoring_opportunities: The scoring_opportunities of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsScoringOpportunities]
        """

        self._scoring_opportunities = scoring_opportunities

    @property
    def field_position(self):
        """Gets the field_position of this BoxScoreTeams.  # noqa: E501


        :return: The field_position of this BoxScoreTeams.  # noqa: E501
        :rtype: list[BoxScoreTeamsFieldPosition]
        """
        return self._field_position

    @field_position.setter
    def field_position(self, field_position):
        """Sets the field_position of this BoxScoreTeams.


        :param field_position: The field_position of this BoxScoreTeams.  # noqa: E501
        :type: list[BoxScoreTeamsFieldPosition]
        """

        self._field_position = field_position

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
        if issubclass(BoxScoreTeams, dict):
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
        if not isinstance(other, BoxScoreTeams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
