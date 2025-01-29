from selenium.webdriver.common.by import By
from test.utils.common_utils import webdriver_wait

# Dashboard Page Class
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    user_logged_in = (By.XPATH, "//span[@data-qa='lufexuloga']")

    # Page Actions
    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_logged_in_text(self):
        webdriver_wait(driver=self.driver, element_tuple=self.user_logged_in, timeout=15)
        return self.get_user_logged_in().text
