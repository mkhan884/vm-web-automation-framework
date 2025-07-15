from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .mbb_promo_page import MbbPromoPage
import allure
import time

class CoverageCheckPage(BasePage):

    PAGE_HEADER = (By.XPATH, "//*[text()='Check your coverage']")
    SEARCH_BAR = (By.ID, "map_search_box")
    MAP = (By.ID, "CoverageMap")
    CHECK_COVERAGE_BTN = (By.ID, 'vmo-check-coverage-btn')
    CONTINUE_BTN = (By.XPATH, "//button[contains(@class, 'vmo-button') and contains(@class, 'popup_cta_btn') and text()='Continue']")
    ID_POPUP = (By.XPATH, "//div[@class='check_residency_popup_wrapper']")
    POPUP_HEADER = (By.XPATH, "//h2[normalize-space(text())='Have a valid Emirates ID?']")
    VALID_ID_BTN = (By.XPATH, '//button[text()="Yes, I have a valid Emirates ID"]')

    @allure.step("Verify page header, search bar and map")
    def verify_coverage_check_page(self):
        header = self.find(self.PAGE_HEADER)
        search = self.find(self.SEARCH_BAR)
        map = self.find(self.MAP)

        assert header.is_displayed() and search.is_displayed() and map.is_displayed()

    @allure.step("Enter address, confirm coverage and continue")
    def enter_address(self):
        search = self.find(self.SEARCH_BAR)
        search.send_keys("Dubai Design District")
        search.send_keys(Keys.ENTER)
        btn = self.find(self.CHECK_COVERAGE_BTN)
        time.sleep(2)
        btn.click()
        self.find(self.CONTINUE_BTN).click()
    
    @allure.step("Verify ID Popup and Confirm")
    def id_popup_check(self):
        self.find(self.ID_POPUP)
        self.find(self.POPUP_HEADER)
        self.click(self.VALID_ID_BTN)
        return MbbPromoPage(self.driver)



