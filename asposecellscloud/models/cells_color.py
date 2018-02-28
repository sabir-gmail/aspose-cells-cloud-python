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


class CellsColor(object):
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
        'color': 'Color',
        'color_index': 'int',
        'is_shape_color': 'bool',
        'theme_color': 'ThemeColor',
        'type': 'str'
    }

    attribute_map = {
        'color': 'Color',
        'color_index': 'ColorIndex',
        'is_shape_color': 'IsShapeColor',
        'theme_color': 'ThemeColor',
        'type': 'Type'
    }
    
    def get_swagger_types(self):
        return CellsColor.swagger_types
        
    def get_attribute_map(self):
        return CellsColor.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, color=None, color_index=None, is_shape_color=None, theme_color=None, type=None):
        """
        CellsColor - a model defined in Swagger
        """

        self.container['color'] = None
        self.container['color_index'] = None
        self.container['is_shape_color'] = None
        self.container['theme_color'] = None
        self.container['type'] = None

        if color is not None:
          self.color = color
        if color_index is not None:
          self.color_index = color_index
        if is_shape_color is not None:
          self.is_shape_color = is_shape_color
        if theme_color is not None:
          self.theme_color = theme_color
        if type is not None:
          self.type = type

    @property
    def color(self):
        """
        Gets the color of this CellsColor.

        :return: The color of this CellsColor.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this CellsColor.

        :param color: The color of this CellsColor.
        :type: Color
        """

        self.container['color'] = color

    @property
    def color_index(self):
        """
        Gets the color_index of this CellsColor.

        :return: The color_index of this CellsColor.
        :rtype: int
        """
        return self.container['color_index']

    @color_index.setter
    def color_index(self, color_index):
        """
        Sets the color_index of this CellsColor.

        :param color_index: The color_index of this CellsColor.
        :type: int
        """

        self.container['color_index'] = color_index

    @property
    def is_shape_color(self):
        """
        Gets the is_shape_color of this CellsColor.

        :return: The is_shape_color of this CellsColor.
        :rtype: bool
        """
        return self.container['is_shape_color']

    @is_shape_color.setter
    def is_shape_color(self, is_shape_color):
        """
        Sets the is_shape_color of this CellsColor.

        :param is_shape_color: The is_shape_color of this CellsColor.
        :type: bool
        """

        self.container['is_shape_color'] = is_shape_color

    @property
    def theme_color(self):
        """
        Gets the theme_color of this CellsColor.

        :return: The theme_color of this CellsColor.
        :rtype: ThemeColor
        """
        return self.container['theme_color']

    @theme_color.setter
    def theme_color(self, theme_color):
        """
        Sets the theme_color of this CellsColor.

        :param theme_color: The theme_color of this CellsColor.
        :type: ThemeColor
        """

        self.container['theme_color'] = theme_color

    @property
    def type(self):
        """
        Gets the type of this CellsColor.

        :return: The type of this CellsColor.
        :rtype: str
        """
        return self.container['type']

    @type.setter
    def type(self, type):
        """
        Sets the type of this CellsColor.

        :param type: The type of this CellsColor.
        :type: str
        """

        self.container['type'] = type

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
        if not isinstance(other, CellsColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other