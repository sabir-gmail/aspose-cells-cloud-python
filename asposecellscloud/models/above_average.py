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


class AboveAverage(object):
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
        'is_above_average': 'bool',
        'is_equal_average': 'bool',
        'std_dev': 'int'
    }

    attribute_map = {
        'is_above_average': 'IsAboveAverage',
        'is_equal_average': 'IsEqualAverage',
        'std_dev': 'StdDev'
    }
    
    def get_swagger_types(self):
        return AboveAverage.swagger_types
        
    def get_attribute_map(self):
        return AboveAverage.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, is_above_average=None, is_equal_average=None, std_dev=None):
        """
        AboveAverage - a model defined in Swagger
        """

        self.container['is_above_average'] = None
        self.container['is_equal_average'] = None
        self.container['std_dev'] = None

        self.is_above_average = is_above_average
        self.is_equal_average = is_equal_average
        self.std_dev = std_dev

    @property
    def is_above_average(self):
        """
        Gets the is_above_average of this AboveAverage.
        Get or set the flag indicating whether the rule is an \"above average\" rule.    'true' indicates 'above average'.  Default value is true.             

        :return: The is_above_average of this AboveAverage.
        :rtype: bool
        """
        return self.container['is_above_average']

    @is_above_average.setter
    def is_above_average(self, is_above_average):
        """
        Sets the is_above_average of this AboveAverage.
        Get or set the flag indicating whether the rule is an \"above average\" rule.    'true' indicates 'above average'.  Default value is true.             

        :param is_above_average: The is_above_average of this AboveAverage.
        :type: bool
        """
        if is_above_average is None:
            raise ValueError("Invalid value for `is_above_average`, must not be `None`")

        self.container['is_above_average'] = is_above_average

    @property
    def is_equal_average(self):
        """
        Gets the is_equal_average of this AboveAverage.
        Get or set the flag indicating whether the 'aboveAverage' and 'belowAverage'    criteria is inclusive of the average itself, or exclusive of that value.    'true' indicates to include the average value in the criteria.  Default value    is false.             

        :return: The is_equal_average of this AboveAverage.
        :rtype: bool
        """
        return self.container['is_equal_average']

    @is_equal_average.setter
    def is_equal_average(self, is_equal_average):
        """
        Sets the is_equal_average of this AboveAverage.
        Get or set the flag indicating whether the 'aboveAverage' and 'belowAverage'    criteria is inclusive of the average itself, or exclusive of that value.    'true' indicates to include the average value in the criteria.  Default value    is false.             

        :param is_equal_average: The is_equal_average of this AboveAverage.
        :type: bool
        """
        if is_equal_average is None:
            raise ValueError("Invalid value for `is_equal_average`, must not be `None`")

        self.container['is_equal_average'] = is_equal_average

    @property
    def std_dev(self):
        """
        Gets the std_dev of this AboveAverage.
        Get or set the number of standard deviations to include above or below the   average in the conditional formatting rule. The input value must between   0 and 3 (include 0 and 3). Setting this value to 0 means stdDev is not set.    The default value is 0.             

        :return: The std_dev of this AboveAverage.
        :rtype: int
        """
        return self.container['std_dev']

    @std_dev.setter
    def std_dev(self, std_dev):
        """
        Sets the std_dev of this AboveAverage.
        Get or set the number of standard deviations to include above or below the   average in the conditional formatting rule. The input value must between   0 and 3 (include 0 and 3). Setting this value to 0 means stdDev is not set.    The default value is 0.             

        :param std_dev: The std_dev of this AboveAverage.
        :type: int
        """
        if std_dev is None:
            raise ValueError("Invalid value for `std_dev`, must not be `None`")

        self.container['std_dev'] = std_dev

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
        if not isinstance(other, AboveAverage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
