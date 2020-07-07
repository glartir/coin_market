import pytest
from ..pages.base_page import BasePage
from ..pages.main_page  import MainPage

def test_should_be_language_change(browser):
    link="https://coinmarketcap.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_change_language()



    # shold_be_change_title()
    # should_be_change_url()
    # should_be_changed_price()

