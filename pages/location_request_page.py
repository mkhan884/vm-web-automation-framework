from selenium.webdriver.common.by import By
from .base_page import BasePage
from .activation_method_page import ActivationMethodPage
import allure

class LocationRequestPage(BasePage):

    HEADER = (By.XPATH, "//span[normalize-space(.)='We need your location']")
    SHARE_LOCATION_BTN = (By.XPATH, "//button[normalize-space(.)='Share location']")

    @allure.step("Verify location page header")
    def verify_location_request_page(self):
        header = self.find(self.HEADER)
        assert header.is_displayed()
        
    @allure.step("Select share location and navigate to activation method page")
    def click_share_location_btn(self):
        self.scroll_to(self.SHARE_LOCATION_BTN)
        self.click(self.SHARE_LOCATION_BTN)
        return ActivationMethodPage(self.driver)
    
 

