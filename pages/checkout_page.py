from pages.base_page import BasePage
import logging
import allure

logger = logging.getLogger(__name__)

class CheckoutPage(BasePage):
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE = "#continue"
    FINISH = "#finish"
    INVENTORY_ITEM_NAME = "[data-test='inventory-item-name']"

    def enterCheckoutInformation(self, firstName, lastName, postalCode):
        self.fill(self.FIRST_NAME, firstName)
        self.fill(self.LAST_NAME, lastName)
        logger.info(f"postalCode: {postalCode}")
        allure.attach(f"Pet id received from API: {postalCode}",
                  name="Pet Id from API",
                  attachment_type=allure.attachment_type.TEXT)
        self.fill(self.POSTAL_CODE, f"{postalCode}")

    def clickContinueButton(self):
        self.click(self.CONTINUE)

    def is_finish_button_visible(self):
        return self.page.locator(self.FINISH).is_visible()
    
    def verify_item_text(self, expected_text):
        actual_text = self.page.locator(self.INVENTORY_ITEM_NAME).inner_text()
    
        allure.attach(f"Expected: {expected_text}\nActual: {actual_text}",
                  name="Verify Item Text",
                  attachment_type=allure.attachment_type.TEXT)
    
        return actual_text.strip() == expected_text.strip()