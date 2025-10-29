from selenium.webdriver.common.by import By
from .base_page import BasePage
from .account_creation_page import AccountCreationPage
import allure

class IdTypePage(BasePage):
    
    PAGE_HEADER = (By.XPATH, "//*[text()='Choose your ID type']")
    ID_SELECTOR = (By.XPATH, '//div[contains(text(), "I have an Emirates ID")]')
    PP_SELECTOR = (By.XPATH, "//div[text()='I have a passport']")

    def wait_for_page_to_load(self):
        header = self.find(self.PAGE_HEADER)
        id = self.find(self.ID_SELECTOR)
        pp = self.find(self.PP_SELECTOR)
        return header, id, pp

    @allure.step("Verify ID type page")
    def verify_id_page(self):
        header, id, pp = self.wait_for_page_to_load()
        assert header.is_displayed() and id.is_displayed() and pp.is_displayed()

    @allure.step("Select EID as the ID option")
    def select_id(self):
        self.click(self.ID_SELECTOR)
        return AccountCreationPage(self.driver)