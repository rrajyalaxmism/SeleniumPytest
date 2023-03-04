from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import pytest


class Test_Simple_Search:

    @pytest.fixture(scope='class')
    def driver(self):
        driver = webdriver.Chrome()
        driver.get(r"https:\\www.Cleartrip.com")
        driver.maximize_window()
        time.sleep(2)
        yield driver
        driver.close()
        driver.quit()

    def test_close_popups(self, driver):

        try:
            driver.find_element(By.CSS_SELECTOR, "svg.c-neutral-900").click()
        except NoSuchElementException:
            print("Start up dialog does not exists")

    def test_search(self, driver):

        driver.find_element(By.XPATH, "//span[text()='One way']").click()
        driver.find_element(By.XPATH, "//li[@value='rt']").click()
