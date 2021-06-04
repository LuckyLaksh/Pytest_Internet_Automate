from selenium import webdriver as wb
from selenium.common.exceptions import TimeoutException

class CustomDriver(wb):
    def __init__(self, browser):
        if browser.lower() == 'chrome':
            self.driver = wb.Chrome()

    # def exit_browser(self):
    #     self.driver.quit()

    def get_url(self, url):
        try:
            self.driver.get(url)
        except TimeoutException:
            self.driver.quit()


mydriver = CustomDriver('Chrome')
mydriver.get_url("https://www.google.com/")
