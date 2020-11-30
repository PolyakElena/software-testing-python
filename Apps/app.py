from selenium import webdriver
from Pages.CartPage import CartPage
from Pages.MainPage import MainPage
from Pages.ProductPage import ProductPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_products(self, number: int):
        for i in range(number):
            self.add_product()

    def add_product(self):
        self.main_page.open()
        self.product_page.open(self.main_page.first_prod())
        self.product_page.add_product()

    def delete_all_products_from_cart(self):
        self.cart_page.open()
        self.cart_page.delete_all_products()
