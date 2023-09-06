# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.4.15
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cfbd.configuration import Configuration


class TeamLocation(object):
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
        'venue_id': 'int',
        'name': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country_code': 'str',
        'timezone': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'elevation': 'float',
        'capacity': 'float',
        'year_constructed': 'float',
        'grass': 'bool',
        'dome': 'bool'
    }

    attribute_map = {
        'venue_id': 'venue_id',
        'name': 'name',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country_code': 'country_code',
        'timezone': 'timezone',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'elevation': 'elevation',
        'capacity': 'capacity',
        'year_constructed': 'year_constructed',
        'grass': 'grass',
        'dome': 'dome'
    }

    def __init__(self, venue_id=None, name=None, city=None, state=None, zip=None, country_code=None, timezone=None, latitude=None, longitude=None, elevation=None, capacity=None, year_constructed=None, grass=None, dome=None, _configuration=None):  # noqa: E501
        """TeamLocation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._venue_id = None
        self._name = None
        self._city = None
        self._state = None
        self._zip = None
        self._country_code = None
        self._timezone = None
        self._latitude = None
        self._longitude = None
        self._elevation = None
        self._capacity = None
        self._year_constructed = None
        self._grass = None
        self._dome = None
        self.discriminator = None

        if venue_id is not None:
            self.venue_id = venue_id
        if name is not None:
            self.name = name
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if country_code is not None:
            self.country_code = country_code
        if timezone is not None:
            self.timezone = timezone
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if elevation is not None:
            self.elevation = elevation
        if capacity is not None:
            self.capacity = capacity
        if year_constructed is not None:
            self.year_constructed = year_constructed
        if grass is not None:
            self.grass = grass
        if dome is not None:
            self.dome = dome

    @property
    def venue_id(self):
        """Gets the venue_id of this TeamLocation.  # noqa: E501


        :return: The venue_id of this TeamLocation.  # noqa: E501
        :rtype: int
        """
        return self._venue_id

    @venue_id.setter
    def venue_id(self, venue_id):
        """Sets the venue_id of this TeamLocation.


        :param venue_id: The venue_id of this TeamLocation.  # noqa: E501
        :type: int
        """

        self._venue_id = venue_id

    @property
    def name(self):
        """Gets the name of this TeamLocation.  # noqa: E501


        :return: The name of this TeamLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TeamLocation.


        :param name: The name of this TeamLocation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def city(self):
        """Gets the city of this TeamLocation.  # noqa: E501


        :return: The city of this TeamLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this TeamLocation.


        :param city: The city of this TeamLocation.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this TeamLocation.  # noqa: E501


        :return: The state of this TeamLocation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TeamLocation.


        :param state: The state of this TeamLocation.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this TeamLocation.  # noqa: E501


        :return: The zip of this TeamLocation.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this TeamLocation.


        :param zip: The zip of this TeamLocation.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country_code(self):
        """Gets the country_code of this TeamLocation.  # noqa: E501


        :return: The country_code of this TeamLocation.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this TeamLocation.


        :param country_code: The country_code of this TeamLocation.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def timezone(self):
        """Gets the timezone of this TeamLocation.  # noqa: E501


        :return: The timezone of this TeamLocation.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this TeamLocation.


        :param timezone: The timezone of this TeamLocation.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def latitude(self):
        """Gets the latitude of this TeamLocation.  # noqa: E501


        :return: The latitude of this TeamLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this TeamLocation.


        :param latitude: The latitude of this TeamLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this TeamLocation.  # noqa: E501


        :return: The longitude of this TeamLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this TeamLocation.


        :param longitude: The longitude of this TeamLocation.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def elevation(self):
        """Gets the elevation of this TeamLocation.  # noqa: E501


        :return: The elevation of this TeamLocation.  # noqa: E501
        :rtype: float
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this TeamLocation.


        :param elevation: The elevation of this TeamLocation.  # noqa: E501
        :type: float
        """

        self._elevation = elevation

    @property
    def capacity(self):
        """Gets the capacity of this TeamLocation.  # noqa: E501


        :return: The capacity of this TeamLocation.  # noqa: E501
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this TeamLocation.


        :param capacity: The capacity of this TeamLocation.  # noqa: E501
        :type: float
        """

        self._capacity = capacity

    @property
    def year_constructed(self):
        """Gets the year_constructed of this TeamLocation.  # noqa: E501


        :return: The year_constructed of this TeamLocation.  # noqa: E501
        :rtype: float
        """
        return self._year_constructed

    @year_constructed.setter
    def year_constructed(self, year_constructed):
        """Sets the year_constructed of this TeamLocation.


        :param year_constructed: The year_constructed of this TeamLocation.  # noqa: E501
        :type: float
        """

        self._year_constructed = year_constructed

    @property
    def grass(self):
        """Gets the grass of this TeamLocation.  # noqa: E501


        :return: The grass of this TeamLocation.  # noqa: E501
        :rtype: bool
        """
        return self._grass

    @grass.setter
    def grass(self, grass):
        """Sets the grass of this TeamLocation.


        :param grass: The grass of this TeamLocation.  # noqa: E501
        :type: bool
        """

        self._grass = grass

    @property
    def dome(self):
        """Gets the dome of this TeamLocation.  # noqa: E501


        :return: The dome of this TeamLocation.  # noqa: E501
        :rtype: bool
        """
        return self._dome

    @dome.setter
    def dome(self, dome):
        """Sets the dome of this TeamLocation.


        :param dome: The dome of this TeamLocation.  # noqa: E501
        :type: bool
        """

        self._dome = dome

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
        if issubclass(TeamLocation, dict):
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
        if not isinstance(other, TeamLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamLocation):
            return True

        return self.to_dict() != other.to_dict()
