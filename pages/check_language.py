#from langdetect.detector_factory import detect
import cld2
title = "Mga Ranking Kagamitan Mga Mapagkukunan Blog Nangungunang 100 Mga Cryptocurrency ng Market Capitalization Rank	Pangalan Market Cap Presyo	Dami (24 na oras)	Umiikot na Supply Pagbabago (24h) Graph ng Presyo (7d)"
isReliable, textBytesFound, lang_lit = cld2.detect(title)
print(lang_lit)
#print (cld2.LANGUAGES)


def should_be_change_currency(self, lang_interface="fil"):
    # current_currency = WebDriverWait(self.browser, 5).until(
    #     EC.element_to_be_clickable(MainPageLocators.CURRENCY_BUTTON))
    # current_currency.click()#
    currency = MainPageLocators.LANGUAGE_BUTTONS_DICT[lang_interface][2]
    kek = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(MainPageLocators.CURRENCY_BUTTON)).text
    # Периодически падает так как грузит не актуальные данные

    current_currency = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable(MainPageLocators.CURRENCY_VALUE)).text

    print(kek)
    print("ne upal")
