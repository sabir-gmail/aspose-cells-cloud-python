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


class Style(object):
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
        'font': 'Font',
        'name': 'str',
        'culture_custom': 'str',
        'custom': 'str',
        'background_color': 'Color',
        'foreground_color': 'Color',
        'is_formula_hidden': 'bool',
        'is_date_time': 'bool',
        'is_text_wrapped': 'bool',
        'is_gradient': 'bool',
        'is_locked': 'bool',
        'is_percent': 'bool',
        'shrink_to_fit': 'bool',
        'indent_level': 'int',
        'number': 'int',
        'rotation_angle': 'int',
        'pattern': 'str',
        'text_direction': 'str',
        'vertical_alignment': 'str',
        'horizontal_alignment': 'str',
        'border_collection': 'list[Border]',
        'background_theme_color': 'ThemeColor',
        'foreground_theme_color': 'ThemeColor'
    }

    attribute_map = {
        'link': 'link',
        'font': 'Font',
        'name': 'Name',
        'culture_custom': 'CultureCustom',
        'custom': 'Custom',
        'background_color': 'BackgroundColor',
        'foreground_color': 'ForegroundColor',
        'is_formula_hidden': 'IsFormulaHidden',
        'is_date_time': 'IsDateTime',
        'is_text_wrapped': 'IsTextWrapped',
        'is_gradient': 'IsGradient',
        'is_locked': 'IsLocked',
        'is_percent': 'IsPercent',
        'shrink_to_fit': 'ShrinkToFit',
        'indent_level': 'IndentLevel',
        'number': 'Number',
        'rotation_angle': 'RotationAngle',
        'pattern': 'Pattern',
        'text_direction': 'TextDirection',
        'vertical_alignment': 'VerticalAlignment',
        'horizontal_alignment': 'HorizontalAlignment',
        'border_collection': 'BorderCollection',
        'background_theme_color': 'BackgroundThemeColor',
        'foreground_theme_color': 'ForegroundThemeColor'
    }
    
    def get_swagger_types(self):
        return Style.swagger_types
        
    def get_attribute_map(self):
        return Style.attribute_map
    
    """
        Associative dict for storing property values
    """
    container = {}
    
    def get_from_container(self, attr):
        if attr in self.container:
            return self.container[attr]
        return None

    def __init__(self, link=None, font=None, name=None, culture_custom=None, custom=None, background_color=None, foreground_color=None, is_formula_hidden=None, is_date_time=None, is_text_wrapped=None, is_gradient=None, is_locked=None, is_percent=None, shrink_to_fit=None, indent_level=None, number=None, rotation_angle=None, pattern=None, text_direction=None, vertical_alignment=None, horizontal_alignment=None, border_collection=None, background_theme_color=None, foreground_theme_color=None):
        """
        Style - a model defined in Swagger
        """

        self.container['link'] = None
        self.container['font'] = None
        self.container['name'] = None
        self.container['culture_custom'] = None
        self.container['custom'] = None
        self.container['background_color'] = None
        self.container['foreground_color'] = None
        self.container['is_formula_hidden'] = None
        self.container['is_date_time'] = None
        self.container['is_text_wrapped'] = None
        self.container['is_gradient'] = None
        self.container['is_locked'] = None
        self.container['is_percent'] = None
        self.container['shrink_to_fit'] = None
        self.container['indent_level'] = None
        self.container['number'] = None
        self.container['rotation_angle'] = None
        self.container['pattern'] = None
        self.container['text_direction'] = None
        self.container['vertical_alignment'] = None
        self.container['horizontal_alignment'] = None
        self.container['border_collection'] = None
        self.container['background_theme_color'] = None
        self.container['foreground_theme_color'] = None

        if link is not None:
          self.link = link
        if font is not None:
          self.font = font
        if name is not None:
          self.name = name
        if culture_custom is not None:
          self.culture_custom = culture_custom
        if custom is not None:
          self.custom = custom
        if background_color is not None:
          self.background_color = background_color
        if foreground_color is not None:
          self.foreground_color = foreground_color
        if is_formula_hidden is not None:
          self.is_formula_hidden = is_formula_hidden
        if is_date_time is not None:
          self.is_date_time = is_date_time
        if is_text_wrapped is not None:
          self.is_text_wrapped = is_text_wrapped
        if is_gradient is not None:
          self.is_gradient = is_gradient
        if is_locked is not None:
          self.is_locked = is_locked
        if is_percent is not None:
          self.is_percent = is_percent
        if shrink_to_fit is not None:
          self.shrink_to_fit = shrink_to_fit
        if indent_level is not None:
          self.indent_level = indent_level
        if number is not None:
          self.number = number
        if rotation_angle is not None:
          self.rotation_angle = rotation_angle
        if pattern is not None:
          self.pattern = pattern
        if text_direction is not None:
          self.text_direction = text_direction
        if vertical_alignment is not None:
          self.vertical_alignment = vertical_alignment
        if horizontal_alignment is not None:
          self.horizontal_alignment = horizontal_alignment
        if border_collection is not None:
          self.border_collection = border_collection
        if background_theme_color is not None:
          self.background_theme_color = background_theme_color
        if foreground_theme_color is not None:
          self.foreground_theme_color = foreground_theme_color

    @property
    def link(self):
        """
        Gets the link of this Style.

        :return: The link of this Style.
        :rtype: Link
        """
        return self.container['link']

    @link.setter
    def link(self, link):
        """
        Sets the link of this Style.

        :param link: The link of this Style.
        :type: Link
        """

        self.container['link'] = link

    @property
    def font(self):
        """
        Gets the font of this Style.

        :return: The font of this Style.
        :rtype: Font
        """
        return self.container['font']

    @font.setter
    def font(self, font):
        """
        Sets the font of this Style.

        :param font: The font of this Style.
        :type: Font
        """

        self.container['font'] = font

    @property
    def name(self):
        """
        Gets the name of this Style.

        :return: The name of this Style.
        :rtype: str
        """
        return self.container['name']

    @name.setter
    def name(self, name):
        """
        Sets the name of this Style.

        :param name: The name of this Style.
        :type: str
        """

        self.container['name'] = name

    @property
    def culture_custom(self):
        """
        Gets the culture_custom of this Style.

        :return: The culture_custom of this Style.
        :rtype: str
        """
        return self.container['culture_custom']

    @culture_custom.setter
    def culture_custom(self, culture_custom):
        """
        Sets the culture_custom of this Style.

        :param culture_custom: The culture_custom of this Style.
        :type: str
        """

        self.container['culture_custom'] = culture_custom

    @property
    def custom(self):
        """
        Gets the custom of this Style.

        :return: The custom of this Style.
        :rtype: str
        """
        return self.container['custom']

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this Style.

        :param custom: The custom of this Style.
        :type: str
        """

        self.container['custom'] = custom

    @property
    def background_color(self):
        """
        Gets the background_color of this Style.

        :return: The background_color of this Style.
        :rtype: Color
        """
        return self.container['background_color']

    @background_color.setter
    def background_color(self, background_color):
        """
        Sets the background_color of this Style.

        :param background_color: The background_color of this Style.
        :type: Color
        """

        self.container['background_color'] = background_color

    @property
    def foreground_color(self):
        """
        Gets the foreground_color of this Style.

        :return: The foreground_color of this Style.
        :rtype: Color
        """
        return self.container['foreground_color']

    @foreground_color.setter
    def foreground_color(self, foreground_color):
        """
        Sets the foreground_color of this Style.

        :param foreground_color: The foreground_color of this Style.
        :type: Color
        """

        self.container['foreground_color'] = foreground_color

    @property
    def is_formula_hidden(self):
        """
        Gets the is_formula_hidden of this Style.

        :return: The is_formula_hidden of this Style.
        :rtype: bool
        """
        return self.container['is_formula_hidden']

    @is_formula_hidden.setter
    def is_formula_hidden(self, is_formula_hidden):
        """
        Sets the is_formula_hidden of this Style.

        :param is_formula_hidden: The is_formula_hidden of this Style.
        :type: bool
        """

        self.container['is_formula_hidden'] = is_formula_hidden

    @property
    def is_date_time(self):
        """
        Gets the is_date_time of this Style.

        :return: The is_date_time of this Style.
        :rtype: bool
        """
        return self.container['is_date_time']

    @is_date_time.setter
    def is_date_time(self, is_date_time):
        """
        Sets the is_date_time of this Style.

        :param is_date_time: The is_date_time of this Style.
        :type: bool
        """

        self.container['is_date_time'] = is_date_time

    @property
    def is_text_wrapped(self):
        """
        Gets the is_text_wrapped of this Style.

        :return: The is_text_wrapped of this Style.
        :rtype: bool
        """
        return self.container['is_text_wrapped']

    @is_text_wrapped.setter
    def is_text_wrapped(self, is_text_wrapped):
        """
        Sets the is_text_wrapped of this Style.

        :param is_text_wrapped: The is_text_wrapped of this Style.
        :type: bool
        """

        self.container['is_text_wrapped'] = is_text_wrapped

    @property
    def is_gradient(self):
        """
        Gets the is_gradient of this Style.

        :return: The is_gradient of this Style.
        :rtype: bool
        """
        return self.container['is_gradient']

    @is_gradient.setter
    def is_gradient(self, is_gradient):
        """
        Sets the is_gradient of this Style.

        :param is_gradient: The is_gradient of this Style.
        :type: bool
        """

        self.container['is_gradient'] = is_gradient

    @property
    def is_locked(self):
        """
        Gets the is_locked of this Style.

        :return: The is_locked of this Style.
        :rtype: bool
        """
        return self.container['is_locked']

    @is_locked.setter
    def is_locked(self, is_locked):
        """
        Sets the is_locked of this Style.

        :param is_locked: The is_locked of this Style.
        :type: bool
        """

        self.container['is_locked'] = is_locked

    @property
    def is_percent(self):
        """
        Gets the is_percent of this Style.

        :return: The is_percent of this Style.
        :rtype: bool
        """
        return self.container['is_percent']

    @is_percent.setter
    def is_percent(self, is_percent):
        """
        Sets the is_percent of this Style.

        :param is_percent: The is_percent of this Style.
        :type: bool
        """

        self.container['is_percent'] = is_percent

    @property
    def shrink_to_fit(self):
        """
        Gets the shrink_to_fit of this Style.

        :return: The shrink_to_fit of this Style.
        :rtype: bool
        """
        return self.container['shrink_to_fit']

    @shrink_to_fit.setter
    def shrink_to_fit(self, shrink_to_fit):
        """
        Sets the shrink_to_fit of this Style.

        :param shrink_to_fit: The shrink_to_fit of this Style.
        :type: bool
        """

        self.container['shrink_to_fit'] = shrink_to_fit

    @property
    def indent_level(self):
        """
        Gets the indent_level of this Style.

        :return: The indent_level of this Style.
        :rtype: int
        """
        return self.container['indent_level']

    @indent_level.setter
    def indent_level(self, indent_level):
        """
        Sets the indent_level of this Style.

        :param indent_level: The indent_level of this Style.
        :type: int
        """

        self.container['indent_level'] = indent_level

    @property
    def number(self):
        """
        Gets the number of this Style.

        :return: The number of this Style.
        :rtype: int
        """
        return self.container['number']

    @number.setter
    def number(self, number):
        """
        Sets the number of this Style.

        :param number: The number of this Style.
        :type: int
        """

        self.container['number'] = number

    @property
    def rotation_angle(self):
        """
        Gets the rotation_angle of this Style.

        :return: The rotation_angle of this Style.
        :rtype: int
        """
        return self.container['rotation_angle']

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """
        Sets the rotation_angle of this Style.

        :param rotation_angle: The rotation_angle of this Style.
        :type: int
        """

        self.container['rotation_angle'] = rotation_angle

    @property
    def pattern(self):
        """
        Gets the pattern of this Style.

        :return: The pattern of this Style.
        :rtype: str
        """
        return self.container['pattern']

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this Style.

        :param pattern: The pattern of this Style.
        :type: str
        """

        self.container['pattern'] = pattern

    @property
    def text_direction(self):
        """
        Gets the text_direction of this Style.

        :return: The text_direction of this Style.
        :rtype: str
        """
        return self.container['text_direction']

    @text_direction.setter
    def text_direction(self, text_direction):
        """
        Sets the text_direction of this Style.

        :param text_direction: The text_direction of this Style.
        :type: str
        """

        self.container['text_direction'] = text_direction

    @property
    def vertical_alignment(self):
        """
        Gets the vertical_alignment of this Style.

        :return: The vertical_alignment of this Style.
        :rtype: str
        """
        return self.container['vertical_alignment']

    @vertical_alignment.setter
    def vertical_alignment(self, vertical_alignment):
        """
        Sets the vertical_alignment of this Style.

        :param vertical_alignment: The vertical_alignment of this Style.
        :type: str
        """

        self.container['vertical_alignment'] = vertical_alignment

    @property
    def horizontal_alignment(self):
        """
        Gets the horizontal_alignment of this Style.

        :return: The horizontal_alignment of this Style.
        :rtype: str
        """
        return self.container['horizontal_alignment']

    @horizontal_alignment.setter
    def horizontal_alignment(self, horizontal_alignment):
        """
        Sets the horizontal_alignment of this Style.

        :param horizontal_alignment: The horizontal_alignment of this Style.
        :type: str
        """

        self.container['horizontal_alignment'] = horizontal_alignment

    @property
    def border_collection(self):
        """
        Gets the border_collection of this Style.

        :return: The border_collection of this Style.
        :rtype: list[Border]
        """
        return self.container['border_collection']

    @border_collection.setter
    def border_collection(self, border_collection):
        """
        Sets the border_collection of this Style.

        :param border_collection: The border_collection of this Style.
        :type: list[Border]
        """

        self.container['border_collection'] = border_collection

    @property
    def background_theme_color(self):
        """
        Gets the background_theme_color of this Style.

        :return: The background_theme_color of this Style.
        :rtype: ThemeColor
        """
        return self.container['background_theme_color']

    @background_theme_color.setter
    def background_theme_color(self, background_theme_color):
        """
        Sets the background_theme_color of this Style.

        :param background_theme_color: The background_theme_color of this Style.
        :type: ThemeColor
        """

        self.container['background_theme_color'] = background_theme_color

    @property
    def foreground_theme_color(self):
        """
        Gets the foreground_theme_color of this Style.

        :return: The foreground_theme_color of this Style.
        :rtype: ThemeColor
        """
        return self.container['foreground_theme_color']

    @foreground_theme_color.setter
    def foreground_theme_color(self, foreground_theme_color):
        """
        Sets the foreground_theme_color of this Style.

        :param foreground_theme_color: The foreground_theme_color of this Style.
        :type: ThemeColor
        """

        self.container['foreground_theme_color'] = foreground_theme_color

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
        if not isinstance(other, Style):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
