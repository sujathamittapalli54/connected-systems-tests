from behave import given, when, then
from services.pet_service import PetService
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL, USERNAME, PASSWORD
from faker import Faker

import logging

logger = logging.getLogger(__name__)

@given("I create a pet via API")
def step_create_pet(context):
    service = PetService()
    context.pet = service.create_pet()
    logger.info(f"Pet created: {context.pet}")
    logger.info(f"Pet created id: {context.pet['id']}")
    print(f"Pet ID: {context.pet['id']}")

@when("I login to the application")
def step_login_ui(context):
    login_page = LoginPage(context.page)
    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

@then("I should see the inventory page")
def step_inventory_page(context):
    assert "inventory" in context.page.url

@then("the pet ID should not be null")
def step_pet_id_not_null(context):
    assert context.pet["id"] is not None

@when("click on Shopping cart link after adding an item")
def step_click_on_shopping_cart_link_after_adding_item(context):
    product_page = ProductPage(context.page)
    product_page.clickShoppingCart()

@then("I should see cart page")
def step_cart_page(context):
    assert "cart" in context.page.url

@when("I click on checkout button")
def step_click_on_checkout_button(context):
    product_page = ProductPage(context.page)
    product_page.clickCheckoutButton()

@then("I should see checkout page")
def step_checkout_page(context):
    assert "checkout" in context.page.url

@when("I enter checkout information")
def step_enter_checkout_information(context):
    checkout_page = CheckoutPage(context.page)
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    checkout_page.enterCheckoutInformation(first_name,last_name,context.pet['id'])

@when("I click on continue")
def step_click_on_continue(context):
    checkout_page = CheckoutPage(context.page)
    checkout_page.clickContinueButton()

@then("Make sure finish button is visible")
def step_make_sure_finish_button_visible(context):
    checkout_page = CheckoutPage(context.page)
    assert checkout_page.is_finish_button_visible()

@then("Make sure the same item which is added in listing page exist in checkout")
def step_make_sure_same_item_added_exist_in_checkout(context):
    checkout_page = CheckoutPage(context.page)
    assert checkout_page.verify_item_text('Sauce Labs Backpack')



    


    


