from selenium.webdriver.common.by import By


class Home(object):

    def __init__(self, driver):
        self.driver = driver
        self.dropdown_trip_XPath = "//span[contains(text(),'One way') or contains(text(),'Round')]"
        self.list_round_trip_XPath = "//li[@value='rt']"
        self.location_from_XPath = "//input[@placeholder ='Where from?']"
        self.location_to_XPath = "//input[@placeholder ='Where to?']"
        self.search_flights_XPath = "//span[text()='Search flights']"

    def set_flight_search(self,driver, location_from, location_to):
        driver.find_element(By.XPATH, self.dropdown_trip_XPath).click()
        driver.find_element(By.XPATH, self.list_round_trip_XPath).click()
        driver.find_element(By.XPATH, self.location_from_XPath).send_keys(location_from)
        driver.find_element(By.XPATH, "//ul/li/div/div/div[contains(text()," + location_from + ")]").click()
        driver.find_element(By.XPATH, self.location_to_XPath).send_keys(location_to)
        driver.find_element(By.XPATH, "//ul/li/div/div/div[contains(text()," + location_to + ")]").click()

    def set_flight_search_and_click(self,driver, location_from, location_to):
        self.set_flight_search(driver, location_from, location_to)
        driver.find_element(By.XPATH, self.search_flights_XPath).click()
