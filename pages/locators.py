from selenium.webdriver.common.by import By

class MainPageLocators():

    TITLE_TEXT=(By.CSS_SELECTOR, '.sc-1m8sms1-1')
    SWAP_BUTTON = (By.CSS_SELECTOR, '.frscwy-2:nth-child(2)')


    #LANGUAGE_BUTTON_DE=(By.CSS_SELECTOR, '.frscwy-3:nth-child(1)')
    # LANGUAGE_BUTTONS_DICT=\
    #     {
    #         "de" : (By.CSS_SELECTOR, '.frscwy-3:nth-child(1)'),
    # } На случай если нужна будет такая запись

    LANGUAGE_BUTTONS_DICT = { "de" : (By.CSS_SELECTOR, '[href="/de/"]'),      #Deutsch
                              "en": (By.CSS_SELECTOR, '[href="/"]'),          #English
                              "es": (By.CSS_SELECTOR, '[href="/es/"]'),       #Español
                              "fil": (By.CSS_SELECTOR, '[href="/fil/"]'),     #Filipino
                              "fr": (By.CSS_SELECTOR, '[href="/fr/"]'),       #Français
                              "hi": (By.CSS_SELECTOR, '[href="/hi/"]'),       #हिन्दी
                              "it": (By.CSS_SELECTOR, '[href="/it/"]'),       #Italiano
                              "ja": (By.CSS_SELECTOR, '[href="/ja/"]'),       #日本語
                              "ko": (By.CSS_SELECTOR, '[href="/ko/"]'),       #한국어
                              "pt-br": (By.CSS_SELECTOR, '[href="/pt-br/"]'), #Português Brasil
                              "ru": (By.CSS_SELECTOR, '[href="/ru/"]'),       #Русский
                              "tr": (By.CSS_SELECTOR, '[href="/tr/"]'),       #Türkçe
                              "vi": (By.CSS_SELECTOR, '[href="/vi/"]'),       #Tiếng Việt
                              "zh": (By.CSS_SELECTOR, '[href="/zh/"]'),       #简体中文
                              "zh-tw": (By.CSS_SELECTOR, '[href="/zh-tw/"]'), #繁體中文

                              }


