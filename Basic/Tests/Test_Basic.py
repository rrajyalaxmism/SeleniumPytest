from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
from Pages.HomePage import  *


@pytest.mark.usefixtures("driver")
class Test_Simple_Search:

    def test_close_popups(self, driver):

        try:
            driver.find_element(By.CSS_SELECTOR, "svg.c-neutral-900").click()
        except NoSuchElementException:
            print("Start up dialog does not exists")

    def test_search(self, driver):

        set_flight_search_and_click(driver,"BLR","DEL")



