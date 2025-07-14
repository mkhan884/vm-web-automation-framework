from selenium.webdriver.common.by import By
from .base_page import BasePage
from .delivery_details_page import DeliveryDetailsPage
import time
import allure

class AddressPage(BasePage):
    PAGE_HEADER = (By.XPATH, "//span[contains(text(), \"We'll deliver your SIM\")]")
    SEARCH_BAR = (By.ID, "map_search_box")
    MAP = (By.CSS_SELECTOR, '.vmo-map')
    ADDRESS = (By.XPATH, "//li[contains(text(), 'Dubai Design District')]")
    DELIVER_BTN = (By.XPATH, "//button[text()='Deliver here']")

    @allure.step("Verify the address page header, searchbar and map")
    def verify_address_page(self):
        header = self.find(self.PAGE_HEADER)
        search = self.find(self.SEARCH_BAR)
        map = self.find(self.MAP)
        assert header.is_displayed() and search.is_displayed() and map.is_displayed()

    @allure.step("Enter delivery address in search bar.")
    def enter_address(self):
        search_bar = self.find(self.SEARCH_BAR)
        for char in 'Design district':
            search_bar.send_keys(char)
            time.sleep(0.5)
        self.click(self.ADDRESS)
        time.sleep(3)
        deliver_btn = self.scroll_to(self.DELIVER_BTN)
        assert deliver_btn.is_displayed()
        self.click(self.DELIVER_BTN)
        return DeliveryDetailsPage(self.driver)
