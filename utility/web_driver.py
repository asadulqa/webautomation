from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import shutil

class WebDriverFactory:
    @staticmethod
    def get_driver():
        # ✅ Point to Chromium 114 manually
        chrome_path = shutil.which("chromium-browser")
        if not chrome_path:
            raise RuntimeError("Chromium not found. Make sure it's installed.")

        options = Options()
        options.binary_location = chrome_path
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # ✅ Use matching ChromeDriver for Chromium 114
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(version="114.0.5735.90").install()),
            options=options
        )
        driver.set_window_size(1920, 1080)
        return driver
