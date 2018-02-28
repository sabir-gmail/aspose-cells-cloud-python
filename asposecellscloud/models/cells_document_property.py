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


class CellsDocumentProperty(object):
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
        'link': 'Link',
        'name': 'str',
        'value': 'str',
        'built_in': 'str'
    }

    attribute_map = {
        'link': 'link',
        'name': 'Name',
        'value': 'Value',
        'built_in': 'BuiltIn'
    }
    
    def get_swagger_types(self):
        return CellsDocumentProperty.swagger_types
        
    def get_attribute_map(self):
        return CellsDocumentProperty.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, name=None, value=None, built_in=None):
        """
        CellsDocumentProperty - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['name'] = None
        self.container['value'] = None
        self.container['built_in'] = None

        if link is not None:
          self.link = link
        if name is not None:
          self.name = name
        if value is not None:
          self.value = value
        if built_in is not None:
          self.built_in = built_in

    @property
    def link(self):
        """
        Gets the link of this CellsDocumentProperty.

        :return: The link of this CellsDocumentProperty.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this CellsDocumentProperty.

        :param link: The link of this CellsDocumentProperty.
        :type: Link
        """

        self.container['link'] = link

    @property
    def name(self):
        """
        Gets the name of this CellsDocumentProperty.

        :return: The name of this CellsDocumentProperty.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this CellsDocumentProperty.

        :param name: The name of this CellsDocumentProperty.
        :type: str
        """

        self.container['name'] = name

    @property
    def value(self):
        """
        Gets the value of this CellsDocumentProperty.

        :return: The value of this CellsDocumentProperty.
        :rtype: str
        """
        return self.container['value']

    @value.setter
    def value(self, value):
        """
        Sets the value of this CellsDocumentProperty.

        :param value: The value of this CellsDocumentProperty.
        :type: str
        """

        self.container['value'] = value

    @property
    def built_in(self):
        """
        Gets the built_in of this CellsDocumentProperty.

        :return: The built_in of this CellsDocumentProperty.
        :rtype: str
        """
        return self.container['built_in']

    @built_in.setter
    def built_in(self, built_in):
        """
        Sets the built_in of this CellsDocumentProperty.

        :param built_in: The built_in of this CellsDocumentProperty.
        :type: str
        """

        self.container['built_in'] = built_in

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
        if not isinstance(other, CellsDocumentProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
