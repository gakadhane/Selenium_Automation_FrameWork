import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from test.pageObjects.pageObjectModel.VWO.freetrialpage import FreeTrialPage
from test.pageObjects.pageObjectModel.VWO.loginpage import LoginPage

from test.constants.constants import Constants
from test.utils.Utils import *


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


@allure.title("VWO Free Trail")
@allure.description("TC#0 - VWO Free Trail")
@allure.feature("Feature | VWO Free Trail")
@pytest.mark.negative
def test_vwo_ft_negative(setup):
    driver = setup
    login_page = LoginPage(driver=driver)
    login_page.free_trial_button_click()
    take_screen_shot(driver=driver, name="test_vwo_ft_negative")
    free_trial_page = FreeTrialPage(driver=driver)
    free_trial_page.enter_free_trial_details_invalid("admin")
    error_msg_text = free_trial_page.get_error_message_text()
    assert error_msg_text == "The email address you entered is incorrect."
