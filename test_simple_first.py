import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def open_browser():
   browser.open('https://google.com')
   browser.driver.set_window_size(1024, 600)


def test_google(open_browser):
   browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
   browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_successful(open_browser):
    browser.element('[name="q"]').should(be.blank).type('54654121254152424').press_enter()
    browser.element('[id="result-stats"]').hould(have.text('Результатов: примерно 0'))
    print('Поиск по запросу не выдал результатов')
