package ru.yandex.praktikum.pageobjects;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class MainPage {

    private WebDriver driver;

    // Локаторы для элементов страницы
    @FindBy(xpath = "//button[text()='Войти в аккаунт']")
    private WebElement loginButton;

    @FindBy(xpath = "//p[text()='Личный Кабинет']")
    private WebElement accountButton;

    @FindBy(xpath = "//p[text()='Конструктор']")
    private WebElement constructorButton;

    // Конструктор класса
    public MainPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    // Методы взаимодействия с элементами страницы
    public void clickLoginButton() {
        loginButton.click();
    }

    public void clickAccountButton() {
        accountButton.click();
    }

    public void clickConstructorButton() {
        constructorButton.click();
    }
}
