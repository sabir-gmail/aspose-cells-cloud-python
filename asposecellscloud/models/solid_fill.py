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


class SolidFill(object):
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
        'cells_color': 'CellsColor',
        'transparency': 'float'
    }

    attribute_map = {
        'color': 'Color',
        'cells_color': 'CellsColor',
        'transparency': 'Transparency'
    }
    
    def get_swagger_types(self):
        return SolidFill.swagger_types
        
    def get_attribute_map(self):
        return SolidFill.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, color=None, cells_color=None, transparency=None):
        """
        SolidFill - a model defined in Swagger
        """

        self.container['color'] = None
        self.container['cells_color'] = None
        self.container['transparency'] = None

        if color is not None:
          self.color = color
        if cells_color is not None:
          self.cells_color = cells_color
        if transparency is not None:
          self.transparency = transparency

    @property
    def color(self):
        """
        Gets the color of this SolidFill.

        :return: The color of this SolidFill.
        :rtype: Color
        """
        return self.container['color']

    @color.setter
    def color(self, color):
        """
        Sets the color of this SolidFill.

        :param color: The color of this SolidFill.
        :type: Color
        """

        self.container['color'] = color

    @property
    def cells_color(self):
        """
        Gets the cells_color of this SolidFill.

        :return: The cells_color of this SolidFill.
        :rtype: CellsColor
        """
        return self.container['cells_color']

    @cells_color.setter
    def cells_color(self, cells_color):
        """
        Sets the cells_color of this SolidFill.

        :param cells_color: The cells_color of this SolidFill.
        :type: CellsColor
        """

        self.container['cells_color'] = cells_color

    @property
    def transparency(self):
        """
        Gets the transparency of this SolidFill.

        :return: The transparency of this SolidFill.
        :rtype: float
        """
        return self.container['transparency']

    @transparency.setter
    def transparency(self, transparency):
        """
        Sets the transparency of this SolidFill.

        :param transparency: The transparency of this SolidFill.
        :type: float
        """

        self.container['transparency'] = transparency

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
        if not isinstance(other, SolidFill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
