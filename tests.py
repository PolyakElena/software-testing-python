import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time


def test_sevrn(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    time.sleep(1)
    loc = driver.find_elements_by_css_selector("li#app-")
    for i in range(1, len(loc)+1):
        driver.find_element_by_css_selector(f"li#app-:nth-child({i})").click()
        newloc = driver.find_elements_by_css_selector("#app- li")
        driver.find_element_by_tag_name("h1")
        if len(newloc) > 1:
            for j in range(1, len(newloc)+1):
                driver.find_element_by_css_selector(f"#app- li:nth-child({j})").click()
                driver.find_element_by_tag_name("h1")


# def test_eight(driver):
#     driver.get("http://localhost/litecart")
#     time.sleep(2)
#     product = driver.find_elements_by_css_selector(".product")
#     print(product)
#     for i in product:
#         i.find_element_by_xpath(".//div[contains(@class,'sticker')]")

