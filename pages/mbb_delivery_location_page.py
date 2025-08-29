from selenium.webdriver.common.by import By
from .base_page import BasePage
from .delivery_details_page import DeliveryDetailsPage
import allure

class MbbDeliveryLocationPage(BasePage):
    PAGE_HEADER = (By.XPATH, '//span[normalize-space(.)="Where do you want your order delivered?"]')
    CURR_LOCATION = (By.XPATH, '//div[@class="vmo-delivery-box-title" and normalize-space(.)="Chosen location"]')

    @allure.step("Verify the page that asks whether the delivery should be at the same or different location")
    def verify_delivery_location_page(self):
        assert self.find(self.PAGE_HEADER).is_displayed()
    
    @allure.step("Select current location for delivery")
    def select_current_location(self):
        self.find(self.CURR_LOCATION).click()
        return DeliveryDetailsPage(self.driver)
