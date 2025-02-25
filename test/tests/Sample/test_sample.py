import allure
import pytest


@allure.title("Dry run of the Framework 1")
@allure.description("Verify that Dry run is working")
@allure.feature("TC#1 - Sample Test Run.")
@pytest.mark.sample
def test_sample_pass():
    print("Hello Sample")
    assert True == True


@allure.title("Dry run of the Framework 2")
@allure.description("Verify that Dry run is working 2")
@allure.feature("TC#2 - Sample Failed Run. ")
@pytest.mark.sample
def test_sample_fail():
    print("Hello Sample")
    assert True == False
