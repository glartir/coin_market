from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
       # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def change_window_size(self,height=1280,width=1024):
        self.browser.set_window_size(height, width)

    def wait_and_click_button(self,how,what,timeout=4):
        button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((how,what)))

        button.click()
