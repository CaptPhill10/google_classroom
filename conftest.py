from selenium import webdriver
import undetected_chromedriver as uc
import pytest
from core.config import TestConfig


@pytest.fixture(scope="module")
def driver():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    driver = uc.Chrome()
    options = uc.ChromeOptions()
    # driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    
    driver.quit()


@pytest.fixture(scope="module")
def test_config():
    test_cfg = TestConfig()
    return test_cfg
