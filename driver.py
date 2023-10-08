from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def chrome_options() -> webdriver.ChromeOptions:
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--headless")

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    return chrome_options


def chrome_browser(wait: int = 5) -> webdriver.Chrome:
    driver = webdriver.Chrome(
        service=Service('/var/task/chromedriver'),
        options=chrome_options()
    )
    driver.implicitly_wait(wait)
    
    return driver
