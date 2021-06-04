import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from Object_Repository import Object_Repository as ob
from datetime import datetime


@pytest.mark.skip(reason='Out of Scope: Completed no more test objective')
class Test_Case_Launch(ob):
    def test_website_launch(self):
        driver = webdriver.Chrome()
        driver.get(ob.url)
        assert ob.title_text == driver.title
        search_box = driver.find_element_by_css_selector(ob.search_css_locator)
        dt = str(datetime.now())
        driver.get_screenshot_as_file("before_search"+dt+".png")
        search_box.send_keys("Apple")
        search_button = driver.find_element_by_css_selector(ob.search_btn_css_locator)
        dt = str(datetime.now())
        driver.get_screenshot_as_file("after_search"+dt+".png")
        search_button.click()
        driver.get_screenshot_as_file("after_click"+dt+".png")
        #in_item_value = driver.find_element_by_xpath(ob.items_xpath_locator)
        #in_price_vlaue = driver.find_element_by_xpath(ob.price_xpath_locator)
        item_v = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,ob.items_css_locator)))
        item_value = item_v.text
        cart_button = driver.find_element_by_css_selector(ob.addtocart_css_locator)
        cart_button.click()
        dt = str(datetime.now())
        driver.get_screenshot_as_file("after_addtocart"+dt+".png")

        #print(cart_button.text
        #fi_item_value = driver.find_element_by_xpath(ob.items_xpath_locator)
        #fi_price_vlaue = driver.find_element_by_xpath(ob.price_xpath_locator)
        driver.quit()
    def test_facebook_login(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(options=options)
        driver.get(ob.fb)
        dt = str(datetime.now())
        driver.get_screenshot_as_file("fb_login_page"+dt+".png")
        driver.find_element_by_css_selector(ob.user_css_locator).send_keys("a.ravi99@yahoo.in")
        driver.find_element_by_css_selector(ob.pass_css_locator).send_keys("19932308")
        dt = str(datetime.now())
        driver.get_screenshot_as_file("fb_login_page"+dt+".png")
        driver.find_element_by_css_selector(ob.btn_css_locator).click()
        dt = str(datetime.now())
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("fb_after_login_page"+dt+".png")
        post_click = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,ob.postclick_css_locator)))
        post_click.click()
        # actions = ActionChains(driver)
        # actions.send_keys("HELLO WORLD")
        # actions.perform()
        driver.implicitly_wait(2)
        # act_postwindow = driver.switch_to.active_element()
        # act_postwindow.send_keys("HELLO WORLD")
        post_wall = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,ob.wall_css_loc)))
        post_wall.send_keys("HELLO WORLD")
        # driver.find_element_by_css_selector(ob.wall_css_loc).send_keys("HELLO WORLD")
        #wall_css_loc
        dt = str(datetime.now())
        driver.get_screenshot_as_file("fb_before_post"+dt+".png")
        driver.implicitly_wait(2)
        driver.find_element_by_css_selector(ob.post_btn).click()
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("fb_after_post"+dt+".png")
        driver.quit()
    def test_gmail(self):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(options=options)
        driver.get(ob.gmail)
        dt = str(datetime.now())
        driver.get_screenshot_as_file("gmail_login_page"+dt+".png")
        driver.find_element_by_css_selector(ob.gmail_user_css).send_keys("bloggger1993")
        next_button = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,ob.gmail_next_css)))
        #driver.find_element_by_css_selector(ob.gmail_next_css).click()
        next_button.click()
        dt = str(datetime.now())
        driver.get_screenshot_as_file("gmail_next_page"+dt+".png")
        password_t = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,ob.gmail_password_css)))
        password_t.send_keys("19932308")
        #driver.find_element_by_css_selector(ob.gmail_password_css).send_keys("19932308")
        dt = str(datetime.now())
        driver.get_screenshot_as_file("gmail_login"+dt+".png")
        #driver.find_element_by_css_selector(ob.gmail_next_css).click()
        next_button2 = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,ob.gmail_next_css)))
        next_button2.click()
        dt = str(datetime.now())
        driver.implicitly_wait(2)
        driver.get_screenshot_as_file("gmail_after_login_page"+dt+".png")
        text = driver.find_element_by_css_selector(ob.gmail_attribute).get_attribute('aria-label')
        print(text)
        driver.quit()













tc = Test_Case_Launch
#tc.test_website_launch
#tc.test_facebook_login
tc.test_gmail
