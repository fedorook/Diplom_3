import allure
from src import HttpMethods, URLS


class ApiUser:
    def __init__(self, api_client):
        self.client = api_client

    @allure.step("Send login request for a user")
    def login_user(self, data, **kwargs):
        return self.client.send_request(
            HttpMethods.POST,
            URLS.LOGIN_ENDPOINT,
            json=data,
            **kwargs
        )

    @allure.step("Send registration request to create a new user")
    def create_user(self, data, **kwargs):
        return self.client.send_request(
            HttpMethods.POST,
            URLS.REGISTRATION_ENDPOINT,
            json=data,
            **kwargs
        )

    @allure.step("Send PATCH request to update user data")
    def update_userdata(self, data, **kwargs):
        return self.client.send_request(
            HttpMethods.PATCH,
            URLS.USER_ENDPOINT,
            json=data,
            **kwargs
        )

    @allure.step("Send DELETE request to remove a user")
    def delete_user(self, **kwargs):
        return self.client.send_request(
            HttpMethods.DELETE,
            URLS.DELETE_ENDPOINT,
            **kwargs
        )
