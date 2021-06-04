class Object_Repository:
    ''' Rahul Shetty Greenkart Objects Respository '''
    url = 'https://rahulshettyacademy.com/seleniumPractise/#/'
    title_text = 'GreenKart - veg and fruits kart'
    search_css_locator = '[class=search-keyword]'
    search_btn_css_locator = '[class=search-button]'
    items_xpath_locator = "//td[contains(text(),'Items')]/following-sibling::td/strong"
    price_xpath_locator = "//td[contains(text(),'Price')]/following-sibling::td/strong"
    items_css_locator = "div.cart-info > table > tbody > tr:nth-child(1) > td:nth-child(3) > strong"
    price_css_locator = "div.cart-info > table > tbody > tr:nth-child(2) > td:nth-child(3) > strong"
    addtocart_css_locator = "div.product-action > button"
    addtocart_before_txt = 'ADD TO CART'
    addtocart_after_txt = 'ADDED'
    ''' Facebook Objects Respository  '''
    fb = "https://www.facebook.com/"
    user_css_locator = "[data-testid=royal_email]"
    pass_css_locator = "[data-testid=royal_pass]"
    btn_css_locator = "[data-testid=royal_login_button]"
    postclick_css_locator = "div.k4urcfbm.g5gj957u.buofh1pr.j83agx80.ll8tlv6m > div"
    wall_css_locator = "[aria-label*='What\'s on your mind,']"
    wall_css_loc = "div._5rpb > div"
    post_btn = "div.k4urcfbm.dati1w0a.hv4rvrfc.i1fnvgqd.j83agx80.rq0escxv.bp9cbjyn.discj3wi > div"

    '''Gmail login and validation'''
    gmail ='https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier'
    gmail_user_css = '[type=email]'
    gmail_next_css = '[type=button][jsname=LgbsSe]'
    gmail_password_css = '[type=password]'
    gmail_attribute = '[aria-label*=\'Google Account:\']'

    ''' Multiple Items Selenium '''
    mul = "https://rahulshettyacademy.com/AutomationPractice/"
    r_css_one = "fieldset > label:nth-child(2)"
    r_css_two = "fieldset > label:nth-child(3)"
    r_css_three = "fieldset > label:nth-child(4)"
    open_tab = "//*[@id='opentab']"

    ''' Internet Heroku App '''
    hiurl = 'https://the-internet.herokuapp.com/'
    abtest_link = '//a[contains(text(),"A/B Testing")]'
    abtest_css = 'h3'
    footer_xpath_head = '//*[@id="page-footer"]/div/div'
    footer_xpath_tail = '//*[@id="page-footer"]/div/div/a'
    addremove_link = '//a[contains(text(),"Add/Remove Elements")]'
    addelement_xpath = '//button[contains(text(),"Add Element")]'
    delete_xpath = '//button[contains(text(),"Delete")]'
    basic_auth = '//a[contains(text(),"Basic Auth")]'
    ba_url = 'https://<admin>:<admin>@the-internet.herokuapp.com/basic_auth'
    broken_img_link = '//a[contains(text(),"Broken Images")]'
    Challenging_DOM = '//a[contains(text(),"Challenging DOM")]'
    Checkboxes = '//a[contains(text(),"Checkboxes")]'
    checkbx = '//form/input'
    Contextmenu = '//a[contains(text(),"Context Menu")]'
    hotbox = '//*[@id="hot-spot"]'
    Digest_Authentication = '//a[contains(text(),"Broken Images")]'
    drag_drop = '//a[contains(text(),"Drag and Drop")]'
    a_loc= '//*[@id="column-a"]'
    aloc = 'column-a'
    bloc = 'column-b'
    b_loc= '//*[@id="column-b"]'
    dropdownlink = '//a[contains(text(),"Dropdown")]'
    dropdownid = '//*[@id="dropdown"]'
    dymcontrol = '//a[contains(text(),"Dynamic Controls")]'
