package ru.yandex.praktikum.tests;

import io.qameta.allure.junit4.DisplayName;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import ru.yandex.praktikum.pageobjects.ProfilePage;
import utils.Urls;
import utils.WebDriverFactory;

import static org.junit.Assert.assertEquals;

public class ProfileNavigationTest {
    private WebDriver driver;
    private ProfilePage profilePage;

    @Before
    public void setUp() {
        driver = WebDriverFactory.getDriver();
        profilePage = new ProfilePage(driver);
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @DisplayName("Navigate to Main Page via Constructor link")
    public void navigateToMainPageViaConstructorLinkTest() {
        // Navigate to the Login Page
        driver.get(Urls.LOGIN_PAGE_URL);

        // Click on the "Constructor" link and verify navigation to the Main Page
        profilePage.clickConstructorLink();
        assertEquals("Should navigate to the Main Page", Urls.MAIN_PAGE_URL, driver.getCurrentUrl());
    }

    @Test
    @DisplayName("Navigate to Main Page via logo")
    public void navigateToMainPageViaLogoTest() {
        // Navigate to the Login Page
        driver.get(Urls.LOGIN_PAGE_URL);

        // Click on the logo and verify navigation to the Main Page
        profilePage.clickLogo();
        assertEquals("Should navigate to the Main Page", Urls.MAIN_PAGE_URL, driver.getCurrentUrl());
    }
}
