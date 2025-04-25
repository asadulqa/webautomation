
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import shutil

class WebDriverFactory:
    @staticmethod
    def get_driver():
        chrome_path = shutil.which("chromium-browser")  # 👈 Get the real path in Actions
        if chrome_path is None:
            raise RuntimeError("Chromium is not installed or not found")

        options = Options()
        options.binary_location = chrome_path
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager(version="114.0.5735.90").install()),
            options=options
        )
        driver.set_window_size(1920, 1080)
        return driver
