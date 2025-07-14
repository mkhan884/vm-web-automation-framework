import pytest
from utils.driver import get_driver
import allure

# Hook to capture test status
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get the report object
    outcome = yield
    rep = outcome.get_result()
    
    # Attach report to test node for later access
    setattr(item, f"rep_{rep.when}", rep)

# Main driver fixture with screenshot logic
@pytest.fixture
def driver(request):
    # Initialize WebDriver
    driver = get_driver()
    yield driver
    
    # Check if test failed during execution phase
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            # Capture screenshot as PNG binary
            screenshot = driver.get_screenshot_as_png()
            # Attach to Allure report
            allure.attach(
                screenshot,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print(f"Failed to capture screenshot: {str(e)}")
    
    # Teardown: Quit driver
    driver.quit()