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
from . import ImportOption

class ImportIntArrayOption(ImportOption):
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
        'first_row': 'int',
        'first_column': 'int',
        'is_vertical': 'bool',
        'data': 'list[int]'
    }

    attribute_map = {
        'first_row': 'FirstRow',
        'first_column': 'FirstColumn',
        'is_vertical': 'IsVertical',
        'data': 'Data'
    }
    
    def get_swagger_types(self):
        return dict(ImportIntArrayOption.swagger_types, **ImportOption.get_swagger_types(self))
        
    def get_attribute_map(self):
        return dict(ImportIntArrayOption.attribute_map, **ImportOption.get_attribute_map(self))
    
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, first_row=None, first_column=None, is_vertical=None, data=None):
        """
        ImportIntArrayOption - a model defined in Swagger
        """

        self.container['first_row'] = None
        self.container['first_column'] = None
        self.container['is_vertical'] = None
        self.container['data'] = None

        if first_row is not None:
          self.first_row = first_row
        if first_column is not None:
          self.first_column = first_column
        if is_vertical is not None:
          self.is_vertical = is_vertical
        if data is not None:
          self.data = data

    @property
    def first_row(self):
        """
        Gets the first_row of this ImportIntArrayOption.

        :return: The first_row of this ImportIntArrayOption.
        :rtype: int
        """
        return self.container['first_row']

    @first_row.setter
    def first_row(self, first_row):
        """
        Sets the first_row of this ImportIntArrayOption.

        :param first_row: The first_row of this ImportIntArrayOption.
        :type: int
        """

        self.container['first_row'] = first_row

    @property
    def first_column(self):
        """
        Gets the first_column of this ImportIntArrayOption.

        :return: The first_column of this ImportIntArrayOption.
        :rtype: int
        """
        return self.container['first_column']

    @first_column.setter
    def first_column(self, first_column):
        """
        Sets the first_column of this ImportIntArrayOption.

        :param first_column: The first_column of this ImportIntArrayOption.
        :type: int
        """

        self.container['first_column'] = first_column

    @property
    def is_vertical(self):
        """
        Gets the is_vertical of this ImportIntArrayOption.

        :return: The is_vertical of this ImportIntArrayOption.
        :rtype: bool
        """
        return self.container['is_vertical']

    @is_vertical.setter
    def is_vertical(self, is_vertical):
        """
        Sets the is_vertical of this ImportIntArrayOption.

        :param is_vertical: The is_vertical of this ImportIntArrayOption.
        :type: bool
        """

        self.container['is_vertical'] = is_vertical

    @property
    def data(self):
        """
        Gets the data of this ImportIntArrayOption.

        :return: The data of this ImportIntArrayOption.
        :rtype: list[int]
        """
        return self.container['data']

    @data.setter
    def data(self, data):
        """
        Sets the data of this ImportIntArrayOption.

        :param data: The data of this ImportIntArrayOption.
        :type: list[int]
        """

        self.container['data'] = data

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
        if not isinstance(other, ImportIntArrayOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other