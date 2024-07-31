package ru.yandex.praktikum.utils;

import io.restassured.RestAssured;
import io.restassured.response.Response;

public class ApiUtils {

    private static final String BASE_URL = "https://stellarburgers.nomoreparties.site/api/";

    public static String createUser(String name, String email, String password) {
        String createUserEndpoint = BASE_URL + "auth/register";

        String requestBody = String.format("{\"name\":\"%s\",\"email\":\"%s\",\"password\":\"%s\"}", name, email, password);

        System.out.println("Creating user with name: " + name + " email: " + email);
        System.out.println("Request body: " + requestBody);
        System.out.println("Endpoint: " + createUserEndpoint);

        Response response = RestAssured
                .given()
                .header("Content-Type", "application/json")
                .body(requestBody)
                .post(createUserEndpoint)
                .andReturn();

        System.out.println("Response status code: " + response.getStatusCode());
        System.out.println("Response body: " + response.getBody().asString());

        if (response.getStatusCode() != 200) {
            throw new RuntimeException("Failed to create user: " + response.getBody().asString());
        }

        return response.jsonPath().getString("accessToken");
    }

    public static String loginAndGetToken(String email, String password) {
        String loginEndpoint = BASE_URL + "auth/login";

        String requestBody = String.format("{\"email\":\"%s\",\"password\":\"%s\"}", email, password);

        Response response = RestAssured
                .given()
                .header("Content-Type", "application/json")
                .body(requestBody)
                .post(loginEndpoint)
                .andReturn();

        if (response.getStatusCode() == 200) {
            return response.jsonPath().getString("accessToken");
        }

        throw new RuntimeException("Failed to login: " + response.getBody().asString());
    }

    public static void deleteUser(String accessToken) {
        String deleteUserEndpoint = BASE_URL + "auth/user";

        RestAssured
                .given()
                .header("Content-Type", "application/json")
                .header("Authorization", accessToken)
                .delete(deleteUserEndpoint)
                .andReturn();
    }
}
