# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CellsChartAreaApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def cells_chart_area_get_chart_area(self, name, sheet_name, chart_index, **kwargs):
        """
        Get chart area info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_chart_area_get_chart_area(name, sheet_name, chart_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Workbook name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int chart_index: The chart index. (required)
        :param str folder: Workbook folder.
        :return: ChartAreaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_chart_area_get_chart_area_with_http_info(name, sheet_name, chart_index, **kwargs)
        else:
            (data) = self.cells_chart_area_get_chart_area_with_http_info(name, sheet_name, chart_index, **kwargs)
            return data

    def cells_chart_area_get_chart_area_with_http_info(self, name, sheet_name, chart_index, **kwargs):
        """
        Get chart area info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_chart_area_get_chart_area_with_http_info(name, sheet_name, chart_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Workbook name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int chart_index: The chart index. (required)
        :param str folder: Workbook folder.
        :return: ChartAreaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'chart_index', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_chart_area_get_chart_area" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_chart_area_get_chart_area`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_chart_area_get_chart_area`")
        # verify the required parameter 'chart_index' is set
        if ('chart_index' not in params) or (params['chart_index'] is None):
            raise ValueError("Missing the required parameter `chart_index` when calling `cells_chart_area_get_chart_area`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'chart_index' in params:
            path_params['chartIndex'] = params['chart_index']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ChartAreaResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_chart_area_get_chart_area_border(self, name, sheet_name, chart_index, **kwargs):
        """
        Get chart area border info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_chart_area_get_chart_area_border(name, sheet_name, chart_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Workbook name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int chart_index: The chart index. (required)
        :param str folder: Workbook folder.
        :return: LineResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_chart_area_get_chart_area_border_with_http_info(name, sheet_name, chart_index, **kwargs)
        else:
            (data) = self.cells_chart_area_get_chart_area_border_with_http_info(name, sheet_name, chart_index, **kwargs)
            return data

    def cells_chart_area_get_chart_area_border_with_http_info(self, name, sheet_name, chart_index, **kwargs):
        """
        Get chart area border info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_chart_area_get_chart_area_border_with_http_info(name, sheet_name, chart_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Workbook name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int chart_index: The chart index. (required)
        :param str folder: Workbook folder.
        :return: LineResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'chart_index', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_chart_area_get_chart_area_border" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_chart_area_get_chart_area_border`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_chart_area_get_chart_area_border`")
        # verify the required parameter 'chart_index' is set
        if ('chart_index' not in params) or (params['chart_index'] is None):
            raise ValueError("Missing the required parameter `chart_index` when calling `cells_chart_area_get_chart_area_border`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'chart_index' in params:
            path_params['chartIndex'] = params['chart_index']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea/border', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='LineResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def cells_chart_area_get_chart_area_fill_format(self, name, sheet_name, chart_index, **kwargs):
        """
        Get chart area fill format info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_chart_area_get_chart_area_fill_format(name, sheet_name, chart_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Workbook name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int chart_index: The chart index. (required)
        :param str folder: Workbook folder.
        :return: FillFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.cells_chart_area_get_chart_area_fill_format_with_http_info(name, sheet_name, chart_index, **kwargs)
        else:
            (data) = self.cells_chart_area_get_chart_area_fill_format_with_http_info(name, sheet_name, chart_index, **kwargs)
            return data

    def cells_chart_area_get_chart_area_fill_format_with_http_info(self, name, sheet_name, chart_index, **kwargs):
        """
        Get chart area fill format info.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.cells_chart_area_get_chart_area_fill_format_with_http_info(name, sheet_name, chart_index, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: Workbook name. (required)
        :param str sheet_name: Worksheet name. (required)
        :param int chart_index: The chart index. (required)
        :param str folder: Workbook folder.
        :return: FillFormatResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'sheet_name', 'chart_index', 'folder']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cells_chart_area_get_chart_area_fill_format" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params) or (params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `cells_chart_area_get_chart_area_fill_format`")
        # verify the required parameter 'sheet_name' is set
        if ('sheet_name' not in params) or (params['sheet_name'] is None):
            raise ValueError("Missing the required parameter `sheet_name` when calling `cells_chart_area_get_chart_area_fill_format`")
        # verify the required parameter 'chart_index' is set
        if ('chart_index' not in params) or (params['chart_index'] is None):
            raise ValueError("Missing the required parameter `chart_index` when calling `cells_chart_area_get_chart_area_fill_format`")


        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']
        if 'sheet_name' in params:
            path_params['sheetName'] = params['sheet_name']
        if 'chart_index' in params:
            path_params['chartIndex'] = params['chart_index']

        query_params = []
        if 'folder' in params:
            query_params.append(('folder', params['folder']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/cells/{name}/worksheets/{sheetName}/charts/{chartIndex}/chartArea/fillFormat', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FillFormatResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
