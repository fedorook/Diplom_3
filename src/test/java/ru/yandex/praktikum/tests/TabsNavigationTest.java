package ru.yandex.praktikum.tests;

import io.qameta.allure.junit4.DisplayName;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import ru.yandex.praktikum.pageobjects.TabsPage;
import utils.Urls;
import utils.WebDriverFactory;

import static org.junit.Assert.assertTrue;

public class TabsNavigationTest {

    private WebDriver driver;
    private TabsPage tabsPage;

    @Before
    public void setUp() {
        driver = WebDriverFactory.getDriver();
        driver.get(Urls.MAIN_PAGE_URL);
        tabsPage = new TabsPage(driver);
    }

    @After
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    @Test
    @DisplayName("Check Buns tab navigation")
    public void checkBunsTabNavigation() {
        tabsPage.clickBunsTab();
        assertTrue("Buns tab should be active", tabsPage.isBunsTabActive());
    }

    @Test
    @DisplayName("Check Sauces tab navigation")
    public void checkSaucesTabNavigation() {
        tabsPage.clickSaucesTab();
        assertTrue("Sauces tab should be active", tabsPage.isSaucesTabActive());
    }

    @Test
    @DisplayName("Check Fillings tab navigation")
    public void checkFillingsTabNavigation() {
        tabsPage.clickFillingsTab();
        assertTrue("Fillings tab should be active", tabsPage.isFillingsTabActive());
    }
}
