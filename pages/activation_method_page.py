from selenium.webdriver.common.by import By
from .base_page import BasePage
from .address_page import AddressPage
from .checkout_page import CheckoutPage
import allure

class ActivationMethodPage(BasePage):

    PAGE_HEADER = (By.XPATH, "//span[normalize-space(.)='Choose activation method']")
    STORE_ACTIVATION_CARD = (By.XPATH, "//div[contains(@class, 'activation-method-option') and contains(@class, 'instore-activation')]")
    STORE_ACTIVATION_BTN = (By.XPATH, "//button[text()='Physical Activation']")
    DRIVER_BTN = (By.XPATH, "//button[normalize-space(.)='Activation via driver']")

    @allure.step("Verify the activation method page header, instant activation / store activation cards.")
    def verify_activation_method_page(self):
        header = self.find(self.PAGE_HEADER)
        store = self.scroll_to(self.STORE_ACTIVATION_CARD)
        driver = self.scroll_to(self.DRIVER_BTN)
        assert header.is_displayed() and store.is_displayed() and driver.is_displayed()

    @allure.step("Select in store activation button and navigate to payment page")
    def select_driver_activation(self):
        self.scroll_to(self.DRIVER_BTN).click()
        return AddressPage(self.driver)
    
    def select_store_activation(self):
        self.scroll_to(self.STORE_ACTIVATION_BTN)
        self.click(self.STORE_ACTIVATION_BTN)
        return CheckoutPage(self.driver)

