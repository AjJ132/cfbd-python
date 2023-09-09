# coding: utf-8

"""
    College Football Data API

    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \"Bearer \" prepended (e.g. \"Bearer your_key\"). API keys can be acquired from the CollegeFootballData.com website.  # noqa: E501

    OpenAPI spec version: 4.5.0
    Contact: admin@collegefootballdata.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cfbd.api_client import ApiClient


class PlayersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_player_season_stats(self, year, **kwargs):  # noqa: E501
        """Player stats by season  # noqa: E501

        Season player stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_season_stats(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param int start_week: Start week filter
        :param int end_week: Start week filter
        :param str season_type: Season type filter (regular, postseason, or both)
        :param str category: Stat category filter (e.g. passing)
        :return: list[PlayerSeasonStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_season_stats_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_season_stats_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_player_season_stats_with_http_info(self, year, **kwargs):  # noqa: E501
        """Player stats by season  # noqa: E501

        Season player stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_season_stats_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param int start_week: Start week filter
        :param int end_week: Start week filter
        :param str season_type: Season type filter (regular, postseason, or both)
        :param str category: Stat category filter (e.g. passing)
        :return: list[PlayerSeasonStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference', 'start_week', 'end_week', 'season_type', 'category']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_season_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `get_player_season_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'start_week' in params:
            query_params.append(('startWeek', params['start_week']))  # noqa: E501
        if 'end_week' in params:
            query_params.append(('endWeek', params['end_week']))  # noqa: E501
        if 'season_type' in params:
            query_params.append(('seasonType', params['season_type']))  # noqa: E501
        if 'category' in params:
            query_params.append(('category', params['category']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stats/player/season', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayerSeasonStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_usage(self, year, **kwargs):  # noqa: E501
        """Player usage metrics broken down by season  # noqa: E501

        Player usage metrics by season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_usage(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param str position: Position abbreviation filter
        :param int player_id: Player id filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :return: list[PlayerUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_usage_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_usage_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_player_usage_with_http_info(self, year, **kwargs):  # noqa: E501
        """Player usage metrics broken down by season  # noqa: E501

        Player usage metrics by season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_usage_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :param str position: Position abbreviation filter
        :param int player_id: Player id filter
        :param bool exclude_garbage_time: Filter to remove garbage time plays from calculations
        :return: list[PlayerUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference', 'position', 'player_id', 'exclude_garbage_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_usage" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `get_player_usage`")  # noqa: E501

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2013):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_player_usage`, must be a value greater than or equal to `2013`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501
        if 'position' in params:
            query_params.append(('position', params['position']))  # noqa: E501
        if 'player_id' in params:
            query_params.append(('playerId', params['player_id']))  # noqa: E501
        if 'exclude_garbage_time' in params:
            query_params.append(('excludeGarbageTime', params['exclude_garbage_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/player/usage', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayerUsage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_returning_production(self, **kwargs):  # noqa: E501
        """Team returning production metrics  # noqa: E501

        Returning production metrics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_returning_production(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :return: list[ReturningProduction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_returning_production_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_returning_production_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_returning_production_with_http_info(self, **kwargs):  # noqa: E501
        """Team returning production metrics  # noqa: E501

        Returning production metrics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_returning_production_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter
        :param str team: Team filter
        :param str conference: Conference abbreviation filter
        :return: list[ReturningProduction]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year', 'team', 'conference']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_returning_production" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2014):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `get_returning_production`, must be a value greater than or equal to `2014`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'conference' in params:
            query_params.append(('conference', params['conference']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/player/returning', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ReturningProduction]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transfer_portal(self, year, **kwargs):  # noqa: E501
        """Transfer portal by season  # noqa: E501

        Transfer portal by season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transfer_portal(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :return: list[PortalPlayer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_transfer_portal_with_http_info(year, **kwargs)  # noqa: E501
        else:
            (data) = self.get_transfer_portal_with_http_info(year, **kwargs)  # noqa: E501
            return data

    def get_transfer_portal_with_http_info(self, year, **kwargs):  # noqa: E501
        """Transfer portal by season  # noqa: E501

        Transfer portal by season  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transfer_portal_with_http_info(year, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int year: Year filter (required)
        :return: list[PortalPlayer]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transfer_portal" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'year' is set
        if self.api_client.client_side_validation and ('year' not in params or
                                                       params['year'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `year` when calling `get_transfer_portal`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/player/portal', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortalPlayer]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def player_search(self, search_term, **kwargs):  # noqa: E501
        """Search for player information  # noqa: E501

        Search for players  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.player_search(search_term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_term: Term to search on (required)
        :param str position: Position abbreviation filter
        :param str team: Team filter
        :param int year: Year filter
        :return: list[PlayerSearchResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.player_search_with_http_info(search_term, **kwargs)  # noqa: E501
        else:
            (data) = self.player_search_with_http_info(search_term, **kwargs)  # noqa: E501
            return data

    def player_search_with_http_info(self, search_term, **kwargs):  # noqa: E501
        """Search for player information  # noqa: E501

        Search for players  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.player_search_with_http_info(search_term, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_term: Term to search on (required)
        :param str position: Position abbreviation filter
        :param str team: Team filter
        :param int year: Year filter
        :return: list[PlayerSearchResult]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_term', 'position', 'team', 'year']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method player_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'search_term' is set
        if self.api_client.client_side_validation and ('search_term' not in params or
                                                       params['search_term'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `search_term` when calling `player_search`")  # noqa: E501

        if self.api_client.client_side_validation and ('year' in params and params['year'] < 2001):  # noqa: E501
            raise ValueError("Invalid value for parameter `year` when calling `player_search`, must be a value greater than or equal to `2001`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'search_term' in params:
            query_params.append(('searchTerm', params['search_term']))  # noqa: E501
        if 'position' in params:
            query_params.append(('position', params['position']))  # noqa: E501
        if 'team' in params:
            query_params.append(('team', params['team']))  # noqa: E501
        if 'year' in params:
            query_params.append(('year', params['year']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/player/search', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PlayerSearchResult]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
