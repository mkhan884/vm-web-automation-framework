from selenium.webdriver.common.by import By
from .base_page import BasePage
from .address_page import AddressPage
from .checkout_page import CheckoutPage
import allure

class ActivationMethodPage(BasePage):

    PAGE_HEADER = (By.XPATH, "//span[normalize-space(.)='Choose activation method']")
    DRIVER_CARD = (By.XPATH, "//p[@class='activation-method-title' and normalize-space(.)='Activation via Driver']")
    DELIVERY_ACTIVATION_BTN = (By.XPATH, "//button[text()='delivery activation']")
    STORE_ACTIVATION_LINK = (By.XPATH,"//button[contains(@class,'instore-activation-method-cta') and normalize-space(.)='Activation in store']")


    @allure.step("Verify the activation method page header, instant activation / store activation cards.")
    def verify_activation_method_page(self):
        header = self.find(self.PAGE_HEADER)
        driver = self.find(self.DRIVER_CARD)
        store = self.find(self.STORE_ACTIVATION_LINK)

        assert header.is_displayed() and store.is_displayed() and driver.is_displayed()

    @allure.step("Select activation via driver button and navigate to address page.")
    def select_driver_activation(self):
        self.scroll_to(self.DELIVERY_ACTIVATION_BTN).click()
        return AddressPage(self.driver)
    
    @allure.step("Select activation in store link and navigate to checkout page.")
    def select_store_activation(self):
        self.click(self.STORE_ACTIVATION_LINK)
        return CheckoutPage(self.driver)

