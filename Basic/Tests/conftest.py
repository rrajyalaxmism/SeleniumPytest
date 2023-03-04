from selenium import webdriver
import time
import pytest


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    driver.get(r"https:\\www.Cleartrip.com")
    driver.maximize_window()
    time.sleep(2)
    yield driver
    driver.close()
    driver.quit()
