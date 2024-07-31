package ru.yandex.praktikum.tests;

import io.qameta.allure.junit4.DisplayName;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import ru.yandex.praktikum.pageobjects.LoginPage;
import ru.yandex.praktikum.utils.ApiUtils;
import ru.yandex.praktikum.utils.Urls;
import ru.yandex.praktikum.utils.WebDriverFactory;

import static org.junit.Assert.assertTrue;

public class LoginTests {
    private WebDriver driver;
    private LoginPage loginPage;
    private String userToken;
    private String email;
    private final String password = "password123";
    private final String name = "Test User";

    @Before
    public void setUp() {
        // Generate unique email
        email = "testuser" + System.currentTimeMillis() + "@example.com";
        // Create user through API
        userToken = ApiUtils.createUser(name, email, password);

        // Get the browser type from system properties
        String browser = System.getProperty("browser", "chrome");

        // Initialize WebDriver
        driver = WebDriverFactory.getDriver();
        loginPage = new LoginPage(driver);
    }

    @After
    public void tearDown() {
        // Close browser after test
        if (driver != null) {
            driver.quit();
        }
        // Delete user through API
        if (userToken != null) {
            ApiUtils.deleteUser(userToken);
        }
    }

    @Test
    @DisplayName("Login via 'Войти в аккаунт' button on main page")
    public void loginViaMainPageLoginButtonTest() {
        driver.get(Urls.MAIN_PAGE_URL);
        loginPage.clickLoginButtonOnTheMainPage();
        loginPage.login(email, password);
        // Check if user is logged in by verifying the presence of a specific element
        assertTrue("User should be logged in", loginPage.isLoggedIn());
    }

    @Test
    @DisplayName("Login via Personal Account button on Login page")
    public void loginViaPersonalAccountLoginButtonTest() {
        driver.get(Urls.LOGIN_PAGE_URL);
        loginPage.clickPersonalAccountButton();
        loginPage.login(email, password);
        assertTrue("User should be logged in", loginPage.isLoggedIn());
    }

    @Test
    @DisplayName("Login via button on Registration form")
    public void loginViaRegistrationFormButtonTest() {
        driver.get(Urls.REGISTRATION_PAGE_URL);
        loginPage.clickPersonalAccountButton();
        loginPage.login(email, password);
        assertTrue("User should be logged in", loginPage.isLoggedIn());
    }

    @Test
    @DisplayName("Login via button on Forgot Password form")
    public void loginViaForgotPasswordFormButtonTest() {
        driver.get(Urls.FORGOT_PASSWORD_PAGE_URL);
        loginPage.clickPersonalAccountButton();
        loginPage.login(email, password);
        assertTrue("User should be logged in", loginPage.isLoggedIn());
    }

}
