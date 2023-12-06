from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_ADDRESS_LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "div.login_form button.btn-lg")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_REGISTER = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "div.register_form button.btn-lg")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".breadcrumb .active")
    PRODUCT_NAME_IN_ALERT = (By.XPATH, ("//div[@id='messages']//div[@class='alertinner ']//strong"))
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_VALUE = (By.XPATH, ("//div[@class='basket-mini pull-right hidden-xs']"))

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(2)")

