from selenium.webdriver.common.by import By
from .base_page import BasePage
from .checkout_page import CheckoutPage
import allure

class DeliveryDetailsPage(BasePage):
    PAGE_HEADER = (By.XPATH, "//span[contains(text(), \"We'll deliver your SIM\")]")
    OFFICE = (By.XPATH, "//div[@class='vmo-location-type-title' and text()='Office']")
    BUILDING_NAME = (By.ID, 'building')
    FLOOR = (By.ID, "floor")
    UNIT = (By.ID, "unit")
    NAME = (By.ID, "customer_name")
    NUMBER = (By.ID, "phone")
    INSTRUCTIONS = (By.ID, "instructions")
    CONTINUE_BTN = (By.ID, "btn_delivery_form_continue")

    @allure.step("Verify delivery details page header and building options")
    def verify_delivery_details_page(self):
        header = self.find(self.PAGE_HEADER)
        office = self.find(self.OFFICE)
        assert header.is_displayed() and office.is_displayed
    
    @allure.step("Enter the address details and click continue")
    def enter_address(self):
        self.find(self.OFFICE).click()
        self.type(self.BUILDING_NAME, "TEST")
        self.type(self.FLOOR, "TEST")
        self.type(self.UNIT, "UNIT")
        self.type(self.NAME, "TEST")
        self.type(self.NUMBER, "0585152784")
        self.type(self.INSTRUCTIONS, "TEST")
        self.scroll_to(self.CONTINUE_BTN)
        self.click(self.CONTINUE_BTN)
        return CheckoutPage(self.driver)
        

