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


class CellsDocumentProperties(object):
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
        'document_property_list': 'list[CellsDocumentProperty]'
    }

    attribute_map = {
        'link': 'link',
        'document_property_list': 'DocumentPropertyList'
    }
    
    def get_swagger_types(self):
        return CellsDocumentProperties.swagger_types
        
    def get_attribute_map(self):
        return CellsDocumentProperties.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, document_property_list=None):
        """
        CellsDocumentProperties - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['document_property_list'] = None

        if link is not None:
          self.link = link
        if document_property_list is not None:
          self.document_property_list = document_property_list

    @property
    def link(self):
        """
        Gets the link of this CellsDocumentProperties.

        :return: The link of this CellsDocumentProperties.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this CellsDocumentProperties.

        :param link: The link of this CellsDocumentProperties.
        :type: Link
        """

        self.container['link'] = link

    @property
    def document_property_list(self):
        """
        Gets the document_property_list of this CellsDocumentProperties.

        :return: The document_property_list of this CellsDocumentProperties.
        :rtype: list[CellsDocumentProperty]
        """
        return self.container['document_property_list']

    @document_property_list.setter
    def document_property_list(self, document_property_list):
        """
        Sets the document_property_list of this CellsDocumentProperties.

        :param document_property_list: The document_property_list of this CellsDocumentProperties.
        :type: list[CellsDocumentProperty]
        """

        self.container['document_property_list'] = document_property_list

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
        if not isinstance(other, CellsDocumentProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
