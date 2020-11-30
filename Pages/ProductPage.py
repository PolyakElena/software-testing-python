from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)

    def open(self, link: str):
        self.driver.get(link)
        return self

    def first_prod(self):
        return self.driver.find_element_by_css_selector('.product > a').get_attribute('href')

    def products_in_cart(self):
        return int(self.driver.find_element_by_css_selector("#cart span.quantity").text)

    def add_product(self):
        element = self.products_in_cart()
        if self.driver.find_element_by_tag_name("h1").text == "Yellow Duck":
            select = self.driver.find_element_by_tag_name("select")
            self.driver.execute_script("arguments[0].selectedIndex=2; arguments[0].dispatchEvent(new Event('change'))",
                                       select)
            self.driver.find_element_by_name("add_cart_product").click()
        else:
            self.driver.find_element_by_name("add_cart_product").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#cart span.quantity"), str(element+1)))
