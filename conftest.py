from selenium import webdriver
import undetected_chromedriver as uc
import pytest
from core.config import TestConfig


@pytest.fixture(scope="module")
def driver():
    driver = uc.Chrome()
    options = uc.ChromeOptions()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture(scope="module")
def test_config():
    test_cfg = TestConfig()
    return test_cfg
