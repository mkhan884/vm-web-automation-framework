from pages.home_page import HomePage
import allure

@allure.title("Sign Up Flow - Tourist Plan")
@allure.description("This test verifies the web toursit sign up flow.")
def test_tourist_plan_flow(driver):
    driver.get("https://www.virginmobile.ae")
    home_page = HomePage(driver)
    service_type_page = home_page.click_join_us()
    service_type_page.verify_service_type_page_load()
    tourist_plan_page = service_type_page.click_tourist_plan_btn()
    tourist_plan_page.verify_tourist_plan_page_load()
    account_creation_page = tourist_plan_page.click_tourist_plan_btn()
    account_creation_page.verify_tourist_account_creation_page()
    location_request_page = account_creation_page.create_account("tourist")
    location_request_page.verify_location_request_page()
    activation_method_page = location_request_page.click_share_location_btn()
    checkout_page = activation_method_page.select_store_activation()
    checkout_page.verify_tourist_checkout_page()