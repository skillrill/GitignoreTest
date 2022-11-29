from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from configs import config

class LoginPage(BasePage):

    # class attributes
    username_field = By.CSS_SELECTOR, "[type='email']"
    password_field = By.CSS_SELECTOR, "[type='password']"
    submit_button = By.CSS_SELECTOR, "[type='submit']"


    # constructor method
    def __init__(self, driver) -> None:
        self.driver = driver
    

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
    
    
    def user_login(self):
        self.login(config.USER, config.USER_PASSWORD)
    

    def admin_login(self):
        self.login(config.ADMIN, config.ADMIN_PASSWORD)