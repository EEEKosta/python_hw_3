import pytest
from selene import browser, be, have



@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_height = 1280
    browser.config.window_width = 720
    browser.open("https://www.google.com/")
    yield browser
    browser.quit()

