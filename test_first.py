from selene import browser, be, have


def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))
    browser.driver.save_screenshot('screenshot.png')

    # browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
