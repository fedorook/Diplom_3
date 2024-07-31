package ru.yandex.praktikum.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class TabsPage {

    private final WebDriver driver;

    // Locators for the tabs
    private final By bunsTab = By.xpath("//span[text()='Булки']");
    private final By saucesTab = By.xpath("//span[text()='Соусы']");
    private final By fillingsTab = By.xpath("//span[text()='Начинки']");

    // Locators for the active tabs
    private final By activeBunsTab = By.xpath("//div[contains(@class, 'tab_type_current') and span[text()='Булки']]");
    private final By activeSaucesTab = By.xpath("//div[contains(@class, 'tab_type_current') and span[text()='Соусы']]");
    private final By activeFillingsTab = By.xpath("//div[contains(@class, 'tab_type_current') and span[text()='Начинки']]");

    public TabsPage(WebDriver driver) {
        this.driver = driver;
    }

    // Methods to click on the tabs
    public void clickBunsTab() {
        WebElement element = driver.findElement(bunsTab);
        ((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);
    }


    public void clickSaucesTab() {
        driver.findElement(saucesTab).click();
    }

    public void clickFillingsTab() {
        driver.findElement(fillingsTab).click();
    }

    // Methods to check if the tab is active
    public boolean isBunsTabActive() {
        return driver.findElement(activeBunsTab).isDisplayed();
    }

    public boolean isSaucesTabActive() {
        return driver.findElement(activeSaucesTab).isDisplayed();
    }

    public boolean isFillingsTabActive() {
        return driver.findElement(activeFillingsTab).isDisplayed();
    }
}
