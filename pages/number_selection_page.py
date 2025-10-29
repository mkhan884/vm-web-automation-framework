from selenium.webdriver.common.by import By
from .base_page import BasePage
from .id_type_page import IdTypePage
import allure

class NumberSelectionPage(BasePage):
    
    PAGE_HEADING = (By.XPATH, "//span[text()='Find a number you love']")
    CONFIRM_BTN = (By.XPATH, "//div[normalize-space()='Yes, I like this number']")
    REJECT_BTN = (By.XPATH, "//div[normalize-space()='No, Choose a number']")
    TRANSFER_LINK = (By.XPATH, "//div[normalize-space()='Transfer my number to Virgin Mobile']")

    @allure.step("Verify number selection page heading, confirm/reject btn and MNP link")
    def verify_number_selection_page(self):
        page_heading = self.find(self.PAGE_HEADING)
        confirm_btn = self.find(self.CONFIRM_BTN)
        reject_btn = self.find(self.REJECT_BTN)
        transfer_link = self.find(self.TRANSFER_LINK)
        assert page_heading.is_displayed() and confirm_btn.is_displayed() and reject_btn.is_displayed() and transfer_link.is_displayed()
    
    @allure.step("Select confirm btn")
    def click_confirm(self):
        self.click(self.CONFIRM_BTN)
        return IdTypePage(self.driver)