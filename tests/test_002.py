from pages.home_page import HomePage
import allure

@allure.title("Sign Up Flow - MBB 1 Month")
@allure.description("This test verifies the web sign up flow for MBB 1 month plan")
def test_mbb_sign_up_flow(driver):
    driver.get("https://www.virginmobile.ae")
    home_page = HomePage(driver)
    home_page.verify_page_load()
    service_type_page = home_page.click_join_us()
    service_type_page.verify_service_type_page_load()
    coverage_check_page = service_type_page.click_mbb_plan_btn()
    coverage_check_page.verify_coverage_check_page()
    mbb_residency_check_page = coverage_check_page.enter_address()
    mbb_promo_page = mbb_residency_check_page.verify_mbb_residency_check_page()
    mbb_promo_page.verify_page_load()
    mbb_promo_page.choose_plan()
    account_creation_page = mbb_promo_page.bypass_compatibility_screen()
    account_creation_page.verify_mbb_account_creation_page()
    mbb_delivery_location_page = account_creation_page.create_account("mbb")
    mbb_delivery_location_page.verify_delivery_location_page()
    delivery_details_page = mbb_delivery_location_page.select_current_location()
    delivery_details_page.verify_delivery_details_page()
    checkout_page = delivery_details_page.enter_address()
    checkout_page.verify_mbb_checkout_page()
    payment_page = checkout_page.agree_and_proceed()
    payment_page.verify_mbb_payment_page()
    