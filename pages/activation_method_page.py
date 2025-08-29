from selenium.webdriver.common.by import By
from .base_page import BasePage
from .checkout_page import CheckoutPage
import allure

class ActivationMethodPage(BasePage):

    PAGE_HEADER = (By.XPATH, "//span[text()='Choose activation method']")
    INSTANT_ACTIVATION_CARD = (By.XPATH, "//div[contains(@class, 'activation-method-option') and contains(@class, 'instant-activation')]")
    STORE_ACTIVATION_CARD = (By.XPATH, "//div[contains(@class, 'activation-method-option') and contains(@class, 'instore-activation')]")
    STORE_ACTIVATION_BTN = (By.XPATH, "//button[text()='Physical Activation']")
    
    @allure.step("Verify the activation method page header, instant activation / store activation cards.")
    def verify_activation_method_page(self):
        header = self.find(self.PAGE_HEADER)
        instant = self.find(self.INSTANT_ACTIVATION_CARD)
        store = self.scroll_to(self.STORE_ACTIVATION_CARD)
        assert header.is_displayed() and instant.is_displayed() and store.is_displayed()

    @allure.step("Select in store activation button and navigate to payment page")
    def select_store_activation(self):
        self.scroll_to(self.STORE_ACTIVATION_BTN).click()
        return CheckoutPage(self.driver)

