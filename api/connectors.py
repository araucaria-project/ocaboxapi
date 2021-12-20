import random
from typing import Iterable, Callable

import requests

from api.exceptions import NotImplementedMethodError, NumericError, ErrorMessage
from api.observatory import Component


class Connector:
    @classmethod
    def create_connector(cls, protocol: str, *args, **kwargs) -> 'Connector':
        """Factory method, crates specialized Connector instance"""
        connector = _connector_classes[protocol](*args, **kwargs)
        return connector

    def get(self, component: Component, variable: str, **data):
        raise NotImplementedMethodError

    def put(self, component: Component, variable: str, **data):
        raise NotImplementedMethodError

    def call(self, component: Component, function: str, **data):
        raise NotImplementedMethodError

    def subscribe(self, variables: Iterable[str, str], callback: Callable):
        raise NotImplementedMethodError


class AlpacaConnector(Connector):
    def __init__(self) -> None:
        self.client_id = random.randint(0, 4294967295)
        self.session_id = 0
        super().__init__()

    def connect(*args, **kwargs):
        pass

    def configure_components(self):
        pass

    def get(self, component: Component, variable: str, **data):
        """Send an HTTP GET request to an Alpaca server and check response for errors.

        Args:
            component (Component): Calling component
            variable (str): Attribute to get from server.

        """
        url = self._url(component=component, variable=variable)
        data.update(self._base_data_for_request())
        response = requests.get(url, data=data)
        self.__check_error(response)
        return response.json()["Value"]

    def put(self, component: Component, variable: str, **data):
        """Send an HTTP PUT request to an Alpaca server and check response for errors.

        Args:
            component (Component): Calling component
            variable (str): Attribute to set on server.
            **data: Data to send with request.

        """
        url = self._url(component=component, variable=variable)
        data.update(self._base_data_for_request())
        response = requests.put(url, data=data)
        self.__check_error(response)
        return response.json()

    def _base_data_for_request(self):
        self.session_id += 1
        return {
            'ClientID': self.client_id,
            'ClientTransactionID': self.session_id
        }

    @staticmethod
    def _url(component: Component, variable: str):
        url = '/'.join([
            component.get_option_recursive('address'),
            component.component_options['kind'],
            str(component.component_options.get('device_number', 0)),
            variable
        ])
        return url

    @staticmethod
    def __check_error(response: requests.Response):
        """Check response from Alpaca server for Errors.

        Args:
            response (Response): Response from Alpaca server to check.

        """
        j = response.json()
        if j["ErrorNumber"] != 0:
            raise NumericError(j["ErrorNumber"], j["ErrorMessage"])
        elif response.status_code == 400 or response.status_code == 500:
            raise ErrorMessage(j["Value"])


_connector_classes = {
    'alpaca': AlpacaConnector
}
