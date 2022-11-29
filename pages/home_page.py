from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    logout_button = By.CSS_SELECTOR, '.controls__logout > span'
    side_menus = By.CSS_SELECTOR, '.aside__label'   

    def __init__(self, driver) -> None:
        self.driver = driver

    
    def logout(self):
        self.driver.find_element(*self.logout_button).click()
    

    def get_side_menus(self):
        side_menus = self.driver.find_elements(*self.side_menus)
        return {menu.text.lower() for menu in side_menus}