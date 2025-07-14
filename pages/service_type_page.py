from selenium.webdriver.common.by import By
from .base_page import BasePage
from .plan_selection_page import PlanSelectionPage
import allure

class ServiceTypePage(BasePage):
    
    SERVICE_TYPE_PAGE_HEADING = (By.XPATH, "//h1[text()='What brings you here?']")
    MOBILE_PLAN_BTN = (By.XPATH, "//p[text()='Mobile Plan']")
    HOME_INTERNET_BTN = (By.XPATH, "//p[text()='Home Internet']")

    @allure.step("Select mobile plan in the sign up flow")
    def click_mobile_plan_btn(self):
        self.click(self.MOBILE_PLAN_BTN)
        return PlanSelectionPage(self.driver)

    @allure.step("Verify that the service type page has loaded correctly")
    def verify_service_type_page_load(self):
        element = self.get_text(self.SERVICE_TYPE_PAGE_HEADING)
        assert element == 'What Brings You Here?'
