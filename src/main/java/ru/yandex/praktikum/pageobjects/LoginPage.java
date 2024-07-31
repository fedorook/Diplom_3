package ru.yandex.praktikum.pageobjects;

import io.qameta.allure.Step;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class LoginPage {
    private WebDriver driver;

    @FindBy(xpath = "//input[@name='name']")
    private WebElement emailField;

    @FindBy(xpath = "//input[@name='Пароль']")
    private WebElement passwordField;

    @FindBy(xpath = "//button[text()='Войти']")
    private WebElement loginButton;

    @FindBy(xpath = "//button[text()='Войти в аккаунт']")
    private WebElement loginButtonOnTheMainPage;

    @FindBy(xpath = "//p[text()='Личный Кабинет']")
    private WebElement personalAccountButton;

    @FindBy(xpath = "//a[text()='Профиль']")
    private WebElement profileLink;

    @FindBy(xpath = "//a[text()='Войти']")
    private WebElement registrationFormLoginButton;

    @FindBy(xpath = "//a[text()='Войти']")
    private WebElement forgotPasswordFormLoginButton;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    @Step("Login with email: {email} and password: {password}")
    public void login(String email, String password) {
        emailField.sendKeys(email);
        passwordField.sendKeys(password);
        loginButton.click();
    }

    @Step("Click on 'Личный кабинет' button")
    public void clickPersonalAccountButton() {
        personalAccountButton.click();
    }

    @Step("Click on 'Войти в аккаунт' button")
    public void clickLoginButtonOnTheMainPage() {
        loginButtonOnTheMainPage.click();
    }

    @Step("Click on the 'Войти' button in the registration form")
    public void clickRegistrationFormLoginButton() {
        registrationFormLoginButton.click();
    }

    @Step("Click on the 'Войти' button in the forgot password form")
    public void clickForgotPasswordFormLoginButton() {
        forgotPasswordFormLoginButton.click();
    }

    @Step("Check if user is logged in")
    public boolean isLoggedIn() {
        // Navigate to personal account page
        driver.get("https://stellarburgers.nomoreparties.site/account");

        // Wait for the profile link to be visible
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        try {
            wait.until(ExpectedConditions.visibilityOf(profileLink));
            return true;
        } catch (Exception e) {
            return false;
        }
    }
}
