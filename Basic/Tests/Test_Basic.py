from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import pytest


@pytest.mark.usefixtures("driver")
class Test_Simple_Search:

    def test_close_popups(self, driver):

        try:
            driver.find_element(By.CSS_SELECTOR, "svg.c-neutral-900").click()
        except NoSuchElementException:
            print("Start up dialog does not exists")

    def test_search(self, driver):

        driver.find_element(By.XPATH, "//span[text()='One way']").click()
        driver.find_element(By.XPATH, "//li[@value='rt']").click()
