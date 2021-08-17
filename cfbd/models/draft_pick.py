# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.1.5
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class DraftPick(object):
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
        'college_athlete_id': 'int',
        'nfl_athlete_id': 'int',
        'college_id': 'int',
        'college_team': 'str',
        'college_conference': 'str',
        'nfl_team': 'str',
        'year': 'int',
        'overall': 'int',
        'round': 'int',
        'pick': 'int',
        'name': 'str',
        'position': 'str',
        'height': 'int',
        'weight': 'int',
        'pre_draft_ranking': 'int',
        'pre_draft_position_ranking': 'int',
        'pre_draft_grade': 'int',
        'hometown_info': 'object'
    }

    attribute_map = {
        'college_athlete_id': 'collegeAthleteId',
        'nfl_athlete_id': 'nflAthleteId',
        'college_id': 'collegeId',
        'college_team': 'collegeTeam',
        'college_conference': 'collegeConference',
        'nfl_team': 'nflTeam',
        'year': 'year',
        'overall': 'overall',
        'round': 'round',
        'pick': 'pick',
        'name': 'name',
        'position': 'position',
        'height': 'height',
        'weight': 'weight',
        'pre_draft_ranking': 'preDraftRanking',
        'pre_draft_position_ranking': 'preDraftPositionRanking',
        'pre_draft_grade': 'preDraftGrade',
        'hometown_info': 'hometownInfo'
    }

    def __init__(self, college_athlete_id=None, nfl_athlete_id=None, college_id=None, college_team=None, college_conference=None, nfl_team=None, year=None, overall=None, round=None, pick=None, name=None, position=None, height=None, weight=None, pre_draft_ranking=None, pre_draft_position_ranking=None, pre_draft_grade=None, hometown_info=None, _configuration=None):  # noqa: E501
        """DraftPick - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._college_athlete_id = None
        self._nfl_athlete_id = None
        self._college_id = None
        self._college_team = None
        self._college_conference = None
        self._nfl_team = None
        self._year = None
        self._overall = None
        self._round = None
        self._pick = None
        self._name = None
        self._position = None
        self._height = None
        self._weight = None
        self._pre_draft_ranking = None
        self._pre_draft_position_ranking = None
        self._pre_draft_grade = None
        self._hometown_info = None
        self.discriminator = None

        if college_athlete_id is not None:
            self.college_athlete_id = college_athlete_id
        if nfl_athlete_id is not None:
            self.nfl_athlete_id = nfl_athlete_id
        if college_id is not None:
            self.college_id = college_id
        if college_team is not None:
            self.college_team = college_team
        if college_conference is not None:
            self.college_conference = college_conference
        if nfl_team is not None:
            self.nfl_team = nfl_team
        if year is not None:
            self.year = year
        if overall is not None:
            self.overall = overall
        if round is not None:
            self.round = round
        if pick is not None:
            self.pick = pick
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if height is not None:
            self.height = height
        if weight is not None:
            self.weight = weight
        if pre_draft_ranking is not None:
            self.pre_draft_ranking = pre_draft_ranking
        if pre_draft_position_ranking is not None:
            self.pre_draft_position_ranking = pre_draft_position_ranking
        if pre_draft_grade is not None:
            self.pre_draft_grade = pre_draft_grade
        if hometown_info is not None:
            self.hometown_info = hometown_info

    @property
    def college_athlete_id(self):
        """Gets the college_athlete_id of this DraftPick.  # noqa: E501


        :return: The college_athlete_id of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._college_athlete_id

    @college_athlete_id.setter
    def college_athlete_id(self, college_athlete_id):
        """Sets the college_athlete_id of this DraftPick.


        :param college_athlete_id: The college_athlete_id of this DraftPick.  # noqa: E501
        :type: int
        """

        self._college_athlete_id = college_athlete_id

    @property
    def nfl_athlete_id(self):
        """Gets the nfl_athlete_id of this DraftPick.  # noqa: E501


        :return: The nfl_athlete_id of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._nfl_athlete_id

    @nfl_athlete_id.setter
    def nfl_athlete_id(self, nfl_athlete_id):
        """Sets the nfl_athlete_id of this DraftPick.


        :param nfl_athlete_id: The nfl_athlete_id of this DraftPick.  # noqa: E501
        :type: int
        """

        self._nfl_athlete_id = nfl_athlete_id

    @property
    def college_id(self):
        """Gets the college_id of this DraftPick.  # noqa: E501


        :return: The college_id of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._college_id

    @college_id.setter
    def college_id(self, college_id):
        """Sets the college_id of this DraftPick.


        :param college_id: The college_id of this DraftPick.  # noqa: E501
        :type: int
        """

        self._college_id = college_id

    @property
    def college_team(self):
        """Gets the college_team of this DraftPick.  # noqa: E501


        :return: The college_team of this DraftPick.  # noqa: E501
        :rtype: str
        """
        return self._college_team

    @college_team.setter
    def college_team(self, college_team):
        """Sets the college_team of this DraftPick.


        :param college_team: The college_team of this DraftPick.  # noqa: E501
        :type: str
        """

        self._college_team = college_team

    @property
    def college_conference(self):
        """Gets the college_conference of this DraftPick.  # noqa: E501


        :return: The college_conference of this DraftPick.  # noqa: E501
        :rtype: str
        """
        return self._college_conference

    @college_conference.setter
    def college_conference(self, college_conference):
        """Sets the college_conference of this DraftPick.


        :param college_conference: The college_conference of this DraftPick.  # noqa: E501
        :type: str
        """

        self._college_conference = college_conference

    @property
    def nfl_team(self):
        """Gets the nfl_team of this DraftPick.  # noqa: E501


        :return: The nfl_team of this DraftPick.  # noqa: E501
        :rtype: str
        """
        return self._nfl_team

    @nfl_team.setter
    def nfl_team(self, nfl_team):
        """Sets the nfl_team of this DraftPick.


        :param nfl_team: The nfl_team of this DraftPick.  # noqa: E501
        :type: str
        """

        self._nfl_team = nfl_team

    @property
    def year(self):
        """Gets the year of this DraftPick.  # noqa: E501


        :return: The year of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this DraftPick.


        :param year: The year of this DraftPick.  # noqa: E501
        :type: int
        """

        self._year = year

    @property
    def overall(self):
        """Gets the overall of this DraftPick.  # noqa: E501


        :return: The overall of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this DraftPick.


        :param overall: The overall of this DraftPick.  # noqa: E501
        :type: int
        """

        self._overall = overall

    @property
    def round(self):
        """Gets the round of this DraftPick.  # noqa: E501


        :return: The round of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._round

    @round.setter
    def round(self, round):
        """Sets the round of this DraftPick.


        :param round: The round of this DraftPick.  # noqa: E501
        :type: int
        """

        self._round = round

    @property
    def pick(self):
        """Gets the pick of this DraftPick.  # noqa: E501


        :return: The pick of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._pick

    @pick.setter
    def pick(self, pick):
        """Sets the pick of this DraftPick.


        :param pick: The pick of this DraftPick.  # noqa: E501
        :type: int
        """

        self._pick = pick

    @property
    def name(self):
        """Gets the name of this DraftPick.  # noqa: E501


        :return: The name of this DraftPick.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DraftPick.


        :param name: The name of this DraftPick.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def position(self):
        """Gets the position of this DraftPick.  # noqa: E501


        :return: The position of this DraftPick.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DraftPick.


        :param position: The position of this DraftPick.  # noqa: E501
        :type: str
        """

        self._position = position

    @property
    def height(self):
        """Gets the height of this DraftPick.  # noqa: E501


        :return: The height of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this DraftPick.


        :param height: The height of this DraftPick.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this DraftPick.  # noqa: E501


        :return: The weight of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this DraftPick.


        :param weight: The weight of this DraftPick.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def pre_draft_ranking(self):
        """Gets the pre_draft_ranking of this DraftPick.  # noqa: E501


        :return: The pre_draft_ranking of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._pre_draft_ranking

    @pre_draft_ranking.setter
    def pre_draft_ranking(self, pre_draft_ranking):
        """Sets the pre_draft_ranking of this DraftPick.


        :param pre_draft_ranking: The pre_draft_ranking of this DraftPick.  # noqa: E501
        :type: int
        """

        self._pre_draft_ranking = pre_draft_ranking

    @property
    def pre_draft_position_ranking(self):
        """Gets the pre_draft_position_ranking of this DraftPick.  # noqa: E501


        :return: The pre_draft_position_ranking of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._pre_draft_position_ranking

    @pre_draft_position_ranking.setter
    def pre_draft_position_ranking(self, pre_draft_position_ranking):
        """Sets the pre_draft_position_ranking of this DraftPick.


        :param pre_draft_position_ranking: The pre_draft_position_ranking of this DraftPick.  # noqa: E501
        :type: int
        """

        self._pre_draft_position_ranking = pre_draft_position_ranking

    @property
    def pre_draft_grade(self):
        """Gets the pre_draft_grade of this DraftPick.  # noqa: E501


        :return: The pre_draft_grade of this DraftPick.  # noqa: E501
        :rtype: int
        """
        return self._pre_draft_grade

    @pre_draft_grade.setter
    def pre_draft_grade(self, pre_draft_grade):
        """Sets the pre_draft_grade of this DraftPick.


        :param pre_draft_grade: The pre_draft_grade of this DraftPick.  # noqa: E501
        :type: int
        """

        self._pre_draft_grade = pre_draft_grade

    @property
    def hometown_info(self):
        """Gets the hometown_info of this DraftPick.  # noqa: E501


        :return: The hometown_info of this DraftPick.  # noqa: E501
        :rtype: object
        """
        return self._hometown_info

    @hometown_info.setter
    def hometown_info(self, hometown_info):
        """Sets the hometown_info of this DraftPick.


        :param hometown_info: The hometown_info of this DraftPick.  # noqa: E501
        :type: object
        """

        self._hometown_info = hometown_info

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
        if issubclass(DraftPick, dict):
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
        if not isinstance(other, DraftPick):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DraftPick):
            return True

        return self.to_dict() != other.to_dict()
