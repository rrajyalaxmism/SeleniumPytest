

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest

from Framework import read_csv_file
from pages.HomePage import Home


@pytest.mark.usefixtures("driver")
class Test_Simple_Search:

    def test_close_popups(self, driver):

        try:
            driver.find_element(By.CSS_SELECTOR, "svg.c-neutral-900").click()
        except NoSuchElementException:
            print("Start up dialog does not exists")

    def test_parameters_check(self, driver):
        filepath =r"Files\Test_data.csv"
        home_page = Home(driver)
        home_page.set_flight_search(driver, read_csv_file(filepath,'BLR'),read_csv_file(filepath,'DEL'))
        assert driver.find_element(By.XPATH, home_page.dropdown_trip_XPath).text == "Round trip"

    def test_search(self, driver):
        home_page = Home(driver)
        home_page.set_flight_search_and_click(driver, "BLR", "DEL")
