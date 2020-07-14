from .base_page import BasePage
from .locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
#from langdetect.detector_factory import detect
import cld2
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def go_to_change_language(self,lang_interface="fil"):
        self.wait_and_click_button(*MainPageLocators.SWAP_BUTTON)
        button =  WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(MainPageLocators.LANGUAGE_BUTTONS_DICT[lang_interface][0]))
        button.click() # Делаем не как с первой кнопкой для того чтобы иметь элемент по которому будем отсекать момент ухода со страницы
        WebDriverWait(self.browser, 5).until(EC.staleness_of(button))

    def should_be_lang_url(self,lang_interface="fil"):
        if lang_interface!="en":
            assert f"/{lang_interface}/" in self.browser.current_url , "The page was not opened." # толкнуть параметризацию
        else:
            assert self.browser.current_url=="https://coinmarketcap.com/"

    def should_be_good_language(self,lang_interface="fil"):

        title = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(MainPageLocators.TITLE_TEXT)).text
        # print(title)
        #detect_lang = detect(title)
        #assert detect_lang == lang_interface , f"The title was not changed, detected {detect_lang}, used {lang_interface}"


    def experiment_write_title(self,lang_interface="fil"):
        lang_interface = MainPageLocators.LANGUAGE_BUTTONS_DICT[lang_interface][1]
        title = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(MainPageLocators.TITLE_TEXT)).text
        # print(title)
        text_on_page = ""
        for i in range(13):
            text_on_page = text_on_page + " " + WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located(MainPageLocators.COLUMNS_DICT[i])).text
        text_on_page = text_on_page + " " + title
        print(text_on_page)

        isReliable, textBytesFound, lang_lit = cld2.detect(title)
        detect_lang = lang_lit[0][1]
        print (detect_lang)
        assert detect_lang == lang_interface, f"The title was not changed, detected {detect_lang}, used {lang_interface}"

    def should_be_change_currency(self,lang_interface="fil"):

        currency = MainPageLocators.LANGUAGE_BUTTONS_DICT[lang_interface][2]
        # current_currency = WebDriverWait(self.browser, 5).until(
        #     EC.element_to_be_clickable(MainPageLocators.CURRENCY_BUTTON)).text
        try:
            WebDriverWait(self.browser, 5).until(
                EC.text_to_be_present_in_element(MainPageLocators.CURRENCY_BUTTON, f"{currency}"))


        except TimeoutException:
            #print ("ded")
            current_currency = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable(MainPageLocators.CURRENCY_BUTTON)).text

            assert currency == current_currency, f"Currency name is not primary for this language currency = {currency}, current= {current_currency}"


        #assert currency == current_currency, f"Currency name is not primary for this language currency = {currency}, current= {current_currency}"

        #print("kek")

        # print(current_currency)
        print("ne upal")





    def Full(self,lang_interface="fil"):

        self.go_to_change_language(lang_interface)
        print("check text: \n")
        #time.sleep(2) # грязный костыль, пока не знаю как исправить
        self.should_be_change_currency(lang_interface)
        self.experiment_write_title(lang_interface)
        #self.should_be_good_language(lang_interface)
        self.should_be_lang_url(lang_interface)








