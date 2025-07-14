from selenium.webdriver.common.by import By
from .base_page import BasePage
import allure

class PaymentPage(BasePage):

    PAYMENT_HEADER = (By.XPATH, '//div[@class="vmo-step-name" and text()="Payment method"]')
    CREDIT = (By.XPATH, '//div[@class="payment-method-name" and text()="Credit/debit card"]')
    GOOGLE_PAY = (By.XPATH, '//div[@class="payment-method-name" and text()="Google Pay"]')
    POD = (By.XPATH, '//div[@class="payment-method-name" and text()="Pay on delivery"]')
    PAYMENT_BTN = (By.ID, 'payment-continue')

    @allure.step("Verify payment page header, credit/debit, google pay and POD")
    def verify_payment_page(self):
        header = self.find(self.PAYMENT_HEADER)
        credit = self.find(self.CREDIT)
        google = self.find(self.GOOGLE_PAY)
        pod = self.find(self.POD)
        btn = self.scroll_to(self.PAYMENT_BTN)

        assert header.is_displayed() and credit.is_displayed() and google.is_displayed() and pod.is_displayed() and btn.is_displayed()

    

    

    