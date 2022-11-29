from selenium import webdriver
from time import sleep
from pages.login_page import LoginPage
from pages.home_page import HomePage
import pytest

def test_user_logout(user_setup):
    driver = user_setup
    home_page = HomePage(driver)
    home_page.logout()
    assert home_page.text_exists('Login')

def test_user_allowed_menus(user_setup):
    driver = user_setup
    home_page = HomePage(driver)
    sleep(5)
    actual_user_menus = home_page.get_side_menus()
    expected_user_menus = {'accounts', 'cards', 'transfers', 'reports', 'news', 'my profile'}
    diff = expected_user_menus.symmetric_difference(actual_user_menus)
    assert len(diff) == 0

def test_admin_allowed_menus(admin_setup):
    driver = admin_setup
    home_page = HomePage(driver)
    sleep(5)
    actual_admin_menus = home_page.get_side_menus()
    expected_admin_menus = {'accounts', 'messages', 'transfers', 'reports', 'news', 'profiles', 'requests', 'settings', 'system log'}
    diff = expected_admin_menus.symmetric_difference(actual_admin_menus)
    assert len(diff) == 0