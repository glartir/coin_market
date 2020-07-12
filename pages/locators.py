from selenium.webdriver.common.by import By

class MainPageLocators():

    TITLE_TEXT=(By.CSS_SELECTOR, '.sc-1m8sms1-1')
    SWAP_BUTTON = (By.CSS_SELECTOR, '.frscwy-2:nth-child(2)')
    CURRENCY_BUTTON = (By.CSS_SELECTOR, '.v3c0kr-0 button')
    CURRENCY_VALUE = (By.CSS_SELECTOR, '.cmc-menu-item:nth-child(1)')



    #LANGUAGE_BUTTON_DE=(By.CSS_SELECTOR, '.frscwy-3:nth-child(1)')
    # LANGUAGE_BUTTONS_DICT=\
    #     {
    #         "de" : (By.CSS_SELECTOR, '.frscwy-3:nth-child(1)'),
    # } На случай если нужна будет такая запись
    COLUMNS_DICT = {0 : (By.CSS_SELECTOR, '.NavbarItem__NavbarItemEl-sc-1a0iugo-1:nth-child(1)'),
                   1  : (By.CSS_SELECTOR, '.NavbarItem__NavbarItemEl-sc-1a0iugo-1:nth-child(2)'),
                   2  : (By.CSS_SELECTOR, '.NavbarItem__NavbarItemEl-sc-1a0iugo-1:nth-child(3)'),
                   3  : (By.CSS_SELECTOR, '.NavbarItem__NavbarItemEl-sc-1a0iugo-1:nth-child(4)'),
                   4  : (By.CSS_SELECTOR, '.NavbarItem__NavbarItemEl-sc-1a0iugo-1:nth-child(5)'),
                   5  : (By.CSS_SELECTOR,'.cmc-table__table-wrapper-outer:nth-child(3) >div >table >thead >tr > .cmc-table__header:nth-child(1)'),
                   6  : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(2)'),
                   7  : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(3)'),
                   8  : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(4)'),
                   9  : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(5)'),
                   10 : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(6)'),
                   11 : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(7)'),
                   12 : (By.CSS_SELECTOR, '.cmc-table__table-wrapper-outer:nth-child(3) > div >table > thead >tr >.cmc-table__header:nth-child(8)')


                     }
    LANGUAGE_BUTTONS_DICT = { "de":[ (By.CSS_SELECTOR, '[href="/de/"]'), "de","EUR"],            #Deutsch
                              "en": [ (By.CSS_SELECTOR, '[href="/"]'),   "en", "USD"],           #English
                              "es": [ (By.CSS_SELECTOR, '[href="/es/"]'),"es", "USD"],           #Español
                              "fil":[(By.CSS_SELECTOR, '[href="/fil/"]'),"tl", "PHP"],           #Filipino
                              "fr": [(By.CSS_SELECTOR, '[href="/fr/"]'), "fr", "EUR"],           #Français
                              "hi": [(By.CSS_SELECTOR, '[href="/hi/"]'), "hi", "USD"],           #हिन्दी
                              "it": [(By.CSS_SELECTOR, '[href="/it/"]'), "it", "EUR"],           #Italiano
                              "ja": [(By.CSS_SELECTOR, '[href="/ja/"]'), "ja", "JPY"],           #日本語
                              "ko": [(By.CSS_SELECTOR, '[href="/ko/"]'), "ko", "KRW"],           #한국어
                              "pt-br": [(By.CSS_SELECTOR, '[href="/pt-br/"]'),"pt", "BRL"],      #Português Brasil
                              "ru": [(By.CSS_SELECTOR, '[href="/ru/"]'), "ru", "RUB"],           #Русский
                              "tr": [(By.CSS_SELECTOR, '[href="/tr/"]'), "tr", "TRY"],           #Türkçe
                              "vi": [(By.CSS_SELECTOR, '[href="/vi/"]'), "vi", "USD"],           #Tiếng Việt
                              "zh": [(By.CSS_SELECTOR, '[href="/zh/"]'), "zh", "CNY"],           #简体中文
                              "zh-tw": [(By.CSS_SELECTOR, '[href="/zh-tw/"]'), "zh-Hant", "TWD"] #繁體中文

                              }
    # LANGUAGE_TO_TRANSLATE_AND_CURRENCY = { "de" : ["de","EUR"],
    #                                        "en": ["en", "USD"],
    #                                        "es": ["es", "USD"],
    #                                        "fil": ["tl", "PHP"],
    #                                        "fr": ["fr", "EUR"],
    #                                        "hi": ["hi", "USD"],
    #                                        "it": ["it", "EUR"],
    #                                        "ja": ["ja", "JPY"],
    #                                        "ko": ["ko", "USD"],
    #                                        "pt-br": ["pt", "BRL"],
    #                                        "ru": ["ru", "RUB"],
    #                                        "tr": ["tr", "TRY"],
    #                                        "vi": ["vi", "USD"],
    #                                        "zh": ["zh", "CNY"],
    #                                        "zh-": ["zh-Hant", "TWD"],
    #
    #                                        }

