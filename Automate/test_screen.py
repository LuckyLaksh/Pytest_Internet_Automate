import pytest
import sys, os
from datetime import datetime
from selenium import webdriver

class Test_Screenshot:
    def test_webpage_screen(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        # path = ''
        #Working after creating specific folder
        dt = str(datetime.now().strftime("%d%m%Y%H:%M:%S"))
        fdt = str(datetime.now().strftime("%d%m%Y"))
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        screenshotpath = os.path.join(os.path.sep, ROOT_DIR,'Screenshots'+ os.sep)
        driver.get_screenshot_as_file(screenshotpath+dt+"testPngFunction.png")

        #not working for screenshots
        #driver.save_screenshot('/Screenshots/foo.png')
        # driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), '//Users//adusumilli//Development//Automate//Screenshot_folder', 'test.png'))
        driver.quit()

ts = Test_Screenshot
ts.test_webpage_screen
