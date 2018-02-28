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


class CreatePivotTableRequest(object):
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
        'name': 'str',
        'source_data': 'str',
        'dest_cell_name': 'str',
        'use_same_source': 'bool',
        'pivot_field_rows': 'list[int]',
        'pivot_field_columns': 'list[int]',
        'pivot_field_data': 'list[int]'
    }

    attribute_map = {
        'name': 'Name',
        'source_data': 'SourceData',
        'dest_cell_name': 'DestCellName',
        'use_same_source': 'UseSameSource',
        'pivot_field_rows': 'PivotFieldRows',
        'pivot_field_columns': 'PivotFieldColumns',
        'pivot_field_data': 'PivotFieldData'
    }
    
    def get_swagger_types(self):
        return CreatePivotTableRequest.swagger_types
        
    def get_attribute_map(self):
        return CreatePivotTableRequest.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, name=None, source_data=None, dest_cell_name=None, use_same_source=None, pivot_field_rows=None, pivot_field_columns=None, pivot_field_data=None):
        """
        CreatePivotTableRequest - a model defined in Swagger
        """

        self.container['name'] = None
        self.container['source_data'] = None
        self.container['dest_cell_name'] = None
        self.container['use_same_source'] = None
        self.container['pivot_field_rows'] = None
        self.container['pivot_field_columns'] = None
        self.container['pivot_field_data'] = None

        if name is not None:
          self.name = name
        if source_data is not None:
          self.source_data = source_data
        if dest_cell_name is not None:
          self.dest_cell_name = dest_cell_name
        self.use_same_source = use_same_source
        if pivot_field_rows is not None:
          self.pivot_field_rows = pivot_field_rows
        if pivot_field_columns is not None:
          self.pivot_field_columns = pivot_field_columns
        if pivot_field_data is not None:
          self.pivot_field_data = pivot_field_data

    @property
    def name(self):
        """
        Gets the name of this CreatePivotTableRequest.

        :return: The name of this CreatePivotTableRequest.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreatePivotTableRequest.

        :param name: The name of this CreatePivotTableRequest.
        :type: str
        """

        self.container['name'] = name

    @property
    def source_data(self):
        """
        Gets the source_data of this CreatePivotTableRequest.

        :return: The source_data of this CreatePivotTableRequest.
        :rtype: str
        """
        return self.container['source_data']

    @source_data.setter
    def source_data(self, source_data):
        """
        Sets the source_data of this CreatePivotTableRequest.

        :param source_data: The source_data of this CreatePivotTableRequest.
        :type: str
        """

        self.container['source_data'] = source_data

    @property
    def dest_cell_name(self):
        """
        Gets the dest_cell_name of this CreatePivotTableRequest.

        :return: The dest_cell_name of this CreatePivotTableRequest.
        :rtype: str
        """
        return self.container['dest_cell_name']

    @dest_cell_name.setter
    def dest_cell_name(self, dest_cell_name):
        """
        Sets the dest_cell_name of this CreatePivotTableRequest.

        :param dest_cell_name: The dest_cell_name of this CreatePivotTableRequest.
        :type: str
        """

        self.container['dest_cell_name'] = dest_cell_name

    @property
    def use_same_source(self):
        """
        Gets the use_same_source of this CreatePivotTableRequest.

        :return: The use_same_source of this CreatePivotTableRequest.
        :rtype: bool
        """
        return self.container['use_same_source']

    @use_same_source.setter
    def use_same_source(self, use_same_source):
        """
        Sets the use_same_source of this CreatePivotTableRequest.

        :param use_same_source: The use_same_source of this CreatePivotTableRequest.
        :type: bool
        """
        if use_same_source is None:
            raise ValueError("Invalid value for `use_same_source`, must not be `None`")

        self.container['use_same_source'] = use_same_source

    @property
    def pivot_field_rows(self):
        """
        Gets the pivot_field_rows of this CreatePivotTableRequest.

        :return: The pivot_field_rows of this CreatePivotTableRequest.
        :rtype: list[int]
        """
        return self.container['pivot_field_rows']

    @pivot_field_rows.setter
    def pivot_field_rows(self, pivot_field_rows):
        """
        Sets the pivot_field_rows of this CreatePivotTableRequest.

        :param pivot_field_rows: The pivot_field_rows of this CreatePivotTableRequest.
        :type: list[int]
        """

        self.container['pivot_field_rows'] = pivot_field_rows

    @property
    def pivot_field_columns(self):
        """
        Gets the pivot_field_columns of this CreatePivotTableRequest.

        :return: The pivot_field_columns of this CreatePivotTableRequest.
        :rtype: list[int]
        """
        return self.container['pivot_field_columns']

    @pivot_field_columns.setter
    def pivot_field_columns(self, pivot_field_columns):
        """
        Sets the pivot_field_columns of this CreatePivotTableRequest.

        :param pivot_field_columns: The pivot_field_columns of this CreatePivotTableRequest.
        :type: list[int]
        """

        self.container['pivot_field_columns'] = pivot_field_columns

    @property
    def pivot_field_data(self):
        """
        Gets the pivot_field_data of this CreatePivotTableRequest.

        :return: The pivot_field_data of this CreatePivotTableRequest.
        :rtype: list[int]
        """
        return self.container['pivot_field_data']

    @pivot_field_data.setter
    def pivot_field_data(self, pivot_field_data):
        """
        Sets the pivot_field_data of this CreatePivotTableRequest.

        :param pivot_field_data: The pivot_field_data of this CreatePivotTableRequest.
        :type: list[int]
        """

        self.container['pivot_field_data'] = pivot_field_data

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
        if not isinstance(other, CreatePivotTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
