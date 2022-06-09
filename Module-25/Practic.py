import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()

@pytest.fixture(autouse=True)
def testing():
    driver.get('https://petfriends.skillfactory.ru/login')
    yield
    driver.quit()

def test_show_all_pets():
    driver.find_element_by_id('email').send_keys('mikkimouse11128@gmail.com')
    driver.find_element_by_id('pass').send_keys('LousySkill17175497')
    driver.find_element_by_css_selector('button[type="submit"]').click()
    assert driver.find_element_by_tag_name('h1').text == "PetFriends"

def test_attributes():
    driver.get('https://petfriends.skillfactory.ru/all_pets')
    images = WebDriverWait(driver, 10).until(
      ec.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-img-top')))
    names = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, '.card-deck .card-title')
    ))
    descriptions = WebDriverWait(driver, 10).until(
      ec.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-text')))
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

# Это для терминала и проверки теста: python -m pytest -v --driver Chrome --driver-path C:/Users/lousy/PycharmProjects/Module-25/chromedriver.exe Practic.py