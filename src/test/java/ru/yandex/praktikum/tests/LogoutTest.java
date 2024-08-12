package ru.yandex.praktikum.tests;

import io.qameta.allure.junit4.DisplayName;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import ru.yandex.praktikum.pageobjects.LoginPage;
import ru.yandex.praktikum.pageobjects.MainPage;
import ru.yandex.praktikum.pageobjects.ProfilePage;
import utils.ApiUtils;
import utils.Urls;
import utils.WebDriverFactory;

import java.time.Duration;

import static org.junit.Assert.assertTrue;

public class LogoutTest {
    private WebDriver driver;
    private ApiUtils apiUtils;

    @Before
    public void setUp() {
        // Initialize WebDriver and ApiUtils objects
        driver = WebDriverFactory.getDriver();
        apiUtils = new ApiUtils();
    }

    @After
    public void tearDown() {
        // Clean up: Delete the user and close the browser
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @DisplayName("Logout from Personal Account")
    public void logoutTest() {
        // Step 1: Register a new user
        String timestamp = String.valueOf(System.currentTimeMillis());
        String email = "testuser" + timestamp + "@example.com";
        String password = "password123";
        String name = "Test User";

        ApiUtils.createUser(name, email, password);

        // Step 2: Login with the newly created user
        driver.get(Urls.LOGIN_PAGE_URL);
        LoginPage loginPage = new LoginPage(driver);
        loginPage.login(email, password);

        // Step 3: Navigate to the personal account
        MainPage mainPage = new MainPage(driver);
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {
            WebElement overlay = wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("Modal_modal_overlay__x2ZCr")));
            overlay.click();
        } catch (TimeoutException e) {
        }

        mainPage.clickAccountButton();

        // Step 4: Logout from the personal account
        ProfilePage profilePage = new ProfilePage(driver);
        profilePage.clickLogoutButton();

        // Step 5: Assert that the user is logged out
        wait.until(ExpectedConditions.urlToBe(Urls.LOGIN_PAGE_URL));
        assertTrue("User should be logged out", loginPage.isAt());
    }
}
