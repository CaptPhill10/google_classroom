from selenium import webdriver
import undetected_chromedriver as uc
import pytest
from core.data.text_data import TextData
from core.config import TestConfig


@pytest.fixture(scope="module")
def driver():
    driver = uc.Chrome()
    options = uc.ChromeOptions()
    driver.maximize_window()

    yield driver

    driver.quit()

# @pytest.fixture(scope="module")
# def driver():
#     chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_argument('--no-sandbox')
#     # chrome_options.add_argument('--headless')
#     # chrome_options.add_argument('--disable-gpu')
#     # chrome_options.add_experimental_option(
#     #     'excludeSwitches', ['enable-automation']
#     # )
#     # chrome_options.add_argument('--disable-notifications')
#     # chrome_options.add_argument('--disable-popup-blocking')
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     yield driver
#
#     driver.quit()


@pytest.fixture(scope="module")
def test_config():
    test_cfg = TestConfig()
    return test_cfg


@pytest.fixture(scope="module")
def text_data(test_config):
    text_data = TextData(test_config=test_config)
    return text_data
