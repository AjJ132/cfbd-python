# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.21
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from cfbd.models.aggregated_team_recruiting import AggregatedTeamRecruiting
from cfbd.models.recruit import Recruit
from cfbd.models.recruit_classification import RecruitClassification
from cfbd.models.team_recruiting_ranking import TeamRecruitingRanking

from cfbd.api_client import ApiClient
from cfbd.api_response import ApiResponse
from cfbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RecruitingApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_aggregated_team_recruiting_ratings(self, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, recruit_type : Annotated[Optional[RecruitClassification], Field(description="Optional recruit type filter, defaults to HighSchool")] = None, start_year : Annotated[Optional[StrictInt], Field(description="Optional start year range, defaults to 2000")] = None, end_year : Annotated[Optional[StrictInt], Field(description="Optional end year range, defaults to current year")] = None, **kwargs) -> List[AggregatedTeamRecruiting]:  # noqa: E501
        """get_aggregated_team_recruiting_ratings  # noqa: E501

        Retrieves aggregated recruiting statistics by team and position grouping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_aggregated_team_recruiting_ratings(team, conference, recruit_type, start_year, end_year, async_req=True)
        >>> result = thread.get()

        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference filter
        :type conference: str
        :param recruit_type: Optional recruit type filter, defaults to HighSchool
        :type recruit_type: RecruitClassification
        :param start_year: Optional start year range, defaults to 2000
        :type start_year: int
        :param end_year: Optional end year range, defaults to current year
        :type end_year: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[AggregatedTeamRecruiting]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_aggregated_team_recruiting_ratings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_aggregated_team_recruiting_ratings_with_http_info(team, conference, recruit_type, start_year, end_year, **kwargs)  # noqa: E501

    @validate_arguments
    def get_aggregated_team_recruiting_ratings_with_http_info(self, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, conference : Annotated[Optional[StrictStr], Field(description="Optional conference filter")] = None, recruit_type : Annotated[Optional[RecruitClassification], Field(description="Optional recruit type filter, defaults to HighSchool")] = None, start_year : Annotated[Optional[StrictInt], Field(description="Optional start year range, defaults to 2000")] = None, end_year : Annotated[Optional[StrictInt], Field(description="Optional end year range, defaults to current year")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_aggregated_team_recruiting_ratings  # noqa: E501

        Retrieves aggregated recruiting statistics by team and position grouping  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_aggregated_team_recruiting_ratings_with_http_info(team, conference, recruit_type, start_year, end_year, async_req=True)
        >>> result = thread.get()

        :param team: Optional team filter
        :type team: str
        :param conference: Optional conference filter
        :type conference: str
        :param recruit_type: Optional recruit type filter, defaults to HighSchool
        :type recruit_type: RecruitClassification
        :param start_year: Optional start year range, defaults to 2000
        :type start_year: int
        :param end_year: Optional end year range, defaults to current year
        :type end_year: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[AggregatedTeamRecruiting], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'team',
            'conference',
            'recruit_type',
            'start_year',
            'end_year'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_aggregated_team_recruiting_ratings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('conference') is not None:  # noqa: E501
            _query_params.append(('conference', _params['conference']))

        if _params.get('recruit_type') is not None:  # noqa: E501
            _query_params.append(('recruitType', _params['recruit_type'].value))

        if _params.get('start_year') is not None:  # noqa: E501
            _query_params.append(('startYear', _params['start_year']))

        if _params.get('end_year') is not None:  # noqa: E501
            _query_params.append(('endYear', _params['end_year']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey']  # noqa: E501

        _response_types_map = {
            '200': "List[AggregatedTeamRecruiting]",
        }

        return self.api_client.call_api(
            '/recruiting/groups', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_recruits(self, year : Annotated[Optional[StrictInt], Field(description="Year filter, required when no team specified")] = None, team : Annotated[Optional[StrictStr], Field(description="Team filter, required when no team specified")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position categorization filter")] = None, state : Annotated[Optional[StrictStr], Field(description="Optional state/province filter")] = None, classification : Annotated[Optional[RecruitClassification], Field(description="Optional recruit type classification filter, defaults to HighSchool")] = None, **kwargs) -> List[Recruit]:  # noqa: E501
        """get_recruits  # noqa: E501

        Retrieves player recruiting rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recruits(year, team, position, state, classification, async_req=True)
        >>> result = thread.get()

        :param year: Year filter, required when no team specified
        :type year: int
        :param team: Team filter, required when no team specified
        :type team: str
        :param position: Optional position categorization filter
        :type position: str
        :param state: Optional state/province filter
        :type state: str
        :param classification: Optional recruit type classification filter, defaults to HighSchool
        :type classification: RecruitClassification
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[Recruit]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_recruits_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_recruits_with_http_info(year, team, position, state, classification, **kwargs)  # noqa: E501

    @validate_arguments
    def get_recruits_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Year filter, required when no team specified")] = None, team : Annotated[Optional[StrictStr], Field(description="Team filter, required when no team specified")] = None, position : Annotated[Optional[StrictStr], Field(description="Optional position categorization filter")] = None, state : Annotated[Optional[StrictStr], Field(description="Optional state/province filter")] = None, classification : Annotated[Optional[RecruitClassification], Field(description="Optional recruit type classification filter, defaults to HighSchool")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_recruits  # noqa: E501

        Retrieves player recruiting rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_recruits_with_http_info(year, team, position, state, classification, async_req=True)
        >>> result = thread.get()

        :param year: Year filter, required when no team specified
        :type year: int
        :param team: Team filter, required when no team specified
        :type team: str
        :param position: Optional position categorization filter
        :type position: str
        :param state: Optional state/province filter
        :type state: str
        :param classification: Optional recruit type classification filter, defaults to HighSchool
        :type classification: RecruitClassification
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[Recruit], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'team',
            'position',
            'state',
            'classification'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_recruits" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('year') is not None:  # noqa: E501
            _query_params.append(('year', _params['year']))

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        if _params.get('position') is not None:  # noqa: E501
            _query_params.append(('position', _params['position']))

        if _params.get('state') is not None:  # noqa: E501
            _query_params.append(('state', _params['state']))

        if _params.get('classification') is not None:  # noqa: E501
            _query_params.append(('classification', _params['classification'].value))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey']  # noqa: E501

        _response_types_map = {
            '200': "List[Recruit]",
        }

        return self.api_client.call_api(
            '/recruiting/players', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_team_recruiting_rankings(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, **kwargs) -> List[TeamRecruitingRanking]:  # noqa: E501
        """get_team_recruiting_rankings  # noqa: E501

        Retrieves team recruiting rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_recruiting_rankings(year, team, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[TeamRecruitingRanking]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_team_recruiting_rankings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_team_recruiting_rankings_with_http_info(year, team, **kwargs)  # noqa: E501

    @validate_arguments
    def get_team_recruiting_rankings_with_http_info(self, year : Annotated[Optional[StrictInt], Field(description="Optional year filter")] = None, team : Annotated[Optional[StrictStr], Field(description="Optional team filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_team_recruiting_rankings  # noqa: E501

        Retrieves team recruiting rankings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_team_recruiting_rankings_with_http_info(year, team, async_req=True)
        >>> result = thread.get()

        :param year: Optional year filter
        :type year: int
        :param team: Optional team filter
        :type team: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[TeamRecruitingRanking], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'team'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_recruiting_rankings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('year') is not None:  # noqa: E501
            _query_params.append(('year', _params['year']))

        if _params.get('team') is not None:  # noqa: E501
            _query_params.append(('team', _params['team']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apiKey']  # noqa: E501

        _response_types_map = {
            '200': "List[TeamRecruitingRanking]",
        }

        return self.api_client.call_api(
            '/recruiting/teams', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
