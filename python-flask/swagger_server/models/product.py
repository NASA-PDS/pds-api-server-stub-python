# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.metadata import Metadata  # noqa: F401,E501
from swagger_server.models.reference import Reference  # noqa: F401,E501
from swagger_server import util


class Product(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, _class: str=None, title: str=None, description: str=None, start_date_time: str=None, stop_date_time: str=None, observing_system_components: List[Reference]=None, targets: List[Reference]=None, metadata: Metadata=None, properties: Dict[str, object]=None):  # noqa: E501
        """Product - a model defined in Swagger

        :param id: The id of this Product.  # noqa: E501
        :type id: str
        :param _class: The _class of this Product.  # noqa: E501
        :type _class: str
        :param title: The title of this Product.  # noqa: E501
        :type title: str
        :param description: The description of this Product.  # noqa: E501
        :type description: str
        :param start_date_time: The start_date_time of this Product.  # noqa: E501
        :type start_date_time: str
        :param stop_date_time: The stop_date_time of this Product.  # noqa: E501
        :type stop_date_time: str
        :param observing_system_components: The observing_system_components of this Product.  # noqa: E501
        :type observing_system_components: List[Reference]
        :param targets: The targets of this Product.  # noqa: E501
        :type targets: List[Reference]
        :param metadata: The metadata of this Product.  # noqa: E501
        :type metadata: Metadata
        :param properties: The properties of this Product.  # noqa: E501
        :type properties: Dict[str, object]
        """
        self.swagger_types = {
            'id': str,
            '_class': str,
            'title': str,
            'description': str,
            'start_date_time': str,
            'stop_date_time': str,
            'observing_system_components': List[Reference],
            'targets': List[Reference],
            'metadata': Metadata,
            'properties': Dict[str, object]
        }

        self.attribute_map = {
            'id': 'id',
            '_class': 'class',
            'title': 'title',
            'description': 'description',
            'start_date_time': 'start_date_time',
            'stop_date_time': 'stop_date_time',
            'observing_system_components': 'observing_system_components',
            'targets': 'targets',
            'metadata': 'metadata',
            'properties': 'properties'
        }
        self._id = id
        self.__class = _class
        self._title = title
        self._description = description
        self._start_date_time = start_date_time
        self._stop_date_time = stop_date_time
        self._observing_system_components = observing_system_components
        self._targets = targets
        self._metadata = metadata
        self._properties = properties

    @classmethod
    def from_dict(cls, dikt) -> 'Product':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The product of this Product.  # noqa: E501
        :rtype: Product
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Product.

        identifier lidvid of the collection  # noqa: E501

        :return: The id of this Product.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Product.

        identifier lidvid of the collection  # noqa: E501

        :param id: The id of this Product.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def _class(self) -> str:
        """Gets the _class of this Product.


        :return: The _class of this Product.
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class: str):
        """Sets the _class of this Product.


        :param _class: The _class of this Product.
        :type _class: str
        """

        self.__class = _class

    @property
    def title(self) -> str:
        """Gets the title of this Product.


        :return: The title of this Product.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Product.


        :param title: The title of this Product.
        :type title: str
        """

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Product.


        :return: The description of this Product.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Product.


        :param description: The description of this Product.
        :type description: str
        """

        self._description = description

    @property
    def start_date_time(self) -> str:
        """Gets the start_date_time of this Product.

        start date time of the observations in ISO8601  # noqa: E501

        :return: The start_date_time of this Product.
        :rtype: str
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time: str):
        """Sets the start_date_time of this Product.

        start date time of the observations in ISO8601  # noqa: E501

        :param start_date_time: The start_date_time of this Product.
        :type start_date_time: str
        """

        self._start_date_time = start_date_time

    @property
    def stop_date_time(self) -> str:
        """Gets the stop_date_time of this Product.

        stop date time of the observations in ISO8601  # noqa: E501

        :return: The stop_date_time of this Product.
        :rtype: str
        """
        return self._stop_date_time

    @stop_date_time.setter
    def stop_date_time(self, stop_date_time: str):
        """Sets the stop_date_time of this Product.

        stop date time of the observations in ISO8601  # noqa: E501

        :param stop_date_time: The stop_date_time of this Product.
        :type stop_date_time: str
        """

        self._stop_date_time = stop_date_time

    @property
    def observing_system_components(self) -> List[Reference]:
        """Gets the observing_system_components of this Product.

        list of instruments or procedures generating the data (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :return: The observing_system_components of this Product.
        :rtype: List[Reference]
        """
        return self._observing_system_components

    @observing_system_components.setter
    def observing_system_components(self, observing_system_components: List[Reference]):
        """Sets the observing_system_components of this Product.

        list of instruments or procedures generating the data (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :param observing_system_components: The observing_system_components of this Product.
        :type observing_system_components: List[Reference]
        """

        self._observing_system_components = observing_system_components

    @property
    def targets(self) -> List[Reference]:
        """Gets the targets of this Product.

        identifier lidvid of the target of or feature of interest the observation (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :return: The targets of this Product.
        :rtype: List[Reference]
        """
        return self._targets

    @targets.setter
    def targets(self, targets: List[Reference]):
        """Sets the targets of this Product.

        identifier lidvid of the target of or feature of interest the observation (for concept see https://en.wikipedia.org/wiki/Observations_and_Measurements)  # noqa: E501

        :param targets: The targets of this Product.
        :type targets: List[Reference]
        """

        self._targets = targets

    @property
    def metadata(self) -> Metadata:
        """Gets the metadata of this Product.


        :return: The metadata of this Product.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: Metadata):
        """Sets the metadata of this Product.


        :param metadata: The metadata of this Product.
        :type metadata: Metadata
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def properties(self) -> Dict[str, object]:
        """Gets the properties of this Product.


        :return: The properties of this Product.
        :rtype: Dict[str, object]
        """
        return self._properties

    @properties.setter
    def properties(self, properties: Dict[str, object]):
        """Sets the properties of this Product.


        :param properties: The properties of this Product.
        :type properties: Dict[str, object]
        """

        self._properties = properties
