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


class ListColumn(object):
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
        'totals_calculation': 'str'
    }

    attribute_map = {
        'name': 'Name',
        'totals_calculation': 'TotalsCalculation'
    }
    
    def get_swagger_types(self):
        return ListColumn.swagger_types
        
    def get_attribute_map(self):
        return ListColumn.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, name=None, totals_calculation=None):
        """
        ListColumn - a model defined in Swagger
        """

        self.container['name'] = None
        self.container['totals_calculation'] = None

        if name is not None:
          self.name = name
        if totals_calculation is not None:
          self.totals_calculation = totals_calculation

    @property
    def name(self):
        """
        Gets the name of this ListColumn.
        Gets and sets the name of the column.

        :return: The name of this ListColumn.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListColumn.
        Gets and sets the name of the column.

        :param name: The name of this ListColumn.
        :type: str
        """

        self.container['name'] = name

    @property
    def totals_calculation(self):
        """
        Gets the totals_calculation of this ListColumn.
        Gets and sets the type of calculation in the Totals row of the list column.

        :return: The totals_calculation of this ListColumn.
        :rtype: str
        """
        return self.container['totals_calculation']

    @totals_calculation.setter
    def totals_calculation(self, totals_calculation):
        """
        Sets the totals_calculation of this ListColumn.
        Gets and sets the type of calculation in the Totals row of the list column.

        :param totals_calculation: The totals_calculation of this ListColumn.
        :type: str
        """

        self.container['totals_calculation'] = totals_calculation

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
        if not isinstance(other, ListColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other