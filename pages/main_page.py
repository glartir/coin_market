from .base_page import BasePage
from .locators import MainPageLocators
from langdetect.detector_factory import detect
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_change_language(self,lang_interface="de"):
        self.wait_and_click_button(*MainPageLocators.SWAP_BUTTON)
        #self.wait_and_click_button(*MainPageLocators.LANGUAGE_BUTTON_DE) самый старый рабочий варик.
        self.wait_and_click_button(*MainPageLocators.LANGUAGE_BUTTONS_DICT[lang_interface])

    def should_be_lang_url(self,lang_interface="de"):
        if lang_interface!="en":
            assert f"/{lang_interface}/" in self.browser.current_url , "The page was not opened." # толкнуть параметризацию
        else:
            assert self.browser.current_url=="https://coinmarketcap.com/"

    def should_be_good_language(self,lang_interface="de"):

        title = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(MainPageLocators.TITLE_TEXT)).text
        #title=self.browser.find_element(*MainPageLocators.TITLE_TEXT).text
        # print(detect(title))
        # print(lang_interface)
        detect_lang=detect(title)
        assert detect_lang == lang_interface , f"The title was not changed, detected {detect_lang}, used {lang_interface}"
        # print (title)



    def Full(self,lang_interface="de"):
        self.go_to_change_language(lang_interface)
        self.should_be_good_language(lang_interface)
        self.should_be_lang_url(lang_interface)







