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


class HorizontalPageBreak(object):
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
        'start_column': 'int',
        'end_column': 'int',
        'row': 'int'
    }

    attribute_map = {
        'start_column': 'StartColumn',
        'end_column': 'EndColumn',
        'row': 'Row'
    }
    
    @staticmethod
    def get_swagger_types():
        return HorizontalPageBreak.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return HorizontalPageBreak.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, start_column=None, end_column=None, row=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        HorizontalPageBreak - a model defined in Swagger
        """

        self.container['start_column'] = None
        self.container['end_column'] = None
        self.container['row'] = None

        self.start_column = start_column
        self.end_column = end_column
        self.row = row

    @property
    def start_column(self):
        """
        Gets the start_column of this HorizontalPageBreak.

        :return: The start_column of this HorizontalPageBreak.
        :rtype: int
        """
        return self.container['start_column']

    @start_column.setter
    def start_column(self, start_column):
        """
        Sets the start_column of this HorizontalPageBreak.

        :param start_column: The start_column of this HorizontalPageBreak.
        :type: int
        """
        """
        if start_column is None:
            raise ValueError("Invalid value for `start_column`, must not be `None`")
        """

        self.container['start_column'] = start_column

    @property
    def end_column(self):
        """
        Gets the end_column of this HorizontalPageBreak.

        :return: The end_column of this HorizontalPageBreak.
        :rtype: int
        """
        return self.container['end_column']

    @end_column.setter
    def end_column(self, end_column):
        """
        Sets the end_column of this HorizontalPageBreak.

        :param end_column: The end_column of this HorizontalPageBreak.
        :type: int
        """
        """
        if end_column is None:
            raise ValueError("Invalid value for `end_column`, must not be `None`")
        """

        self.container['end_column'] = end_column

    @property
    def row(self):
        """
        Gets the row of this HorizontalPageBreak.

        :return: The row of this HorizontalPageBreak.
        :rtype: int
        """
        return self.container['row']

    @row.setter
    def row(self, row):
        """
        Sets the row of this HorizontalPageBreak.

        :param row: The row of this HorizontalPageBreak.
        :type: int
        """
        """
        if row is None:
            raise ValueError("Invalid value for `row`, must not be `None`")
        """

        self.container['row'] = row

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
        if not isinstance(other, HorizontalPageBreak):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
