import pytest
from selene import browser, be, have


def test_google_search():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))


def test_google_search_no_result():
    browser.element('[name="q"]').should(be.blank).type('er_+^%ger#$v023adsa').press_enter()
    browser.element('html').should(have.text('Об этой странице'))
