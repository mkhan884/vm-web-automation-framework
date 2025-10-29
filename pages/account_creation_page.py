from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .mbb_delivery_location_page import MbbDeliveryLocationPage
from .activation_method_page import ActivationMethodPage
from .location_request_page import LocationRequestPage
from utils.random_email import RandomEmail
import allure

class AccountCreationPage(BasePage):
    
    ACCOUNT_CREATION_HEADER = (By.XPATH, "//*[normalize-space(.)='Nice to meet you!']")
    MBB_ACCOUNT_CREATION_HEADER = (By.XPATH, "//div[normalize-space(.)='Hello stranger']")
    TOURIST_ACCOUNT_CREATION_HEADER = (By.XPATH, "//div[normalize-space(.)='Hello!']")
    CONTINUE_WITH_EMAIL = (By.XPATH, "//button[text()='Continue with email']")
    CREATE_BTN = (By.ID, 'btn_create_account')
    EMAIL_TEXT_BOX = (By.ID, 'userEmail')
    PASSWORD_TEXT_BOX = (By.ID, 'userPassword')
    POPUP_HEADER = (By.XPATH, "//h2[contains(text(), 'Is this your email')]")
    POPUP_BTN = (By.ID, "btn_confirm_email_yes")


    @allure.step("Verify that the account creation page has loaded and header / btn is displayed.")
    def verify_account_creation_page(self):
        header = self.find(self.ACCOUNT_CREATION_HEADER)
        continue_with_email_btn = self.find(self.CONTINUE_WITH_EMAIL)
        assert header.is_displayed() and continue_with_email_btn.is_displayed()
        self.click(self.CONTINUE_WITH_EMAIL) # Navigate to email page

    @allure.step("Verify that the mbb account creation page has loaded.")
    def verify_mbb_account_creation_page(self):
        header = self.find(self.MBB_ACCOUNT_CREATION_HEADER)
        assert header.is_displayed()

    @allure.step("verify that the toursit account creation page has loaded.")
    def verify_tourist_account_creation_page(self):
        header = self.find(self.TOURIST_ACCOUNT_CREATION_HEADER)
        assert header.is_displayed()

    @allure.step("Create an account using a randomly generated email")
    def create_account(self, account_type):
        email = RandomEmail.generate_random_email()
        self.find(self.EMAIL_TEXT_BOX).send_keys(email)
        self.find(self.PASSWORD_TEXT_BOX).send_keys("Abcabc123")
        self.click(self.CREATE_BTN)
        element = self.find(self.POPUP_HEADER)
        assert element.is_displayed()
        popup_btn = self.find(self.POPUP_BTN)
        assert popup_btn.is_displayed()
        self.click(self.POPUP_BTN)
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "vmo-modal-inner")))
        if(account_type == 'mbb'):
            return MbbDeliveryLocationPage(self.driver)
        elif(account_type == 'mobile'):
            return ActivationMethodPage(self.driver)
        elif(account_type == 'tourist'):
            return LocationRequestPage(self.driver)
    