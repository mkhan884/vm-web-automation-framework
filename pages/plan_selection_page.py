from selenium.webdriver.common.by import By
from .base_page import BasePage
from .promo_page import PromoPage
import re
import allure
import time

class PlanSelectionPage(BasePage):
    
    PLAN_SELECTION_HEADING = (By.XPATH, "//h2[text()='Build your own plan']")
    DATA_UP_BTN = (By.ID, "btn_up_DATA")
    DATA_AMOUNT = (By.XPATH, "//span[@class='vmo-value' and text()='6']")
    DURATION_SELECTOR = (By.XPATH, "//div[@class='vmo-commitments-option-duration' and text()='1 month']")
    CURRENT_PRICE = (By.XPATH, "//div[@class='current-price-section']/p")
    CONTINUE_BTN = (By.XPATH, "//div[normalize-space()='CONTINUE']")

    @allure.step("Verify plan selection page.")
    def verify_plan_selection_page_load(self):
        heading = self.find(self.PLAN_SELECTION_HEADING)
        assert heading.is_displayed()
    
    @allure.step("Change the plan and verify that the correct amount is reflected in the plan price")
    def change_plan(self):
        self.click(self.DATA_UP_BTN)
        data_amount = self.get_text(self.DATA_AMOUNT)
        assert data_amount == '6'
        self.scroll_to(self.DURATION_SELECTOR)
        self.click(self.DURATION_SELECTOR)
        time.sleep(2)
        price = self.find(self.CURRENT_PRICE).text
        match = re.search(r'\d+', price).group()
        assert match == '119'

    @allure.step("Click continue btn on the plan selection page")
    def click_continue_btn(self):
        self.scroll_to(self.CONTINUE_BTN)
        self.click(self.CONTINUE_BTN)
        return PromoPage(self.driver)


        

