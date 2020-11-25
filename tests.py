import os

import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


# def test_sevrn(driver):
#     driver.get("http://localhost/litecart/admin/")
#     driver.find_element_by_name("username").send_keys("admin")
#     driver.find_element_by_name("password").send_keys("admin")
#     driver.find_element_by_name("login").click()
#     time.sleep(1)
#     loc = driver.find_elements_by_css_selector("li#app-")
#     for i in range(1, len(loc)+1):
#         driver.find_element_by_css_selector(f"li#app-:nth-child({i})").click()
#         newloc = driver.find_elements_by_css_selector("#app- li")
#         driver.find_element_by_tag_name("h1")
#         if len(newloc) > 1:
#             for j in range(1, len(newloc)+1):
#                 driver.find_element_by_css_selector(f"#app- li:nth-child({j})").click()
#                 driver.find_element_by_tag_name("h1")


# def test_eight(driver):
#     driver.get("http://localhost/litecart")
#     time.sleep(2)
#     product = driver.find_elements_by_css_selector(".product")
#     print(product)
#     for i in product:
#         i.find_element_by_xpath(".//div[contains(@class,'sticker')]")


# def test_nine_one(driver):
#     driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
#     driver.find_element_by_name("username").send_keys("admin")
#     driver.find_element_by_name("password").send_keys("admin")
#     driver.find_element_by_name("login").click()
#     time.sleep(1)
#     contryCSS = driver.find_elements_by_css_selector(".row")
#     contry = []
#     nomber = []
#     for i in contryCSS:
#         contry.append(i.find_element_by_xpath("./td[5]").text)
#         zones = int(i.find_element_by_xpath("./td[6]").text)
#         ids = int(i.find_element_by_xpath("./td[3]").text)
#         if zones > 0:
#             nomber.append(ids)
#     assert contry == sorted(contry)
#     for j in nomber:
#         driver.find_element_by_css_selector(f".row:nth-child({j + 1}) a").click()
#         table = driver.find_element_by_css_selector("#table-zones")
#         rows = table.find_elements_by_tag_name("tr")
#         strana = []
#         for row in rows[1:len(rows) - 1]:
#             a = row.find_element_by_xpath("./td[3]").text
#             strana.append(a)
#         driver.find_element_by_css_selector("[name=cancel]").click()
#         assert strana == sorted(strana)
#
#
# def test_nine_two(driver):
#     driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
#     driver.find_element_by_name("username").send_keys("admin")
#     driver.find_element_by_name("password").send_keys("admin")
#     driver.find_element_by_name("login").click()
#     time.sleep(1)
#     url = []
#     st = driver.find_element_by_css_selector(".dataTable")
#     row = st.find_elements_by_css_selector(".row")
#     for i in row:
#         url.append(i.find_element_by_tag_name("a").get_attribute("href"))
#     for u in url:
#         driver.get(u)
#         s = driver.find_element_by_css_selector("#table-zones")
#         row_zone = s.find_elements_by_tag_name("tr")
#         contry = []
#         for j in row_zone[1:len(row_zone)-1]:
#             f = j.find_element_by_css_selector('td:nth-of-type(3)> select option[selected]').text
#             contry.append(f)
#             assert contry == sorted(contry)
#         time.sleep(1)


# def test_ten(driver):
#     driver.get("http://localhost/litecart")
#     time.sleep(1)
#     products = driver.find_elements_by_css_selector(".product")
#     for i in products[5: 6]:
#         names = i.find_element_by_css_selector(".name").get_attribute("textContent")
#         regular_price = i.find_element_by_css_selector(".regular-price").get_attribute("textContent")
#         campaign_price = i.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
#         tag_regular_price = i.find_element_by_css_selector(".regular-price").get_attribute("tagName")
#         color_regular_price = i.find_element_by_css_selector(".regular-price").value_of_css_property("color").split()
#         assert color_regular_price[1] == color_regular_price[2]
#         tag_campaign_price = i.find_element_by_css_selector(".campaign-price").get_attribute("tagName")
#         color_campaign_price = i.find_element_by_css_selector(".campaign-price").value_of_css_property("color").split()
#         assert color_campaign_price[1] == color_campaign_price[2]
#         size_regular_price = i.find_element_by_css_selector(".regular-price").value_of_css_property('font-size')
#         size_regular_price = float(size_regular_price[0:-2])
#         size_campaign_price = i.find_element_by_css_selector(".campaign-price").value_of_css_property('font-size')
#         size_campaign_price = float(size_campaign_price[0:-2])
#         assert size_regular_price < size_campaign_price
#         driver.get(i.find_element_by_css_selector(".link").get_attribute("href"))
#         time.sleep(1)
#         names2 = driver.find_element_by_tag_name("h1").get_attribute("textContent")
#         assert names == names2
#         regular_price_2 = driver.find_element_by_tag_name(".regular-price").get_attribute("textContent")
#         assert regular_price == regular_price_2
#         campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
#         assert campaign_price == campaign_price_2
#         tag_regular_price_2 = driver.find_element_by_css_selector(".regular-price").get_attribute("tagName")
#         assert tag_regular_price == tag_regular_price_2
#         color_regular_price_2 = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color").split()
#         assert color_regular_price_2[1] == color_regular_price_2[2]
#         tag_campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").get_attribute("tagName")
#         assert tag_campaign_price == tag_campaign_price_2
#         color_campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color").split()
#         assert color_campaign_price_2[1] == color_campaign_price_2[2]
#         size_regular_price_2 = driver.find_element_by_css_selector(".regular-price").value_of_css_property('font-size')
#         size_regular_price_2 = float(size_regular_price_2[0:-2])
#         size_campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").value_of_css_property('font-size')
#         size_campaign_price_2 = float(size_campaign_price_2[0:-2])
#         assert size_regular_price_2 < size_campaign_price_2


# def test_eleven_reg(driver):
#     email = f'email{random.randint(0, 1000)}@yandex.ru'
#     pas = '123456789'
#     driver.get("http://localhost/litecart")
#     new = driver.find_element_by_tag_name('table')
#     new.find_element_by_tag_name('a').click()
#     time.sleep(1)
#     driver.find_element_by_name("firstname").send_keys("my_firstname")
#     time.sleep(1)
#     driver.find_element_by_name("lastname").send_keys("my_lastname")
#     time.sleep(1)
#     driver.find_element_by_name("address1").send_keys("my_address1")
#     time.sleep(1)
#     driver.find_element_by_name("postcode").send_keys("12345")
#     time.sleep(1)
#     driver.find_element_by_name("city").send_keys("my_city")
#     time.sleep(1)
#     select = driver.find_element_by_tag_name("select")
#     driver.execute_script("arguments[0].selectedIndex=224; arguments[0].dispatchEvent(new Event('change'))", select)
#     time.sleep(1)
#     driver.find_element_by_name("email").send_keys(f"{email}")
#     time.sleep(1)
#     driver.find_element_by_name("phone").send_keys('+79007001212')
#     time.sleep(1)
#     driver.find_element_by_name("password").send_keys(f"{pas}")
#     time.sleep(1)
#     driver.find_element_by_name("confirmed_password").send_keys(f"{pas}")
#     time.sleep(1)
#     driver.find_element_by_tag_name("button").click()
#     time.sleep(3)
#     sd = driver.find_elements_by_css_selector("#box-account a")
#     sd[-1].click()
#     time.sleep(3)
#     driver.find_element_by_name('email').send_keys(f'{email}')
#     time.sleep(1)
#     driver.find_element_by_name('password').send_keys(pas)
#     time.sleep(1)
#     driver.find_element_by_name('login').click()
#     time.sleep(2)
#     sd = driver.find_elements_by_css_selector("#box-account a")
#     sd[-1].click()
#     time.sleep(5)


# def test_twelve(driver):
#     driver.get("http://localhost/litecart/admin/")
#     driver.find_element_by_name("username").send_keys("admin")
#     driver.find_element_by_name("password").send_keys("admin")
#     driver.find_element_by_name("login").click()
#     time.sleep(1)
#     driver.find_element_by_css_selector(".list-vertical li:nth-child(2)").click()
#     time.sleep(1)
#     kol = len(driver.find_elements_by_css_selector(".dataTable .row"))
#     s = driver.find_elements_by_css_selector("#content .button")
#     s[-1].click()
#     time.sleep(1)
#     driver.find_element_by_name("status").click()
#     time.sleep(1)
#     driver.find_element_by_name("name[en]").send_keys("new product")
#     time.sleep(1)
#     driver.find_element_by_name("code").send_keys("1236")
#     time.sleep(1)
#     driver.find_element_by_css_selector("[value='1-3']").click()
#     time.sleep(1)
#     driver.find_element_by_name("quantity").clear()
#     time.sleep(1)
#     driver.find_element_by_name("quantity").send_keys('40')
#     time.sleep(1)
#     elm = driver.find_element_by_xpath("//input[@type='file']")
#     elm.send_keys(os.getcwd() + "/ime/duck.jpg")
#     time.sleep(1)
#     driver.find_element_by_css_selector(".index li:nth-child(2)").click()
#     time.sleep(1)
#     sel1 = Select(driver.find_element_by_name("manufacturer_id"))
#     time.sleep(1)
#     sel1.select_by_visible_text("ACME Corp.")
#     time.sleep(1)
#     driver.find_element_by_name("short_description[en]").send_keys('NEW PRODUCKT')
#     time.sleep(1)
#     driver.find_element_by_css_selector(".trumbowyg-editor").send_keys('NEW AMAZING PRODUCKT')
#     time.sleep(1)
#     driver.find_element_by_name("head_title[en]").send_keys('NEW PRODUCKT')
#     time.sleep(1)
#     driver.find_element_by_css_selector(".index li:nth-child(4)").click()
#     time.sleep(2)
#     driver.find_element_by_name("purchase_price").clear()
#     time.sleep(1)
#     driver.find_element_by_name("purchase_price").send_keys('10')
#     time.sleep(1)
#     sel2 = Select(driver.find_element_by_name("purchase_price_currency_code"))
#     sel2.select_by_visible_text("US Dollars")
#     time.sleep(1)
#     driver.find_element_by_name("save").click()
#     time.sleep(2)
#     kol_2 = len(driver.find_elements_by_css_selector(".dataTable .row"))
#     assert kol + 1 == kol_2
#     time.sleep(2)

def test_thirteen(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/")
    time.sleep(1)
    for i in range(1, 2):
        prod = driver.find_elements_by_css_selector(".image-wrapper")
        prod[0].click()
        element = driver.find_element_by_css_selector("#cart span.quantity")
        if driver.find_element_by_tag_name("h1").text == "Yellow Duck":
            select = driver.find_element_by_tag_name("select")
            driver.execute_script("arguments[0].selectedIndex=2; arguments[0].dispatchEvent(new Event('change'))",
                                  select)
            driver.find_element_by_name("add_cart_product").click()
        else:
            driver.find_element_by_name("add_cart_product").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart span.quantity"), f'{i}'))
        element = driver.find_element_by_css_selector("#cart span.quantity")
        assert element.text == f'{i}'
        driver.find_element_by_id("logotype-wrapper").click()

    driver.find_element_by_css_selector("#cart .link").click()
    # wait.until(EC.presence_of_element_located(By.CSS_SELECTOR(".dataTable tr")))
    l = driver.find_element_by_css_selector(".dataTable")
    r = len(l.find_elements_by_tag_name("tr")) - 5
    for j in range(r):
        table = driver.find_element_by_css_selector(".dataTable")
        but = driver.find_element_by_css_selector("li:first-child [name=remove_cart_item]")
        wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR("li:first-child [name=remove_cart_item]")))
        but.click()
        wait.until(EC.staleness_of(table))
        time.sleep(2)


# def test_fourteen(driver):
#     driver.get("http://localhost/litecart/admin")
#     driver.find_element_by_name("username").send_keys("admin")
#     driver.find_element_by_name("password").send_keys("admin")
#     driver.find_element_by_name("login").click()
#     time.sleep(1)
#     driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
#     time.sleep(1)
#     countries = driver.find_elements_by_css_selector(".row")
#     for i in countries[0: 1]:
#         i.find_element_by_xpath("./td[7]").click()
#         time.sleep(3)
#         lst = driver.find_elements_by_css_selector("#content table [target='_blank']")
#         for j in lst:
#             main_window = [driver.current_window_handle]  # текущее окон
#             j.click()
#             WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
#             old_windows = driver.window_handles  # список открытых окон
#             new_windows = list(set(old_windows) - set(main_window))
#             driver.switch_to_window(new_windows[0])
#             driver.close()
#             driver.switch_to_window(main_window[0])
#         driver.find_element_by_name("cancel").click()


def test_seventeen(driver):
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    lst = driver.find_elements_by_css_selector(".dataTable .row")
    for i in range(3, len(lst)):
        a = driver.find_elements_by_css_selector(".dataTable .row")
        a[i].find_element_by_tag_name("a").click()
        time.sleep(2)
        for l in driver.get_log("browser"):
            print(l)
        driver.find_element_by_name("cancel").click()
