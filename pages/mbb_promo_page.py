from selenium.webdriver.common.by import By
from .base_page import BasePage
from .account_creation_page import AccountCreationPage
import allure

class MbbPromoPage(BasePage):

    PAGE_HEADER = (By.XPATH, '//h2[@class="vmo-page-title" and normalize-space(text())="12-months offer"]')
    CARD_TITLE = (By.XPATH, '//h3[normalize-space(.)="Home Internet for 12 months"]')
    ROUTER_IMG = (By.XPATH, '//img[@alt="Huawei 5G Router"]')
    CREATE_PLAN_HEADER = (By.XPATH, '//span[normalize-space(text())="Create your own plan"]')
    DATA_CARD = (By.XPATH, '//div[contains(@class, "vmo-broadband-plan-data") and contains(@class, "vmo-broadband-plan-card")]')
    ROUTER_CARD = (By.XPATH, '//div[contains(@class, "vmo-broadband-plan-modem") and contains(@class, "vmo-broadband-plan-card")]')
    NO_ROUTER_TAB = (By.XPATH, '//div[contains(@class, "tab-item") and normalize-space(.)="No router"]')
    PLAN_PRICE = (By.XPATH, '//span[@class="price" and normalize-space(.)="250"]')
    CONTINUE_BTN = (By.XPATH, '//button[normalize-space(.)="Continue"]')
    COMPATIBILITY_CARD = (By.XPATH, '//p[@class="router-disclaimer-box-title bold" and normalize-space(.)="Avoid compatibility issues"]')
    CONTIUNE_WITHOUT_ROUTER = (By.XPATH, '//button[normalize-space(.)="Continue without Router"]')

    @allure.step("Verify that the header, title and router image have loaded")
    def verify_page_load(self):
        header = self.find(self.PAGE_HEADER)
        title = self.find(self.CARD_TITLE)
        img = self.find(self.ROUTER_IMG)
        assert header.is_displayed() and title.is_displayed() and img.is_displayed()
    
    @allure.step("Verify header, data card and router card. Select no router and proceed")
    def choose_plan(self):
        header = self.scroll_to(self.CREATE_PLAN_HEADER)
        data_card = self.find(self.DATA_CARD)
        router_card = self.find(self.ROUTER_CARD)
        assert header.is_displayed() and data_card.is_displayed() and router_card.is_displayed()
        self.scroll_to(self.NO_ROUTER_TAB).click()
        self.scroll_to(self.PLAN_PRICE)
        price_text = self.get_text(self.PLAN_PRICE)
        assert price_text == '250'
        self.scroll_to(self.CONTINUE_BTN).click()

    @allure.step("Verify compatability screen is shown, and continue with no router")
    def bypass_compatibility_screen(self):
        assert self.find(self.COMPATIBILITY_CARD).is_displayed()
        self.scroll_to(self.CONTIUNE_WITHOUT_ROUTER).click()
        return AccountCreationPage(self.driver)

    


    