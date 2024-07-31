package ru.yandex.praktikum.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class ProfilePage {
    private final WebDriver driver;

    // Locators
    private final By constructorLink = By.xpath("//p[text()='Конструктор']");
    private final By logoLink = By.xpath("//div[contains(@class, 'AppHeader_header__logo__2D0X2')]");

    // Constructor
    public ProfilePage(WebDriver driver) {
        this.driver = driver;
    }

    // Method to click on "Конструктор"
    public void clickConstructorLink() {
        driver.findElement(constructorLink).click();
    }

    // Method to click on the Stellar Burgers logo
    public void clickLogo() {
        driver.findElement(logoLink).click();
    }
}
