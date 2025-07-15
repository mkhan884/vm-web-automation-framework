from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class PaymentPage(BasePage):

    PAYMENT_HEADER = (By.XPATH, '//div[@class="vmo-step-name" and text()="Payment method"]')
    MBB_PAYMENT_HEADER = (By.XPATH, '//span[normalize-space(.)="Payment method"]')
    CREDIT = (By.XPATH, '//*[text()="Credit/debit card"]')
    GOOGLE_PAY = (By.XPATH, '//*[text()="Google Pay"]')
    POD = (By.XPATH, '//*[text()="Pay on delivery"]')
    PAYMENT_BTN = (By.ID, 'payment-continue')
    MBB_PAYMENT_BTN = (By.XPATH, '//button[normalize-space(.)="Continue"]')

    @allure.step("Verify payment page header, credit/debit, google pay and POD")
    def verify_payment_page(self):
        header = self.scroll_to_top_of_element(self.PAYMENT_HEADER)
        credit = self.find(self.CREDIT)
        google = self.find(self.GOOGLE_PAY)
        pod = self.find(self.POD)
        btn = self.scroll_to(self.PAYMENT_BTN)

        assert header.is_displayed() and credit.is_displayed() and google.is_displayed() and pod.is_displayed() and btn.is_displayed()

    @allure.step("Verify payment page header, credit/debit, google pay and POD")
    def verify_mbb_payment_page(self):
        header = self.scroll_to_top_of_element(self.MBB_PAYMENT_HEADER)
        credit = self.find(self.CREDIT)
        google = self.find(self.GOOGLE_PAY)
        pod = self.find(self.POD)
        btn = self.scroll_to(self.MBB_PAYMENT_BTN)
        
        assert header.is_displayed() and credit.is_displayed() and google.is_displayed() and pod.is_displayed() and btn.is_displayed()



    