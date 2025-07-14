from selenium import webdriver

def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
