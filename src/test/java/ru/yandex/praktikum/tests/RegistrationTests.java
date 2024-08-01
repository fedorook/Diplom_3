package ru.yandex.praktikum.tests;

import io.qameta.allure.junit4.DisplayName;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import ru.yandex.praktikum.pageobjects.RegisterPage;
import utils.ApiUtils;
import utils.WebDriverFactory;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

public class RegistrationTests {
    private WebDriver driver;
    private RegisterPage registerPage;

    @Before
    public void setUp() {
        driver = WebDriverFactory.getDriver();
        driver.get("https://stellarburgers.nomoreparties.site/register");
        registerPage = new RegisterPage(driver);
    }


    @After
    public void tearDown() {
        // Closing the browser after the test
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @DisplayName("Successful Registration")
    public void successfulRegistrationTest() {
        String email = "testuser" + System.currentTimeMillis() + "@example.com";
        String password = "password123";
        registerPage.register("Test User", email, password);

        // Verify successful registration by logging in via API
        String accessToken = ApiUtils.loginAndGetToken(email, password);
        assertNotNull("User should be able to login with the registered credentials", accessToken);

        // Clean up: delete the user via API
        ApiUtils.deleteUser(accessToken);
    }


    @Test
    @DisplayName("Error on registration with invalid password")
    public void errorOnInvalidPasswordTest() {
        registerPage.register("Test User", "testuser@example.com", "123");
        assertTrue("Error message for invalid password is not displayed", registerPage.isInvalidPasswordErrorDisplayed());
    }
}
