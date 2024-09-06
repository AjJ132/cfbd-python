# coding: utf-8

"""
    College Football Data API

    This API is in limited Beta for Patreon subscribers. It may have bugs and is subject to changes. API keys can be acquired from the CollegeFootballData.com website.

    The version of the OpenAPI document: 5.0.19
    Contact: admin@collegefootballdata.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictFloat, StrictInt

from typing import List, Optional, Union

from cfbd.models.poll_week import PollWeek
from cfbd.models.season_type import SeasonType

from cfbd.api_client import ApiClient
from cfbd.api_response import ApiResponse
from cfbd.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RankingsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_rankings(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], season_type : Annotated[Optional[SeasonType], Field(description="Optional season type filter")] = None, week : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Optional week filter")] = None, **kwargs) -> List[PollWeek]:  # noqa: E501
        """get_rankings  # noqa: E501

        Retrieves historical poll data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rankings(year, season_type, week, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param season_type: Optional season type filter
        :type season_type: SeasonType
        :param week: Optional week filter
        :type week: float
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PollWeek]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_rankings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_rankings_with_http_info(year, season_type, week, **kwargs)  # noqa: E501

    @validate_arguments
    def get_rankings_with_http_info(self, year : Annotated[StrictInt, Field(..., description="Required year filter")], season_type : Annotated[Optional[SeasonType], Field(description="Optional season type filter")] = None, week : Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Optional week filter")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """get_rankings  # noqa: E501

        Retrieves historical poll data  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rankings_with_http_info(year, season_type, week, async_req=True)
        >>> result = thread.get()

        :param year: Required year filter (required)
        :type year: int
        :param season_type: Optional season type filter
        :type season_type: SeasonType
        :param week: Optional week filter
        :type week: float
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
        :rtype: tuple(List[PollWeek], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'year',
            'season_type',
            'week'
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
                    " to method get_rankings" % _key
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

        if _params.get('season_type') is not None:  # noqa: E501
            _query_params.append(('seasonType', _params['season_type'].value))

        if _params.get('week') is not None:  # noqa: E501
            _query_params.append(('week', _params['week']))

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
            '200': "List[PollWeek]",
        }

        return self.api_client.call_api(
            '/rankings', 'GET',
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
