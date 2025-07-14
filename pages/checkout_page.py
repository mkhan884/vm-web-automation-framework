from selenium.webdriver.common.by import By
from .base_page import BasePage
from .payment_page import PaymentPage
import time
import allure

class CheckoutPage(BasePage):

    CHECKOUT_HEADER = (By.XPATH, "//span[contains(text(), \"Please review the info below\")]")
    NUMBER_CARD = (By.XPATH, '//h3[text()="Your new number"]')
    PLAN_CARD = (By.XPATH, '//h3[normalize-space(.)="Your plan"]')
    PAYMENT_PLAN_CARD = (By.XPATH, '//h3[text()="Your payment plan"]')
    DELIVERY_ADDRESS_CARD = (By.XPATH, '//h3[normalize-space(.)="Your delivery address"]')
    AGREE_INPUT = (By.XPATH, "//label[@for='agree']")
    CHOOSE_PAYMENT_BTN = (By.XPATH, '//button[text()="Choose Payment"]')

    @allure.step("Verify all payment elements are loaded and displayed on the screen")
    def verify_checkout_page(self):
        header = self.find(self.CHECKOUT_HEADER)
        number = self.find(self.NUMBER_CARD)
        plan = self.find(self.PLAN_CARD)
        delivery_address = self.find(self.DELIVERY_ADDRESS_CARD)
        payment_plan = self.scroll_to(self.PAYMENT_PLAN_CARD)

        assert header.is_displayed() and number.is_displayed() and plan.is_displayed() and payment_plan.is_displayed() and delivery_address.is_displayed()

    @allure.step("Agree to terms and proceed to payment")
    def agree_and_proceed(self):
        self.scroll_to(self.AGREE_INPUT).click()
        time.sleep(0.5)
        self.click(self.CHOOSE_PAYMENT_BTN)
        return PaymentPage(self.driver)
