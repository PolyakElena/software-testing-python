import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time


# def test_example(driver):
#     driver.get("http://localhost/litecart/admin/")
#     driver.find_element_by_name("username").send_keys("admin")
#     time.sleep(1)
#     driver.find_element_by_name("password").send_keys("admin")
#     time.sleep(1)
#     driver.find_element_by_name("login").click()
#     time.sleep(1)
#     loc = driver.find_element_by_css_selector("li#app-")
#     d = int(len(loc)) - 1
#     for i in range(0, d):
#         driver.get(i).click()
#         newloc = driver.find_element_by_css_selector("#app-.selected li")
#         if newloc > 1:
#             for j in range(0, int(len(newloc)) - 1):
#                 newloc.get(j).click()
#                 newloc = driver.find_element_by_css_selector("#app-.selected li")
#                 loc = driver.find_element_by_css_selector("li#app-")
#                 driver.find_element_by_tag_name("h1")
#         else:
#             loc = driver.find_element_by_css_selector("li#app-")
#             driver.find_element_by_tag_name("h1")
#             loc.get(i).click()

def test_eight(driver):
    driver.get("http://localhost/litecart")
    time.sleep(2)
    product = driver.find_elements_by_css_selector(".product")
    print(product)
    for i in product:
        i.find_element_by_xpath(".//div[contains(@class,'sticker')]")

