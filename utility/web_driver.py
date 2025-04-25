from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverFactory:
    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--headless")  # Optional
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # 🔥 Pin to a known working version (until 135 is available)
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(version="114.0.5735.90").install()),
            options=options
        )

        return driver
