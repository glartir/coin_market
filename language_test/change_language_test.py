import pytest
from ..pages.base_page import BasePage
from ..pages.main_page  import MainPage



@pytest.mark.parametrize('lang_interface', ["de","en","es","fil","fr","hi","it","ja","ko","pt-br","ru","tr","vi","zh","zh-tw"])
def test_should_be_language_change_big_size(browser,lang_interface):
    link="https://coinmarketcap.com/"
    page = MainPage(browser, link)
    page.change_window_size()
    page.open()
    page.Full(lang_interface)




#@pytest.mark.parametrize('lang_interface', ["de","en","es","fr","hi","it","ko","ja","ru","tr","vi"])
#@pytest.mark.parametrize('lang_interface', ["de","en","es","fil","fr","hi","it","ja","ko","pt-br","ru","tr","vi","zh","zh-tw"])