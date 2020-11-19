import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time


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


# def test_nine(driver):
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

def test_ten(driver):
    driver.get("http://localhost/litecart")
    time.sleep(1)
    products = driver.find_elements_by_css_selector(".product")
    for i in products[5: 6]:
        # imeges = i.find_element_by_css_selector(".image").get_attribute('src')
        names = i.find_element_by_css_selector(".name").get_attribute("textContent")
        regular_price = i.find_element_by_css_selector(".regular-price").get_attribute("textContent")
        campaign_price = i.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
        tag_regular_price = i.find_element_by_css_selector(".regular-price").get_attribute("tagName")
        color_regular_price = i.find_element_by_css_selector(".regular-price").value_of_css_property("color").split()
        assert color_regular_price[1] == color_regular_price[2]
        tag_campaign_price = i.find_element_by_css_selector(".campaign-price").get_attribute("tagName")
        color_campaign_price = i.find_element_by_css_selector(".campaign-price").value_of_css_property("color").split()
        assert color_campaign_price[1] == color_campaign_price[2]
        size_regular_price = i.find_element_by_css_selector(".regular-price").size
        size_campaign_price = i.find_element_by_css_selector(".campaign-price").size
        assert size_regular_price['height'] < size_campaign_price['height']
        assert size_regular_price['width'] < size_campaign_price['width']
        driver.get(i.find_element_by_css_selector(".link").get_attribute("href"))
        time.sleep(1)
        # image2 = driver.find_element_by_css_selector(".image").get_attribute('src')
        names2 = driver.find_element_by_tag_name("h1").get_attribute("textContent")
        assert names == names2
        regular_price_2 = driver.find_element_by_tag_name(".regular-price").get_attribute("textContent")
        assert regular_price == regular_price_2
        campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").get_attribute("textContent")
        assert campaign_price == campaign_price_2
        tag_regular_price_2 = driver.find_element_by_css_selector(".regular-price").get_attribute("tagName")
        assert tag_regular_price == tag_regular_price_2
        color_regular_price_2 = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color").split()
        assert color_regular_price_2[1] == color_regular_price_2[2]
        tag_campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").get_attribute("tagName")
        assert tag_campaign_price == tag_campaign_price_2
        color_campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color").split()
        assert color_campaign_price_2[1] == color_campaign_price_2[2]
        size_regular_price_2 = driver.find_element_by_css_selector(".regular-price").size
        size_campaign_price_2 = driver.find_element_by_css_selector(".campaign-price").size
        assert size_regular_price_2['height'] < size_campaign_price_2['height']
        assert size_regular_price_2['width'] < size_campaign_price_2['width']





