from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL_SUBSTRING = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"  # строка, которая должна содержаться в URL страницы

    # Новые селекторы для форм регистрации и логина
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASSWORD = (By.NAME, "login-password")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASSWORD = (By.NAME, "registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")