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


class DraftPickHometownInfo(object):
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
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'country_fips': 'int'
    }

    attribute_map = {
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'country_fips': 'countryFips'
    }

    def __init__(self, city=None, state=None, country=None, latitude=None, longitude=None, country_fips=None, _configuration=None):  # noqa: E501
        """DraftPickHometownInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._city = None
        self._state = None
        self._country = None
        self._latitude = None
        self._longitude = None
        self._country_fips = None
        self.discriminator = None

        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if country_fips is not None:
            self.country_fips = country_fips

    @property
    def city(self):
        """Gets the city of this DraftPickHometownInfo.  # noqa: E501


        :return: The city of this DraftPickHometownInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this DraftPickHometownInfo.


        :param city: The city of this DraftPickHometownInfo.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this DraftPickHometownInfo.  # noqa: E501


        :return: The state of this DraftPickHometownInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DraftPickHometownInfo.


        :param state: The state of this DraftPickHometownInfo.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this DraftPickHometownInfo.  # noqa: E501


        :return: The country of this DraftPickHometownInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this DraftPickHometownInfo.


        :param country: The country of this DraftPickHometownInfo.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def latitude(self):
        """Gets the latitude of this DraftPickHometownInfo.  # noqa: E501


        :return: The latitude of this DraftPickHometownInfo.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this DraftPickHometownInfo.


        :param latitude: The latitude of this DraftPickHometownInfo.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this DraftPickHometownInfo.  # noqa: E501


        :return: The longitude of this DraftPickHometownInfo.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this DraftPickHometownInfo.


        :param longitude: The longitude of this DraftPickHometownInfo.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def country_fips(self):
        """Gets the country_fips of this DraftPickHometownInfo.  # noqa: E501


        :return: The country_fips of this DraftPickHometownInfo.  # noqa: E501
        :rtype: int
        """
        return self._country_fips

    @country_fips.setter
    def country_fips(self, country_fips):
        """Sets the country_fips of this DraftPickHometownInfo.


        :param country_fips: The country_fips of this DraftPickHometownInfo.  # noqa: E501
        :type: int
        """

        self._country_fips = country_fips

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
        if issubclass(DraftPickHometownInfo, dict):
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
        if not isinstance(other, DraftPickHometownInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DraftPickHometownInfo):
            return True

        return self.to_dict() != other.to_dict()
