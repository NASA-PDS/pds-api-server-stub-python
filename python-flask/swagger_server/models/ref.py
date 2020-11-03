# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Ref(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, title: str=None, ref: str=None, type: str=None, description: str=None):  # noqa: E501
        """Ref - a model defined in Swagger

        :param title: The title of this Ref.  # noqa: E501
        :type title: str
        :param ref: The ref of this Ref.  # noqa: E501
        :type ref: str
        :param type: The type of this Ref.  # noqa: E501
        :type type: str
        :param description: The description of this Ref.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'title': str,
            'ref': str,
            'type': str,
            'description': str
        }

        self.attribute_map = {
            'title': 'title',
            'ref': 'ref',
            'type': 'type',
            'description': 'description'
        }
        self._title = title
        self._ref = ref
        self._type = type
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Ref':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ref of this Ref.  # noqa: E501
        :rtype: Ref
        """
        return util.deserialize_model(dikt, cls)

    @property
    def title(self) -> str:
        """Gets the title of this Ref.

        name to display for the external reference  # noqa: E501

        :return: The title of this Ref.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Ref.

        name to display for the external reference  # noqa: E501

        :param title: The title of this Ref.
        :type title: str
        """

        self._title = title

    @property
    def ref(self) -> str:
        """Gets the ref of this Ref.

        external reference, here lidvid urn  # noqa: E501

        :return: The ref of this Ref.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref: str):
        """Sets the ref of this Ref.

        external reference, here lidvid urn  # noqa: E501

        :param ref: The ref of this Ref.
        :type ref: str
        """
        if ref is None:
            raise ValueError("Invalid value for `ref`, must not be `None`")  # noqa: E501

        self._ref = ref

    @property
    def type(self) -> str:
        """Gets the type of this Ref.

        type of the external reference, can be displayed as an icon for example  # noqa: E501

        :return: The type of this Ref.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Ref.

        type of the external reference, can be displayed as an icon for example  # noqa: E501

        :param type: The type of this Ref.
        :type type: str
        """

        self._type = type

    @property
    def description(self) -> str:
        """Gets the description of this Ref.

        longer description for the external reference, can be displayed in a tooltip  # noqa: E501

        :return: The description of this Ref.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Ref.

        longer description for the external reference, can be displayed in a tooltip  # noqa: E501

        :param description: The description of this Ref.
        :type description: str
        """

        self._description = description
