from enum import Enum

import requests


class HttpMethods(Enum):
    """
    Enumeration of supported HTTP methods.
    """

    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"


class ApiClient:
    """
    A simple API client for making HTTP requests to a base URL.
    """

    def __init__(self, base_url: str):
        """
        Initialize the client with the given base URL.

        :param base_url: The root URL for all API requests.
        """
        self.url = base_url

    def _create_url(self, endpoint: str) -> str:
        """
        Build the full URL for a given endpoint path.

        :param endpoint: Relative path or endpoint key.
        :return: A full URL string.
        """
        return f"{self.url}/{endpoint}"

    def send_request(
        self,
        method: HttpMethods,
        endpoint: str,
        **kwargs
    ) -> requests.Response:
        """
        Dispatch an HTTP request using the specified method to the target endpoint.

        :param method: An HttpMethods enum member.
        :param endpoint: The API endpoint path.
        :param kwargs: Additional keyword args passed to requests.request().
        :return: The Response object from the HTTP call.
        """
        full_url = self._create_url(endpoint)
        return requests.request(
            method.value,
            full_url,
            **kwargs
        )