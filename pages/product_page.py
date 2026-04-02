from pages.base_page import BasePage

class ProductPage(BasePage):
    ADDTOCART_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    SHOPPINT_CART = "[data-test=shopping-cart-link]"
    CHECKOUT_BUTTON = "#checkout"

    def clickShoppingCart(self):
        self.click(self.ADDTOCART_BACKPACK)
        self.click(self.SHOPPINT_CART)

    def clickCheckoutButton(self):
        self.click(self.CHECKOUT_BUTTON)