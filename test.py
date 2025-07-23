```
import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "edge"])
def browser(request):
    if request.param == "chrome":
       driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif request.param == "firefox":
       driver = webdriver.Firefox(executable_path="drivers/geckodriver")
    elif request.param == "edge":
       driver = webdriver.Edge(executable_path="drivers/msedgedriver")
    else:
       raise ValueError(f"Unsupported browser: {request.param}")
       driver.maximize_window()
       yield driver
       driver.quit()
```
