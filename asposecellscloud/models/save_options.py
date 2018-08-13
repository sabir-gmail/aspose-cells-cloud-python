# coding: utf-8

"""
    Web API Swagger specification

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SaveOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'enable_http_compression': 'bool',
        'save_format': 'str',
        'clear_data': 'bool',
        'cached_file_folder': 'str',
        'validate_merged_areas': 'bool',
        'refresh_chart_cache': 'bool',
        'create_directory': 'bool',
        'sort_names': 'bool'
    }

    attribute_map = {
        'enable_http_compression': 'EnableHTTPCompression',
        'save_format': 'SaveFormat',
        'clear_data': 'ClearData',
        'cached_file_folder': 'CachedFileFolder',
        'validate_merged_areas': 'ValidateMergedAreas',
        'refresh_chart_cache': 'RefreshChartCache',
        'create_directory': 'CreateDirectory',
        'sort_names': 'SortNames'
    }
    
    @staticmethod
    def get_swagger_types():
        return SaveOptions.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return SaveOptions.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, enable_http_compression=None, save_format=None, clear_data=None, cached_file_folder=None, validate_merged_areas=None, refresh_chart_cache=None, create_directory=None, sort_names=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        SaveOptions - a model defined in Swagger
        """

        self.container['enable_http_compression'] = None
        self.container['save_format'] = None
        self.container['clear_data'] = None
        self.container['cached_file_folder'] = None
        self.container['validate_merged_areas'] = None
        self.container['refresh_chart_cache'] = None
        self.container['create_directory'] = None
        self.container['sort_names'] = None

        if enable_http_compression is not None:
          self.enable_http_compression = enable_http_compression
        if save_format is not None:
          self.save_format = save_format
        if clear_data is not None:
          self.clear_data = clear_data
        if cached_file_folder is not None:
          self.cached_file_folder = cached_file_folder
        if validate_merged_areas is not None:
          self.validate_merged_areas = validate_merged_areas
        if refresh_chart_cache is not None:
          self.refresh_chart_cache = refresh_chart_cache
        if create_directory is not None:
          self.create_directory = create_directory
        if sort_names is not None:
          self.sort_names = sort_names

    @property
    def enable_http_compression(self):
        """
        Gets the enable_http_compression of this SaveOptions.

        :return: The enable_http_compression of this SaveOptions.
        :rtype: bool
        """
        return self.container['enable_http_compression']

    @enable_http_compression.setter
    def enable_http_compression(self, enable_http_compression):
        """
        Sets the enable_http_compression of this SaveOptions.

        :param enable_http_compression: The enable_http_compression of this SaveOptions.
        :type: bool
        """

        self.container['enable_http_compression'] = enable_http_compression

    @property
    def save_format(self):
        """
        Gets the save_format of this SaveOptions.

        :return: The save_format of this SaveOptions.
        :rtype: str
        """
        return self.container['save_format']

    @save_format.setter
    def save_format(self, save_format):
        """
        Sets the save_format of this SaveOptions.

        :param save_format: The save_format of this SaveOptions.
        :type: str
        """

        self.container['save_format'] = save_format

    @property
    def clear_data(self):
        """
        Gets the clear_data of this SaveOptions.
        Make the workbook empty after saving the file.

        :return: The clear_data of this SaveOptions.
        :rtype: bool
        """
        return self.container['clear_data']

    @clear_data.setter
    def clear_data(self, clear_data):
        """
        Sets the clear_data of this SaveOptions.
        Make the workbook empty after saving the file.

        :param clear_data: The clear_data of this SaveOptions.
        :type: bool
        """

        self.container['clear_data'] = clear_data

    @property
    def cached_file_folder(self):
        """
        Gets the cached_file_folder of this SaveOptions.
        The cached file folder is used to store some large data.

        :return: The cached_file_folder of this SaveOptions.
        :rtype: str
        """
        return self.container['cached_file_folder']

    @cached_file_folder.setter
    def cached_file_folder(self, cached_file_folder):
        """
        Sets the cached_file_folder of this SaveOptions.
        The cached file folder is used to store some large data.

        :param cached_file_folder: The cached_file_folder of this SaveOptions.
        :type: str
        """

        self.container['cached_file_folder'] = cached_file_folder

    @property
    def validate_merged_areas(self):
        """
        Gets the validate_merged_areas of this SaveOptions.
        Indicates whether validate merged areas before saving the file. The default value is false.             

        :return: The validate_merged_areas of this SaveOptions.
        :rtype: bool
        """
        return self.container['validate_merged_areas']

    @validate_merged_areas.setter
    def validate_merged_areas(self, validate_merged_areas):
        """
        Sets the validate_merged_areas of this SaveOptions.
        Indicates whether validate merged areas before saving the file. The default value is false.             

        :param validate_merged_areas: The validate_merged_areas of this SaveOptions.
        :type: bool
        """

        self.container['validate_merged_areas'] = validate_merged_areas

    @property
    def refresh_chart_cache(self):
        """
        Gets the refresh_chart_cache of this SaveOptions.

        :return: The refresh_chart_cache of this SaveOptions.
        :rtype: bool
        """
        return self.container['refresh_chart_cache']

    @refresh_chart_cache.setter
    def refresh_chart_cache(self, refresh_chart_cache):
        """
        Sets the refresh_chart_cache of this SaveOptions.

        :param refresh_chart_cache: The refresh_chart_cache of this SaveOptions.
        :type: bool
        """

        self.container['refresh_chart_cache'] = refresh_chart_cache

    @property
    def create_directory(self):
        """
        Gets the create_directory of this SaveOptions.
        If true and the directory does not exist, the directory will be automatically created before saving the file.             

        :return: The create_directory of this SaveOptions.
        :rtype: bool
        """
        return self.container['create_directory']

    @create_directory.setter
    def create_directory(self, create_directory):
        """
        Sets the create_directory of this SaveOptions.
        If true and the directory does not exist, the directory will be automatically created before saving the file.             

        :param create_directory: The create_directory of this SaveOptions.
        :type: bool
        """

        self.container['create_directory'] = create_directory

    @property
    def sort_names(self):
        """
        Gets the sort_names of this SaveOptions.

        :return: The sort_names of this SaveOptions.
        :rtype: bool
        """
        return self.container['sort_names']

    @sort_names.setter
    def sort_names(self, sort_names):
        """
        Sets the sort_names of this SaveOptions.

        :param sort_names: The sort_names of this SaveOptions.
        :type: bool
        """

        self.container['sort_names'] = sort_names

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.get_swagger_types()):
            value = self.get_from_container(attr)
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SaveOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
