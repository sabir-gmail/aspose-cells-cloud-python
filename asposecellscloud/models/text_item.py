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


class TextItem(object):
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
        'text': 'str'
    }

    attribute_map = {
        'link': 'link',
        'text': 'Text'
    }
    
    def get_swagger_types(self):
        return TextItem.swagger_types
        
    def get_attribute_map(self):
        return TextItem.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, text=None):
        """
        TextItem - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['text'] = None

        if link is not None:
          self.link = link
        if text is not None:
          self.text = text

    @property
    def link(self):
        """
        Gets the link of this TextItem.

        :return: The link of this TextItem.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this TextItem.

        :param link: The link of this TextItem.
        :type: Link
        """

        self.container['link'] = link

    @property
    def text(self):
        """
        Gets the text of this TextItem.

        :return: The text of this TextItem.
        :rtype: str
        """
        return self.container['text']

    @text.setter
    def text(self, text):
        """
        Sets the text of this TextItem.

        :param text: The text of this TextItem.
        :type: str
        """

        self.container['text'] = text

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
        if not isinstance(other, TextItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
