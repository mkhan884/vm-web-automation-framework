from selenium.webdriver.common.by import By
from .base_page import BasePage
from .service_type_page import ServiceTypePage
import allure

class HomePage(BasePage):
    
    JOIN_US_BTN = (By.ID, "vmo-get-started-join")
    HEADING_TEXT = (By.XPATH, "//h1[text()='Join Virgin Mobile']")

    @allure.step("Click join us on the homepage")
    def click_join_us(self):
        self.click(self.JOIN_US_BTN)
        return ServiceTypePage(self.driver)

    @allure.step("Verify that the homepage loaded correctly")
    def verify_page_load(self):
        element = self.get_text(self.HEADING_TEXT)
        assert element == "Join Virgin Mobile"