from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 7)

    def open(self):
        self.driver.get('http://localhost/litecart/en/checkout')
        return self

    def delete_all_products(self):
        shortcut_li = self.driver.find_element_by_css_selector('ul.shortcuts > li')
        shortcut_li.click()
        for i in range(len(self.driver.find_elements_by_css_selector('ul.shortcuts > li'))):
            self.del_product()

    def del_product(self):
        table = self.driver.find_elements_by_css_selector('#checkout-summary-wrapper tr')[1]
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li:first-child [name='remove_cart_item']")))
        self.driver.find_element_by_css_selector("li:first-child [name='remove_cart_item']").click()
        self.wait.until(EC.staleness_of(table))
