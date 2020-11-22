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


class Play(object):
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
        'drive_id': 'int',
        'game_id': 'int',
        'drive_number': 'int',
        'play_number': 'int',
        'offense': 'str',
        'offense_conference': 'str',
        'offense_score': 'int',
        'defense': 'str',
        'home': 'str',
        'away': 'str',
        'defense_conference': 'str',
        'defense_score': 'int',
        'period': 'int',
        'clock': 'DriveStartTime',
        'offense_timeouts': 'int',
        'defense_timeouts': 'int',
        'yard_line': 'int',
        'yards_to_goal': 'int',
        'down': 'int',
        'distance': 'int',
        'yards_gained': 'int',
        'scoring': 'bool',
        'play_type': 'str',
        'play_text': 'str',
        'ppa': 'float'
    }

    attribute_map = {
        'id': 'id',
        'drive_id': 'drive_id',
        'game_id': 'game_id',
        'drive_number': 'drive_number',
        'play_number': 'play_number',
        'offense': 'offense',
        'offense_conference': 'offense_conference',
        'offense_score': 'offense_score',
        'defense': 'defense',
        'home': 'home',
        'away': 'away',
        'defense_conference': 'defense_conference',
        'defense_score': 'defense_score',
        'period': 'period',
        'clock': 'clock',
        'offense_timeouts': 'offense_timeouts',
        'defense_timeouts': 'defense_timeouts',
        'yard_line': 'yard_line',
        'yards_to_goal': 'yards_to_goal',
        'down': 'down',
        'distance': 'distance',
        'yards_gained': 'yards_gained',
        'scoring': 'scoring',
        'play_type': 'play_type',
        'play_text': 'play_text',
        'ppa': 'ppa'
    }

    def __init__(self, id=None, drive_id=None, game_id=None, drive_number=None, play_number=None, offense=None, offense_conference=None, offense_score=None, defense=None, home=None, away=None, defense_conference=None, defense_score=None, period=None, clock=None, offense_timeouts=None, defense_timeouts=None, yard_line=None, yards_to_goal=None, down=None, distance=None, yards_gained=None, scoring=None, play_type=None, play_text=None, ppa=None):  # noqa: E501
        """Play - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._drive_id = None
        self._game_id = None
        self._drive_number = None
        self._play_number = None
        self._offense = None
        self._offense_conference = None
        self._offense_score = None
        self._defense = None
        self._home = None
        self._away = None
        self._defense_conference = None
        self._defense_score = None
        self._period = None
        self._clock = None
        self._offense_timeouts = None
        self._defense_timeouts = None
        self._yard_line = None
        self._yards_to_goal = None
        self._down = None
        self._distance = None
        self._yards_gained = None
        self._scoring = None
        self._play_type = None
        self._play_text = None
        self._ppa = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if drive_id is not None:
            self.drive_id = drive_id
        if game_id is not None:
            self.game_id = game_id
        if drive_number is not None:
            self.drive_number = drive_number
        if play_number is not None:
            self.play_number = play_number
        if offense is not None:
            self.offense = offense
        if offense_conference is not None:
            self.offense_conference = offense_conference
        if offense_score is not None:
            self.offense_score = offense_score
        if defense is not None:
            self.defense = defense
        if home is not None:
            self.home = home
        if away is not None:
            self.away = away
        if defense_conference is not None:
            self.defense_conference = defense_conference
        if defense_score is not None:
            self.defense_score = defense_score
        if period is not None:
            self.period = period
        if clock is not None:
            self.clock = clock
        if offense_timeouts is not None:
            self.offense_timeouts = offense_timeouts
        if defense_timeouts is not None:
            self.defense_timeouts = defense_timeouts
        if yard_line is not None:
            self.yard_line = yard_line
        if yards_to_goal is not None:
            self.yards_to_goal = yards_to_goal
        if down is not None:
            self.down = down
        if distance is not None:
            self.distance = distance
        if yards_gained is not None:
            self.yards_gained = yards_gained
        if scoring is not None:
            self.scoring = scoring
        if play_type is not None:
            self.play_type = play_type
        if play_text is not None:
            self.play_text = play_text
        if ppa is not None:
            self.ppa = ppa

    @property
    def id(self):
        """Gets the id of this Play.  # noqa: E501


        :return: The id of this Play.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Play.


        :param id: The id of this Play.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def drive_id(self):
        """Gets the drive_id of this Play.  # noqa: E501


        :return: The drive_id of this Play.  # noqa: E501
        :rtype: int
        """
        return self._drive_id

    @drive_id.setter
    def drive_id(self, drive_id):
        """Sets the drive_id of this Play.


        :param drive_id: The drive_id of this Play.  # noqa: E501
        :type: int
        """

        self._drive_id = drive_id

    @property
    def game_id(self):
        """Gets the game_id of this Play.  # noqa: E501


        :return: The game_id of this Play.  # noqa: E501
        :rtype: int
        """
        return self._game_id

    @game_id.setter
    def game_id(self, game_id):
        """Sets the game_id of this Play.


        :param game_id: The game_id of this Play.  # noqa: E501
        :type: int
        """

        self._game_id = game_id

    @property
    def drive_number(self):
        """Gets the drive_number of this Play.  # noqa: E501


        :return: The drive_number of this Play.  # noqa: E501
        :rtype: int
        """
        return self._drive_number

    @drive_number.setter
    def drive_number(self, drive_number):
        """Sets the drive_number of this Play.


        :param drive_number: The drive_number of this Play.  # noqa: E501
        :type: int
        """

        self._drive_number = drive_number

    @property
    def play_number(self):
        """Gets the play_number of this Play.  # noqa: E501


        :return: The play_number of this Play.  # noqa: E501
        :rtype: int
        """
        return self._play_number

    @play_number.setter
    def play_number(self, play_number):
        """Sets the play_number of this Play.


        :param play_number: The play_number of this Play.  # noqa: E501
        :type: int
        """

        self._play_number = play_number

    @property
    def offense(self):
        """Gets the offense of this Play.  # noqa: E501


        :return: The offense of this Play.  # noqa: E501
        :rtype: str
        """
        return self._offense

    @offense.setter
    def offense(self, offense):
        """Sets the offense of this Play.


        :param offense: The offense of this Play.  # noqa: E501
        :type: str
        """

        self._offense = offense

    @property
    def offense_conference(self):
        """Gets the offense_conference of this Play.  # noqa: E501


        :return: The offense_conference of this Play.  # noqa: E501
        :rtype: str
        """
        return self._offense_conference

    @offense_conference.setter
    def offense_conference(self, offense_conference):
        """Sets the offense_conference of this Play.


        :param offense_conference: The offense_conference of this Play.  # noqa: E501
        :type: str
        """

        self._offense_conference = offense_conference

    @property
    def offense_score(self):
        """Gets the offense_score of this Play.  # noqa: E501


        :return: The offense_score of this Play.  # noqa: E501
        :rtype: int
        """
        return self._offense_score

    @offense_score.setter
    def offense_score(self, offense_score):
        """Sets the offense_score of this Play.


        :param offense_score: The offense_score of this Play.  # noqa: E501
        :type: int
        """

        self._offense_score = offense_score

    @property
    def defense(self):
        """Gets the defense of this Play.  # noqa: E501


        :return: The defense of this Play.  # noqa: E501
        :rtype: str
        """
        return self._defense

    @defense.setter
    def defense(self, defense):
        """Sets the defense of this Play.


        :param defense: The defense of this Play.  # noqa: E501
        :type: str
        """

        self._defense = defense

    @property
    def home(self):
        """Gets the home of this Play.  # noqa: E501


        :return: The home of this Play.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this Play.


        :param home: The home of this Play.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def away(self):
        """Gets the away of this Play.  # noqa: E501


        :return: The away of this Play.  # noqa: E501
        :rtype: str
        """
        return self._away

    @away.setter
    def away(self, away):
        """Sets the away of this Play.


        :param away: The away of this Play.  # noqa: E501
        :type: str
        """

        self._away = away

    @property
    def defense_conference(self):
        """Gets the defense_conference of this Play.  # noqa: E501


        :return: The defense_conference of this Play.  # noqa: E501
        :rtype: str
        """
        return self._defense_conference

    @defense_conference.setter
    def defense_conference(self, defense_conference):
        """Sets the defense_conference of this Play.


        :param defense_conference: The defense_conference of this Play.  # noqa: E501
        :type: str
        """

        self._defense_conference = defense_conference

    @property
    def defense_score(self):
        """Gets the defense_score of this Play.  # noqa: E501


        :return: The defense_score of this Play.  # noqa: E501
        :rtype: int
        """
        return self._defense_score

    @defense_score.setter
    def defense_score(self, defense_score):
        """Sets the defense_score of this Play.


        :param defense_score: The defense_score of this Play.  # noqa: E501
        :type: int
        """

        self._defense_score = defense_score

    @property
    def period(self):
        """Gets the period of this Play.  # noqa: E501


        :return: The period of this Play.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Play.


        :param period: The period of this Play.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def clock(self):
        """Gets the clock of this Play.  # noqa: E501


        :return: The clock of this Play.  # noqa: E501
        :rtype: DriveStartTime
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """Sets the clock of this Play.


        :param clock: The clock of this Play.  # noqa: E501
        :type: DriveStartTime
        """

        self._clock = clock

    @property
    def offense_timeouts(self):
        """Gets the offense_timeouts of this Play.  # noqa: E501


        :return: The offense_timeouts of this Play.  # noqa: E501
        :rtype: int
        """
        return self._offense_timeouts

    @offense_timeouts.setter
    def offense_timeouts(self, offense_timeouts):
        """Sets the offense_timeouts of this Play.


        :param offense_timeouts: The offense_timeouts of this Play.  # noqa: E501
        :type: int
        """

        self._offense_timeouts = offense_timeouts

    @property
    def defense_timeouts(self):
        """Gets the defense_timeouts of this Play.  # noqa: E501


        :return: The defense_timeouts of this Play.  # noqa: E501
        :rtype: int
        """
        return self._defense_timeouts

    @defense_timeouts.setter
    def defense_timeouts(self, defense_timeouts):
        """Sets the defense_timeouts of this Play.


        :param defense_timeouts: The defense_timeouts of this Play.  # noqa: E501
        :type: int
        """

        self._defense_timeouts = defense_timeouts

    @property
    def yard_line(self):
        """Gets the yard_line of this Play.  # noqa: E501


        :return: The yard_line of this Play.  # noqa: E501
        :rtype: int
        """
        return self._yard_line

    @yard_line.setter
    def yard_line(self, yard_line):
        """Sets the yard_line of this Play.


        :param yard_line: The yard_line of this Play.  # noqa: E501
        :type: int
        """

        self._yard_line = yard_line

    @property
    def yards_to_goal(self):
        """Gets the yards_to_goal of this Play.  # noqa: E501


        :return: The yards_to_goal of this Play.  # noqa: E501
        :rtype: int
        """
        return self._yards_to_goal

    @yards_to_goal.setter
    def yards_to_goal(self, yards_to_goal):
        """Sets the yards_to_goal of this Play.


        :param yards_to_goal: The yards_to_goal of this Play.  # noqa: E501
        :type: int
        """

        self._yards_to_goal = yards_to_goal

    @property
    def down(self):
        """Gets the down of this Play.  # noqa: E501


        :return: The down of this Play.  # noqa: E501
        :rtype: int
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this Play.


        :param down: The down of this Play.  # noqa: E501
        :type: int
        """

        self._down = down

    @property
    def distance(self):
        """Gets the distance of this Play.  # noqa: E501


        :return: The distance of this Play.  # noqa: E501
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Play.


        :param distance: The distance of this Play.  # noqa: E501
        :type: int
        """

        self._distance = distance

    @property
    def yards_gained(self):
        """Gets the yards_gained of this Play.  # noqa: E501


        :return: The yards_gained of this Play.  # noqa: E501
        :rtype: int
        """
        return self._yards_gained

    @yards_gained.setter
    def yards_gained(self, yards_gained):
        """Sets the yards_gained of this Play.


        :param yards_gained: The yards_gained of this Play.  # noqa: E501
        :type: int
        """

        self._yards_gained = yards_gained

    @property
    def scoring(self):
        """Gets the scoring of this Play.  # noqa: E501


        :return: The scoring of this Play.  # noqa: E501
        :rtype: bool
        """
        return self._scoring

    @scoring.setter
    def scoring(self, scoring):
        """Sets the scoring of this Play.


        :param scoring: The scoring of this Play.  # noqa: E501
        :type: bool
        """

        self._scoring = scoring

    @property
    def play_type(self):
        """Gets the play_type of this Play.  # noqa: E501


        :return: The play_type of this Play.  # noqa: E501
        :rtype: str
        """
        return self._play_type

    @play_type.setter
    def play_type(self, play_type):
        """Sets the play_type of this Play.


        :param play_type: The play_type of this Play.  # noqa: E501
        :type: str
        """

        self._play_type = play_type

    @property
    def play_text(self):
        """Gets the play_text of this Play.  # noqa: E501


        :return: The play_text of this Play.  # noqa: E501
        :rtype: str
        """
        return self._play_text

    @play_text.setter
    def play_text(self, play_text):
        """Sets the play_text of this Play.


        :param play_text: The play_text of this Play.  # noqa: E501
        :type: str
        """

        self._play_text = play_text

    @property
    def ppa(self):
        """Gets the ppa of this Play.  # noqa: E501


        :return: The ppa of this Play.  # noqa: E501
        :rtype: float
        """
        return self._ppa

    @ppa.setter
    def ppa(self, ppa):
        """Sets the ppa of this Play.


        :param ppa: The ppa of this Play.  # noqa: E501
        :type: float
        """

        self._ppa = ppa

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
        if issubclass(Play, dict):
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
        if not isinstance(other, Play):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
