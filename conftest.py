from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@fixture(scope="function")
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()
