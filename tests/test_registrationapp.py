
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_registration_page(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:8090/")

    assert driver.find_element(By.TAG_NAME, "h2").text == \
        "Student Registration Form"


def test_registration_form(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:8090/")

    driver.find_element(By.NAME, "name").send_keys("Sumayya")
    driver.find_element(By.NAME, "email").send_keys("sumayya@example.com")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")

    Select(driver.find_element(By.NAME, "course")).select_by_visible_text("B.Tech")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    assert "Registration successful! Welcome, Sumayya." in \
        driver.find_element(By.TAG_NAME, "h3").text
