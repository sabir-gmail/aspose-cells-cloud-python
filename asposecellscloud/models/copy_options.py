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


class CopyOptions(object):
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
        'refer_to_destination_sheet': 'bool',
        'copy_names': 'bool',
        'refer_to_sheet_with_same_name': 'bool',
        'column_character_width': 'bool',
        'copy_invalid_formulas_as_values': 'bool',
        'extend_to_adjacent_range': 'bool'
    }

    attribute_map = {
        'refer_to_destination_sheet': 'ReferToDestinationSheet',
        'copy_names': 'CopyNames',
        'refer_to_sheet_with_same_name': 'ReferToSheetWithSameName',
        'column_character_width': 'ColumnCharacterWidth',
        'copy_invalid_formulas_as_values': 'CopyInvalidFormulasAsValues',
        'extend_to_adjacent_range': 'ExtendToAdjacentRange'
    }
    
    @staticmethod
    def get_swagger_types():
        return CopyOptions.swagger_types
    
    @staticmethod
    def get_attribute_map():
        return CopyOptions.attribute_map
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, refer_to_destination_sheet=None, copy_names=None, refer_to_sheet_with_same_name=None, column_character_width=None, copy_invalid_formulas_as_values=None, extend_to_adjacent_range=None, **kw):
        """
        Associative dict for storing property values
        """
        self.container = {}
		    
        """
        CopyOptions - a model defined in Swagger
        """

        self.container['refer_to_destination_sheet'] = None
        self.container['copy_names'] = None
        self.container['refer_to_sheet_with_same_name'] = None
        self.container['column_character_width'] = None
        self.container['copy_invalid_formulas_as_values'] = None
        self.container['extend_to_adjacent_range'] = None

        if refer_to_destination_sheet is not None:
          self.refer_to_destination_sheet = refer_to_destination_sheet
        if copy_names is not None:
          self.copy_names = copy_names
        if refer_to_sheet_with_same_name is not None:
          self.refer_to_sheet_with_same_name = refer_to_sheet_with_same_name
        if column_character_width is not None:
          self.column_character_width = column_character_width
        if copy_invalid_formulas_as_values is not None:
          self.copy_invalid_formulas_as_values = copy_invalid_formulas_as_values
        if extend_to_adjacent_range is not None:
          self.extend_to_adjacent_range = extend_to_adjacent_range

    @property
    def refer_to_destination_sheet(self):
        """
        Gets the refer_to_destination_sheet of this CopyOptions.
        When copying the range in the same file and the chart refers to the source sheet,   False means the copied chart's data source will not be changed. True means the   copied chart's data source refers to the destination sheet.             

        :return: The refer_to_destination_sheet of this CopyOptions.
        :rtype: bool
        """
        return self.container['refer_to_destination_sheet']

    @refer_to_destination_sheet.setter
    def refer_to_destination_sheet(self, refer_to_destination_sheet):
        """
        Sets the refer_to_destination_sheet of this CopyOptions.
        When copying the range in the same file and the chart refers to the source sheet,   False means the copied chart's data source will not be changed. True means the   copied chart's data source refers to the destination sheet.             

        :param refer_to_destination_sheet: The refer_to_destination_sheet of this CopyOptions.
        :type: bool
        """

        self.container['refer_to_destination_sheet'] = refer_to_destination_sheet

    @property
    def copy_names(self):
        """
        Gets the copy_names of this CopyOptions.
        Indicates whether copying the names.

        :return: The copy_names of this CopyOptions.
        :rtype: bool
        """
        return self.container['copy_names']

    @copy_names.setter
    def copy_names(self, copy_names):
        """
        Sets the copy_names of this CopyOptions.
        Indicates whether copying the names.

        :param copy_names: The copy_names of this CopyOptions.
        :type: bool
        """

        self.container['copy_names'] = copy_names

    @property
    def refer_to_sheet_with_same_name(self):
        """
        Gets the refer_to_sheet_with_same_name of this CopyOptions.

        :return: The refer_to_sheet_with_same_name of this CopyOptions.
        :rtype: bool
        """
        return self.container['refer_to_sheet_with_same_name']

    @refer_to_sheet_with_same_name.setter
    def refer_to_sheet_with_same_name(self, refer_to_sheet_with_same_name):
        """
        Sets the refer_to_sheet_with_same_name of this CopyOptions.

        :param refer_to_sheet_with_same_name: The refer_to_sheet_with_same_name of this CopyOptions.
        :type: bool
        """

        self.container['refer_to_sheet_with_same_name'] = refer_to_sheet_with_same_name

    @property
    def column_character_width(self):
        """
        Gets the column_character_width of this CopyOptions.
        Indicates whether copying column width in unit of characters.

        :return: The column_character_width of this CopyOptions.
        :rtype: bool
        """
        return self.container['column_character_width']

    @column_character_width.setter
    def column_character_width(self, column_character_width):
        """
        Sets the column_character_width of this CopyOptions.
        Indicates whether copying column width in unit of characters.

        :param column_character_width: The column_character_width of this CopyOptions.
        :type: bool
        """

        self.container['column_character_width'] = column_character_width

    @property
    def copy_invalid_formulas_as_values(self):
        """
        Gets the copy_invalid_formulas_as_values of this CopyOptions.
        If the formula is not valid for the dest destination, only copy values.

        :return: The copy_invalid_formulas_as_values of this CopyOptions.
        :rtype: bool
        """
        return self.container['copy_invalid_formulas_as_values']

    @copy_invalid_formulas_as_values.setter
    def copy_invalid_formulas_as_values(self, copy_invalid_formulas_as_values):
        """
        Sets the copy_invalid_formulas_as_values of this CopyOptions.
        If the formula is not valid for the dest destination, only copy values.

        :param copy_invalid_formulas_as_values: The copy_invalid_formulas_as_values of this CopyOptions.
        :type: bool
        """

        self.container['copy_invalid_formulas_as_values'] = copy_invalid_formulas_as_values

    @property
    def extend_to_adjacent_range(self):
        """
        Gets the extend_to_adjacent_range of this CopyOptions.
        Indicates whether extend ranges when copying the range to adjacent range.

        :return: The extend_to_adjacent_range of this CopyOptions.
        :rtype: bool
        """
        return self.container['extend_to_adjacent_range']

    @extend_to_adjacent_range.setter
    def extend_to_adjacent_range(self, extend_to_adjacent_range):
        """
        Sets the extend_to_adjacent_range of this CopyOptions.
        Indicates whether extend ranges when copying the range to adjacent range.

        :param extend_to_adjacent_range: The extend_to_adjacent_range of this CopyOptions.
        :type: bool
        """

        self.container['extend_to_adjacent_range'] = extend_to_adjacent_range

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
        if not isinstance(other, CopyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
