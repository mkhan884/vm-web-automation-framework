from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os


def get_driver(browser="chrome"):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # always start maximized when running locally
        options.add_argument("--start-maximized")

        # Add stealth flags to reduce bot detection
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        )

        # Optional proxy support via PROXY env var (format: host:port)
        proxy = os.environ.get("PROXY")
        if proxy:
            options.add_argument(f"--proxy-server={proxy}")

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
        # Allow opting into undetected-chromedriver via env var USE_UNDETECTED=true
        use_undetected = os.environ.get("USE_UNDETECTED")
        driver = None
        if use_undetected:
            try:
                import undetected_chromedriver as uc

                # uc.Chrome accepts ChromeOptions
                driver = uc.Chrome(options=options)
            except Exception:
                driver = None

        if not driver:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        # Use CDP to inject a small script that hides common automation indicators
        try:
            driver.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {
                    "source": """
                        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                        window.chrome = { runtime: {} };
                        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                        Object.defineProperty(navigator, 'permissions', {
                            get: () => ({
                                query: (params) =>
                                    params.name === 'notifications' ? Promise.resolve({ state: Notification.permission }) : window.navigator.permissions.query(params)
                            })
                        });
                    """,
                },
            )
        except Exception:
            # If CDP injection fails (older drivers/runtimes), continue without it
            pass

        return driver
    elif browser == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.service import Service as FFService

        service = FFService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    else:
        raise ValueError("Unsupported browser")
