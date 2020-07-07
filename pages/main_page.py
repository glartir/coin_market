from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_change_language(self):
        self.change_window_size()
        self.wait_and_click_button(*MainPageLocators.SWAP_BUTTON)
        self.wait_and_click_button(*MainPageLocators.LANGUAGE_BUTTON_DE)

        #Дописать ожидания.ч




