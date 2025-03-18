import os

import allure
import pytest

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from test.constants.constants import Constants
from test.pageObjects.pageObjectModel.VWO.dashboardpage import DashboardPage
from test.pageObjects.pageObjectModel.VWO.loginpage import LoginPage
from test.utils.Utils import *

from Selenium_Automation_FrameWork.test.utils.Utils import take_screen_shot


# Assertions and use the Page Object class
# Webdriver Start
# User Interaction + Assertions
# Close Webdriver


@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.app_url())
    return driver


@allure.title("VWO Login Test")
@allure.description("TC#0 - VWO App Negative Test")
@allure.feature("Feature | VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("INVALID_USERNAME"), pwd=os.getenv("INVALID_PASSWORD"))
    error_msg_element = login_page.get_error_message_text()
    take_screen_shot(driver=driver, name="test_vwo_login_negative")
    assert error_msg_element == os.getenv("error_message_expected")


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("USERNAME"), pwd=os.getenv("PASSWORD"))
    dashboard_page = DashboardPage(driver=driver)
    take_screen_shot(driver=driver, name="test_vwo_login_positive")
    assert os.getenv("USERNAME_LOGGED_IN") in dashboard_page.user_logged_in_text()
