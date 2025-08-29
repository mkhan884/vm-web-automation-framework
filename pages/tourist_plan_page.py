from selenium.webdriver.common.by import By
from .base_page import BasePage
from .account_creation_page import AccountCreationPage
import allure

class TouristPlanPage(BasePage):

    TOURIST_PAGE_HEADING = (By.XPATH, "//h1[text()='Pick a plan that suits you']")
    PLAN_CARD_ITEM = (By.XPATH, "//div[contains(@class, 'tourist_plan_card_item') and @index='0']")
    CONTINE_BTN = (By.XPATH, "//div[text()='Choose this plan']")

    @allure.step("Verify that the tourist plan page has loaded correctly")
    def verify_tourist_plan_page_load(self):
        element = self.get_text(self.TOURIST_PAGE_HEADING)
        assert element == 'Pick a plan that suits you'
    
    @allure.step("Click on the tourist plan button")
    def click_tourist_plan_btn(self):
        self.scroll_to(self.PLAN_CARD_ITEM)
        self.click(self.PLAN_CARD_ITEM)
        self.scroll_to(self.CONTINE_BTN)
        self.click(self.CONTINE_BTN)
        return AccountCreationPage(self.driver)