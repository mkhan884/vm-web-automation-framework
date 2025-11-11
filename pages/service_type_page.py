from selenium.webdriver.common.by import By
from .base_page import BasePage
from .plan_selection_page import PlanSelectionPage
from .coverage_check_page import CoverageCheckPage
from .tourist_plan_page import TouristPlanPage
import allure

class ServiceTypePage(BasePage):
    
    SERVICE_TYPE_PAGE_HEADING = (By.XPATH, "//h1[text()='What brings you here?']")
    MOBILE_PLAN_BTN = (By.XPATH, "//a[p[normalize-space(.)='Mobile Plan']]")
    HOME_INTERNET_BTN = (By.XPATH, '//p[normalize-space(text())="Home Internet" and span[normalize-space(.)="Emirates ID holders only"]]')
    TOURIST_BTN = (By.XPATH, "//p[contains(text(), 'Tourist Plan') and span[text()='Passport only']]")

    @allure.step("Verify that the service type page has loaded correctly")
    def verify_service_type_page_load(self):
        element = self.get_text(self.SERVICE_TYPE_PAGE_HEADING)
        assert element == 'What Brings You Here?'

    @allure.step("Select mobile plan in the sign up flow")
    def click_mobile_plan_btn(self):
        self.click(self.MOBILE_PLAN_BTN)
        return PlanSelectionPage(self.driver)
    
    @allure.step("Select MBB plan in the sign up flow")
    def click_mbb_plan_btn(self):
        self.scroll_to(self.HOME_INTERNET_BTN)
        self.click(self.HOME_INTERNET_BTN)
        return CoverageCheckPage(self.driver)
    
    @allure.step("Select tourist plan in the sign up flow")
    def click_tourist_plan_btn(self):
        self.scroll_to(self.TOURIST_BTN).click()
        return TouristPlanPage(self.driver)


    
