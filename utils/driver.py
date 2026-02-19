from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os

def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # always start maximized when running locally
        options.add_argument("--start-maximized")

        # if we're running in a CI environment (GitHub Actions sets CI=true)
        # switch to headless mode and add the typical flags required for
        # containerized Linux runners.
        if os.environ.get("CI"):
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")

        # webdriver-manager automatically downloads and sets up the correct chromedriver
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.service import Service as FFService
        service = FFService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise ValueError("Unsupported browser")
