package ru.yandex.praktikum.pageobjects;

import io.qameta.allure.Step;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class RegisterPage {
    private WebDriver driver;

    public RegisterPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    @FindBy(xpath = "//label[text()='Имя']/following-sibling::input")
    private WebElement nameField;

    @FindBy(xpath = "//label[text()='Email']/following-sibling::input")
    private WebElement emailField;

    @FindBy(xpath = "//input[@name='Пароль']")
    private WebElement passwordField;

    @FindBy(xpath = "//button[text()='Зарегистрироваться']")
    private WebElement registerButton;

    @FindBy(xpath = "//a[text()='Войти']")
    private WebElement loginLink;

    @FindBy(xpath = "//p[text()='Некорректный пароль']")
    private WebElement invalidPasswordError;

    @Step("Enter name: {name}")
    public void enterName(String name) {
        nameField.sendKeys(name);
    }

    @Step("Enter email: {email}")
    public void enterEmail(String email) {
        emailField.sendKeys(email);
    }

    @Step("Enter password: {password}")
    public void enterPassword(String password) {
        passwordField.sendKeys(password);
    }

    @Step("Click register button")
    public void clickRegisterButton() {
        registerButton.click();
    }

    @Step("Click login button")
    public void clickLoginLink() {
        loginLink.click();
    }

    @Step("Register user with name: {name}, email: {email}, password: {password}")
    public void register(String name, String email, String password) {
        nameField.sendKeys(name);
        emailField.sendKeys(email);
        passwordField.sendKeys(password);
        registerButton.click();
    }

    public boolean isInvalidPasswordErrorDisplayed() {
        return invalidPasswordError.isDisplayed();
    }
}
