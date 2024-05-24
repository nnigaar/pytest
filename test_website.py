import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service = Service("chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_cookies_element(driver):
    wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds
    eleCookiesDiv = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cookies')))
    background_color = eleCookiesDiv.value_of_css_property("background-color")
    height = float(eleCookiesDiv.size['height'])
    assert background_color == "rgba(255, 0, 0, 1)"
    assert height == 155.2

def test_logo_element(driver):
    wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds
    eleCookiesDiv2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.logo__icon')))
    width = eleCookiesDiv2.value_of_css_property("width")
    height = float(eleCookiesDiv2.size['height'])
    assert width == '300px'
    assert height == 175

def test_login_form_element(driver):
    wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds
    eleCookiesDiv3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.login-form__container')))
    background_color = eleCookiesDiv3.value_of_css_property("background-color")
    assert background_color == "rgba(0, 0, 0, 0)"

def test_input_element(driver):
    wait = WebDriverWait(driver, 20)  # Increased timeout to 20 seconds
    eleCookiesDiv4 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.input.input--blue.input--gray')))
    width = eleCookiesDiv4.value_of_css_property("width")
    height = eleCookiesDiv4.value_of_css_property("height")
    assert width == '372px'
    assert height == '40px'

