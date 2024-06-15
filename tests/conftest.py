import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_password, valid_email

@pytest.fixture(autouse=True)
def auth_pets():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    driver.get('http://petfriends.skillfactory.ru/login') # заходим на страницу с авторизацией
    driver.maximize_window()

    email_log =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))) #вводим свою почту
    email_log.clear()
    email_log.send_keys(valid_email)

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'pass'))) #вводип пароль
    password.clear()
    password.send_keys(valid_password)

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))

    element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"Мои питомцы")]'))).click() #переходим на ссылку "Мои питомцы"
    time.sleep(2)
    yield driver

    driver.quit()