import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.quit()

def test_cookies_div_properties(driver):
    wait = WebDriverWait(driver, 10)
    eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))

    background_color = eleCookiesDiv.value_of_css_property("background-color")
    height = float(eleCookiesDiv.size['height'])
    width = eleCookiesDiv.value_of_css_property("width")

    assert background_color == "rgba(255, 0, 0, 1)", f"Expected rgba(255, 0, 0, 1), but got {background_color}"
    assert height == 175.0, f"Expected height 175.0, but got {height}"
    assert width == '300px', f"Expected width '300px', but got {width}"