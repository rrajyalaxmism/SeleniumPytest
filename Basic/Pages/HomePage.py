from selenium.webdriver.common.by import By

dropdown_trip_XPath = "//span[contains(text(),'One way') or contains(text(),'Round')]"
list_round_trip_XPath = "//li[@value='rt']"
location_from_XPath = "//input[@placeholder ='Where from?']"
location_to_XPath = "//input[@placeholder ='Where to?']"
search_flights_XPath = "//span[text()='Search flights']"


def set_flight_search(driver, location_from, location_to):
    driver.find_element(By.XPATH, dropdown_trip_XPath).click()
    driver.find_element(By.XPATH, list_round_trip_XPath).click()
    driver.find_element(By.XPATH, location_from_XPath).send_keys(location_from)
    driver.find_element(By.XPATH, "//ul/li/div/div/div[contains(text()," + location_from + ")]").click()
    driver.find_element(By.XPATH, location_to_XPath).send_keys(location_to)
    driver.find_element(By.XPATH, "//ul/li/div/div/div[contains(text()," + location_to + ")]").click()


def set_flight_search_and_click(driver, location_from, location_to):
    set_flight_search(driver, location_from, location_to)
    driver.find_element(By.XPATH, search_flights_XPath).click()