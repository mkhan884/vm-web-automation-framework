from pages.home_page import HomePage
import allure

@allure.title("Sign Up Flow - 1 Month")
@allure.description("This test verifies the web sign up flow for a 1 month product")
def test_sign_up_flow(driver):
    driver.get("https://www.virginmobile.ae")
    home_page = HomePage(driver)
    home_page.verify_page_load()
    service_type_page = home_page.click_join_us()
    service_type_page.verify_service_type_page_load()
    plan_selection_page = service_type_page.click_mobile_plan_btn()
    plan_selection_page.verify_plan_selection_page_load()
    plan_selection_page.change_plan()
    promo_page = plan_selection_page.click_continue_btn()
    promo_page.verify_promo_page()
    number_selection_page = promo_page.click_monthly_btn()
    number_selection_page.verify_number_selection_page()
    account_creation_page = number_selection_page.click_confirm()
    account_creation_page.verify_account_creation_page()
    id_type_page = account_creation_page.create_account("mobile")
    id_type_page.verify_id_page()
    address_page = id_type_page.select_id()
    address_page.verify_address_page()
    delivery_details_page = address_page.enter_address()
    delivery_details_page.verify_delivery_details_page()
    checkout_page = delivery_details_page.enter_address()
    checkout_page.verify_checkout_page()
    payment_page = checkout_page.agree_and_proceed()
    payment_page.verify_payment_page()






