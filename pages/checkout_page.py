from selenium.webdriver.common.by import By
from .base_page import BasePage
from .payment_page import PaymentPage
import time
import allure

class CheckoutPage(BasePage):

    CHECKOUT_HEADER = (By.XPATH, "//span[contains(text(), \"Please review the info below\")]")
    MBB_CHECKOUT_HEADER = (By.XPATH, '//span[normalize-space(.)="Review your order"]')
    NUMBER_CARD = (By.XPATH, '//h3[text()="Your new number"]')
    PLAN_CARD = (By.XPATH, '//h3[normalize-space(.)="Your plan"]')
    PAYMENT_PLAN_CARD = (By.XPATH, '//h3[text()="Your payment plan"]')
    DELIVERY_ADDRESS_CARD = (By.XPATH, '//h3[normalize-space(.)="Your delivery address"]')
    AGREE_INPUT = (By.XPATH, "//label[@for='agree']")
    CHOOSE_PAYMENT_BTN = (By.XPATH, '//button[text()="Choose Payment"]')
    MBB_CHOOSE_PAYMENT = (By.XPATH, '//button[normalize-space(.)="CHOOSE PAYMENT"]')
    LOCATION_CARD = (By.XPATH, '//h3[normalize-space(.)="Your chosen location"]')
    LOCATION_INPUT = (By.XPATH, "//label[@for='router_locked']")
    FINAL_AMOUNT = (By.XPATH, '//div[@class="vmo-summary-amount" and normalize-space(.)="AED 262.50"]')

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
        time.sleep(1)
        try:
            self.click(self.CHOOSE_PAYMENT_BTN)
        except:
            self.click(self.MBB_CHOOSE_PAYMENT)
        return PaymentPage(self.driver)

    @allure.step("Verify MBB header, location card, plan card, address card, and final amount")
    def verify_mbb_checkout_page(self):
        header = self.find(self.MBB_CHECKOUT_HEADER)
        location = self.find(self.LOCATION_CARD)
        plan = self.find(self.PLAN_CARD)
        input = self.find(self.LOCATION_INPUT)
        self.click(self.LOCATION_INPUT)
        address = self.scroll_to(self.DELIVERY_ADDRESS_CARD)
        price_text = self.get_text(self.FINAL_AMOUNT)
        assert price_text == "AED 262.50"
        assert header.is_displayed() and location.is_displayed() and plan.is_displayed() and input.is_displayed() and address.is_displayed()
       