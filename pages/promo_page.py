from selenium.webdriver.common.by import By
from .base_page import BasePage
from .number_selection_page import NumberSelectionPage
import allure

class PromoPage(BasePage):
    
    PROMO_HEADING = (By.XPATH, "//span[contains(text(),'Want a discount')]")
    MONTHLY_BTN = (By.XPATH, "//button[normalize-space()='Stay on monthly']")
    YEARLY_BTN = (By.XPATH, "//button[normalize-space()='GO 12-MONTH']")

    @allure.step("Verify that the promo page is loaded")
    def verify_promo_page(self):
        element = self.find(self.PROMO_HEADING)
        assert element.is_displayed()
        btn = self.scroll_to(self.YEARLY_BTN)
        assert btn.is_displayed()

    @allure.step("Click monthly plan on the promo screen")
    def click_monthly_btn(self):
        self.click(self.MONTHLY_BTN)
        return NumberSelectionPage(self.driver)
        