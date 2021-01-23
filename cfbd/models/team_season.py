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


class TeamSeason(object):
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
        'school': 'str',
        'year': 'str',
        'games': 'int',
        'wins': 'int',
        'losses': 'int',
        'ties': 'int',
        'preseason_rank': 'int',
        'postseason_rank': 'int',
        'srs': 'float',
        'sp_overall': 'float',
        'sp_offense': 'float',
        'sp_defense': 'float'
    }

    attribute_map = {
        'school': 'school',
        'year': 'year',
        'games': 'games',
        'wins': 'wins',
        'losses': 'losses',
        'ties': 'ties',
        'preseason_rank': 'preseason_rank',
        'postseason_rank': 'postseason_rank',
        'srs': 'srs',
        'sp_overall': 'sp_overall',
        'sp_offense': 'sp_offense',
        'sp_defense': 'sp_defense'
    }

    def __init__(self, school=None, year=None, games=None, wins=None, losses=None, ties=None, preseason_rank=None, postseason_rank=None, srs=None, sp_overall=None, sp_offense=None, sp_defense=None):  # noqa: E501
        """TeamSeason - a model defined in Swagger"""  # noqa: E501

        self._school = None
        self._year = None
        self._games = None
        self._wins = None
        self._losses = None
        self._ties = None
        self._preseason_rank = None
        self._postseason_rank = None
        self._srs = None
        self._sp_overall = None
        self._sp_offense = None
        self._sp_defense = None
        self.discriminator = None

        if school is not None:
            self.school = school
        if year is not None:
            self.year = year
        if games is not None:
            self.games = games
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if ties is not None:
            self.ties = ties
        if preseason_rank is not None:
            self.preseason_rank = preseason_rank
        if postseason_rank is not None:
            self.postseason_rank = postseason_rank
        if srs is not None:
            self.srs = srs
        if sp_overall is not None:
            self.sp_overall = sp_overall
        if sp_offense is not None:
            self.sp_offense = sp_offense
        if sp_defense is not None:
            self.sp_defense = sp_defense

    @property
    def school(self):
        """Gets the school of this TeamSeason.  # noqa: E501


        :return: The school of this TeamSeason.  # noqa: E501
        :rtype: str
        """
        return self._school

    @school.setter
    def school(self, school):
        """Sets the school of this TeamSeason.


        :param school: The school of this TeamSeason.  # noqa: E501
        :type: str
        """

        self._school = school

    @property
    def year(self):
        """Gets the year of this TeamSeason.  # noqa: E501


        :return: The year of this TeamSeason.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this TeamSeason.


        :param year: The year of this TeamSeason.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def games(self):
        """Gets the games of this TeamSeason.  # noqa: E501


        :return: The games of this TeamSeason.  # noqa: E501
        :rtype: int
        """
        return self._games

    @games.setter
    def games(self, games):
        """Sets the games of this TeamSeason.


        :param games: The games of this TeamSeason.  # noqa: E501
        :type: int
        """

        self._games = games

    @property
    def wins(self):
        """Gets the wins of this TeamSeason.  # noqa: E501


        :return: The wins of this TeamSeason.  # noqa: E501
        :rtype: int
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this TeamSeason.


        :param wins: The wins of this TeamSeason.  # noqa: E501
        :type: int
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this TeamSeason.  # noqa: E501


        :return: The losses of this TeamSeason.  # noqa: E501
        :rtype: int
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this TeamSeason.


        :param losses: The losses of this TeamSeason.  # noqa: E501
        :type: int
        """

        self._losses = losses

    @property
    def ties(self):
        """Gets the ties of this TeamSeason.  # noqa: E501


        :return: The ties of this TeamSeason.  # noqa: E501
        :rtype: int
        """
        return self._ties

    @ties.setter
    def ties(self, ties):
        """Sets the ties of this TeamSeason.


        :param ties: The ties of this TeamSeason.  # noqa: E501
        :type: int
        """

        self._ties = ties

    @property
    def preseason_rank(self):
        """Gets the preseason_rank of this TeamSeason.  # noqa: E501

        Rank in the AP preseason poll  # noqa: E501

        :return: The preseason_rank of this TeamSeason.  # noqa: E501
        :rtype: int
        """
        return self._preseason_rank

    @preseason_rank.setter
    def preseason_rank(self, preseason_rank):
        """Sets the preseason_rank of this TeamSeason.

        Rank in the AP preseason poll  # noqa: E501

        :param preseason_rank: The preseason_rank of this TeamSeason.  # noqa: E501
        :type: int
        """

        self._preseason_rank = preseason_rank

    @property
    def postseason_rank(self):
        """Gets the postseason_rank of this TeamSeason.  # noqa: E501

        Final ranking in the AP poll  # noqa: E501

        :return: The postseason_rank of this TeamSeason.  # noqa: E501
        :rtype: int
        """
        return self._postseason_rank

    @postseason_rank.setter
    def postseason_rank(self, postseason_rank):
        """Sets the postseason_rank of this TeamSeason.

        Final ranking in the AP poll  # noqa: E501

        :param postseason_rank: The postseason_rank of this TeamSeason.  # noqa: E501
        :type: int
        """

        self._postseason_rank = postseason_rank

    @property
    def srs(self):
        """Gets the srs of this TeamSeason.  # noqa: E501

        Final SRS rankings  # noqa: E501

        :return: The srs of this TeamSeason.  # noqa: E501
        :rtype: float
        """
        return self._srs

    @srs.setter
    def srs(self, srs):
        """Sets the srs of this TeamSeason.

        Final SRS rankings  # noqa: E501

        :param srs: The srs of this TeamSeason.  # noqa: E501
        :type: float
        """

        self._srs = srs

    @property
    def sp_overall(self):
        """Gets the sp_overall of this TeamSeason.  # noqa: E501

        Final overall SP+ rating  # noqa: E501

        :return: The sp_overall of this TeamSeason.  # noqa: E501
        :rtype: float
        """
        return self._sp_overall

    @sp_overall.setter
    def sp_overall(self, sp_overall):
        """Sets the sp_overall of this TeamSeason.

        Final overall SP+ rating  # noqa: E501

        :param sp_overall: The sp_overall of this TeamSeason.  # noqa: E501
        :type: float
        """

        self._sp_overall = sp_overall

    @property
    def sp_offense(self):
        """Gets the sp_offense of this TeamSeason.  # noqa: E501

        Final SP+ offensive rating  # noqa: E501

        :return: The sp_offense of this TeamSeason.  # noqa: E501
        :rtype: float
        """
        return self._sp_offense

    @sp_offense.setter
    def sp_offense(self, sp_offense):
        """Sets the sp_offense of this TeamSeason.

        Final SP+ offensive rating  # noqa: E501

        :param sp_offense: The sp_offense of this TeamSeason.  # noqa: E501
        :type: float
        """

        self._sp_offense = sp_offense

    @property
    def sp_defense(self):
        """Gets the sp_defense of this TeamSeason.  # noqa: E501

        Final SP+ defensive rating  # noqa: E501

        :return: The sp_defense of this TeamSeason.  # noqa: E501
        :rtype: float
        """
        return self._sp_defense

    @sp_defense.setter
    def sp_defense(self, sp_defense):
        """Sets the sp_defense of this TeamSeason.

        Final SP+ defensive rating  # noqa: E501

        :param sp_defense: The sp_defense of this TeamSeason.  # noqa: E501
        :type: float
        """

        self._sp_defense = sp_defense

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
        if issubclass(TeamSeason, dict):
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
        if not isinstance(other, TeamSeason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
