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


class OleObjects(object):
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
        'ole_object_list': 'list[LinkElement]'
    }

    attribute_map = {
        'link': 'link',
        'ole_object_list': 'OleObjectList'
    }
    
    def get_swagger_types(self):
        return OleObjects.swagger_types
        
    def get_attribute_map(self):
        return OleObjects.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, ole_object_list=None):
        """
        OleObjects - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['ole_object_list'] = None

        if link is not None:
          self.link = link
        if ole_object_list is not None:
          self.ole_object_list = ole_object_list

    @property
    def link(self):
        """
        Gets the link of this OleObjects.

        :return: The link of this OleObjects.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this OleObjects.

        :param link: The link of this OleObjects.
        :type: Link
        """

        self.container['link'] = link

    @property
    def ole_object_list(self):
        """
        Gets the ole_object_list of this OleObjects.

        :return: The ole_object_list of this OleObjects.
        :rtype: list[LinkElement]
        """
        return self.container['ole_object_list']

    @ole_object_list.setter
    def ole_object_list(self, ole_object_list):
        """
        Sets the ole_object_list of this OleObjects.

        :param ole_object_list: The ole_object_list of this OleObjects.
        :type: list[LinkElement]
        """

        self.container['ole_object_list'] = ole_object_list

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
        if not isinstance(other, OleObjects):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other