import pytest
import requests
import sys,os
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from Object_Repository import Object_Repository as ob
from datetime import datetime
from time import sleep

class Test_Internet(ob):

    @pytest.fixture(params=["Chrome","Firefox"],scope="class")
    def open_browser(self,request):
        if request.param == 'Chrome':
            driver = webdriver.Chrome()
            driver.implicitly_wait(2)
        elif request.param == 'Firefox':
            driver = webdriver.Firefox()
            driver.implicitly_wait(2)
        elif request.param == 'Safari':
            driver = webdriver.Safari()
        yield driver
        driver.quit()

    @pytest.mark.skip(reason='Completed')
    def test_abtesting(self,open_browser):
        open_browser.get(ob.hiurl)
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_InternetStartPage.png")
        open_browser.find_element_by_xpath(ob.abtest_link).click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_ABTestingPage.png")
        display_text = open_browser.find_element_by_css_selector(ob.abtest_css).text
        expected_text = 'A/B Test Control'
        expected_text2 = 'A/B Test Variation 1'
        if display_text == expected_text:
            assert display_text == expected_text
        else:
            assert display_text == expected_text2
        expected_footer_head = 'Powered by '
        expected_footer_tail = 'Elemental Selenium'
        displayed_footer = open_browser.find_element_by_xpath(ob.footer_xpath_head).text
        assert expected_footer_head+expected_footer_tail == displayed_footer
        footer_tail = open_browser.find_element_by_xpath(ob.footer_xpath_tail)
        displayed_footer_tail = footer_tail.text
        assert expected_footer_tail == displayed_footer_tail
        footer_tail.click()
        handels = open_browser.window_handles
        size = len(handels)
        for i in range(1,size):
            active_tab = open_browser.window_handles[i]
            open_browser.switch_to.window(active_tab)
            dt = str(datetime.now())
            open_browser.get_screenshot_as_file(dt+"_ElementPage.png")

    @pytest.mark.skip(reason='Completed')
    def test_addremove_element(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.addremove_link).click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_AddRemoveElement.png")
        num_click = randrange(1,5)
        for i in range(0,num_click):
            open_browser.find_element_by_xpath(ob.addelement_xpath).click()
        open_browser.get_screenshot_as_file(dt+"_AfterAddBtnClick.png")
        delete_buttons = open_browser.find_elements_by_xpath(ob.delete_xpath)
        bts = len(delete_buttons)
        assert num_click == bts
        for i in range(0,bts):
            delete_buttons[i].click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_DeleteBtnClick.png")

    @pytest.mark.skip(reason='Completed')
    def test_basic_auth(self,open_browser):
        open_browser.get(ob.ba_url)
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_HandeledBasicAuth.png")

    @pytest.mark.skip(reason='Not able to design -test case already covered')
    def test_basic_ath(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.basic_auth).click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_BasicAuth.png")
        dt = str(datetime.now())
        handels = open_browser.window_handles
        size = len(handels)
        for i in range(1,size):
            active_tab = open_browser.window_handles[i]
            open_browser.switch_to.window(active_tab)
        open_browser.get_screenshot_as_file(dt+"_HandeledBasicAuth.png")

    @pytest.mark.skip(reason='Completed')
    def test_broken_img(self,open_browser):
        open_browser.get(ob.hiurl)
        brokenimglink = WebDriverWait(open_browser,5).until(EC.presence_of_element_located((By.XPATH,ob.broken_img_link)))
        # open_browser.find_element_by_xpath(ob.broken_img_link).click
        brokenimglink.click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_BrokenImg.png")
        img_elements  = open_browser.find_elements_by_xpath('//img')
        valid_img = 0
        broken_img = 0
        for image in img_elements:
            try:
                response = requests.get(image.get_attribute('src'))
                if response.status_code == 200:
                    valid_img +=1
                elif response.status_code == 404:
                    broken_img +=1
            except:
                print("Encountered Some other Exception")
        assert broken_img == 2

    @pytest.mark.skip(reason='Yet to Design')
    def test_challening_dom(self,open_browser):
        open_browser.get(ob.hiurl)
        challenging = WebDriverWait(open_browser,2).until(EC.presence_of_element_located((By.XPATH,ob.Challenging_DOM)))
        challenging.click()

    @pytest.mark.skip(reason='Completed')
    def test_checkboxes(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.Checkboxes).click()
        checkbox_in_page = open_browser.find_elements_by_xpath(ob.checkbx)
        for ck in checkbox_in_page:
            if ck.is_selected():
                ck.click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_unchecked.png")
        for ck in checkbox_in_page:
            ck.click()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_checked.png")

    @pytest.mark.skip(reason='Completed')
    def test_context_menu_popup(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.Contextmenu).click()
        #Create the action to right click over an item and calls on it
        # right_click = ActionChains(driver)
        # hot_spot = driver.find_element_by_id("hot-spot")
        # right_click.context_click(hot_spot).perform()
        # sleep(1)
        #Alert handling focusing on it and clicking in the accepting button
        # alert_obj = driver.switch_to.alert
        # dt = str(datetime.now())
        # driver.get_screenshot_as_file(dt+"_alert.png")
        # alert_obj.accept()
        box = open_browser.find_element_by_id("hot-spot")
        action = ActionChains(open_browser)
        # dt = str(datetime.now())
        # driver.get_screenshot_as_file(dt+"_contextbox.png")
        # #action.move_to_element(box)
        action.context_click(box).perform()
        sleep(1)
        a = open_browser.switch_to.alert
        c_text = a.text
        a.accept()
        expected_text = 'You selected a context menu'
        assert c_text == expected_text
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_alert.png")




    @pytest.mark.skip(reason='Yet to design')
    def test_digest_auth(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.Digest_Authentication).click()

    @pytest.mark.skip(reason='Completed')
    def test_drag_drop(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.drag_drop).click()
        open_browser.maximize_window()
        a = open_browser.find_element_by_id(ob.aloc)
        b = open_browser.find_element_by_id(ob.bloc)
        sleep(2)
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_dranganddropafter.png")
        open_browser.execute_script("function createEvent(typeOfEvent) {\n" + "var event =document.createEvent(\"CustomEvent\");\n"
                    + "event.initCustomEvent(typeOfEvent,true, true, null);\n" + "event.dataTransfer = {\n" + "data: {},\n"
                    + "setData: function (key, value) {\n" + "this.data[key] = value;\n" + "},\n"
                    + "getData: function (key) {\n" + "return this.data[key];\n" + "}\n" + "};\n" + "return event;\n"
                    + "}\n" + "\n" + "function dispatchEvent(element, event,transferData) {\n"
                    + "if (transferData !== undefined) {\n" + "event.dataTransfer = transferData;\n" + "}\n"
                    + "if (element.dispatchEvent) {\n" + "element.dispatchEvent(event);\n"
                    + "} else if (element.fireEvent) {\n" + "element.fireEvent(\"on\" + event.type, event);\n" + "}\n"
                    + "}\n" + "\n" + "function simulateHTML5DragAndDrop(element, destination) {\n"
                    + "var dragStartEvent =createEvent('dragstart');\n" + "dispatchEvent(element, dragStartEvent);\n"
                    + "var dropEvent = createEvent('drop');\n"
                    + "dispatchEvent(destination, dropEvent,dragStartEvent.dataTransfer);\n"
                    + "var dragEndEvent = createEvent('dragend');\n"
                    + "dispatchEvent(element, dragEndEvent,dropEvent.dataTransfer);\n" + "}\n" + "\n"
                    + "var source = arguments[0];\n" + "var destination = arguments[1];\n"
                    + "simulateHTML5DragAndDrop(source,destination);",a,b)
        #actions = ActionChains(driver)
        #actions.click_and_hold(a).pause(2).move_to_element(b).pause(2).release(b).perform()
        sleep(2)
        #actions.drag_and_drop(a,b).perform()
        dt = str(datetime.now())
        open_browser.get_screenshot_as_file(dt+"_dranganddropafter.png")

    @pytest.mark.skip(reason='Completed')
    def test_dropdown(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.dropdownlink).click()
        select = Select(open_browser.find_element_by_xpath(ob.dropdownid))
        select.select_by_visible_text('Option 1')
        dt = str(datetime.now().strftime("%d%m%Y%H%M%S"))
        fdt = str(datetime.now().strftime("%d%m%Y"))

        # screenshortpath = "./Users/adusumilli/Development/Automate/screenshots/"
        # screenshot = screenshortpath+"dropdown.png"
        open_browser.save_screenshot('\AutomationScreenshots\test.png')

    @pytest.mark.skip(reason='Completed')
    def test_dynamic_controls(self,open_browser):
        open_browser.get(ob.hiurl)
        open_browser.find_element_by_xpath(ob.dymcontrol).click()
