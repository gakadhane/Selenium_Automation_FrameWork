from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium import webdriver
from selenium.webdriver.common import by


def test_app_vwo_login_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get ("https://www.magicbricks.com/")
    driver.findelement(by.xpath,"//a[@class='mb-header__sub__tabs__link js-menu-link']").click()
    driver.findelement(by.xpath, "//a[@onclick='openRentUrlInNewTab']")