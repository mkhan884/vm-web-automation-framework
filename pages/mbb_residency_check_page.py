from selenium.webdriver.common.by import By
from .base_page import BasePage
from .mbb_promo_page import MbbPromoPage
import allure

class MbbResidencyCheckPage(BasePage):

    EMIRATES_ID = (By.XPATH, "//h3[normalize-space(.)='I have an Emirates ID']")
    
    @allure.step("Verify emirates id card")
    def verify_mbb_residency_check_page(self):
        self.find(self.EMIRATES_ID)
        self.click(self.EMIRATES_ID)

        return MbbPromoPage(self.driver)

