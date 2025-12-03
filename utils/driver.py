from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
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
