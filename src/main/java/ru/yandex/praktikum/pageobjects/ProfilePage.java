package ru.yandex.praktikum.pageobjects;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class ProfilePage {
    private final WebDriver driver;

    // Locators
    private final By constructorLink = By.xpath("//p[text()='Конструктор']");
    private final By logoLink = By.xpath("//div[contains(@class, 'AppHeader_header__logo__2D0X2')]");
    private final By logoutButton = By.xpath("//button[text()='Выход']");


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

    // Method to click on the "Выйти" button
    public void clickLogoutButton() {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        wait.until(ExpectedConditions.visibilityOfElementLocated(logoutButton)); // Ожидание видимости кнопки
        driver.findElement(logoutButton).click();
    }

}
