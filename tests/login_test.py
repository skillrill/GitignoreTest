from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

def test_landing_page(setup):
    driver = setup
    sleep(5)
    assert driver.title == 'EBANQ'

def test_user_login(user_setup):
    driver = user_setup
    home_page = HomePage(driver)
    assert home_page.text_exists('logout')

def test_admin_login(admin_setup):
    driver = admin_setup
    home_page = HomePage(driver)
    assert home_page.text_exists('logout')

invalid_login_data = [
    ('', '', 'Field is required'),
    ('test', 'test', 'Wrong username or password')
    # ('abc', 'test', 'Should be minimum 4 chars'),
    # ('', 'test', 'Field is required'),
    # ('test', '', 'Field is required')
]

@pytest.mark.parametrize("username, password, checkpoint", invalid_login_data)
def test_invalid_authentication(setup, username, password, checkpoint):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.text_exists(checkpoint)