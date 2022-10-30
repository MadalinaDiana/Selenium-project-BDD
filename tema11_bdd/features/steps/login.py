import time
from behave import *


@given('I am on the login page')
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(1)


@when('Enter the correct username')
def step_impl(context):
    context.browser.set_username_correct('tomsmith')


@when('Enter the correct password')
def step_impl(context):
    context.browser.set_password_correct('SuperSecretPassword!')


@when('I click Login button')
def step_impl(context):
    context.browser.click_login()
    time.sleep(2)


@then('I can see a confirmation message on the page')
def step_impl(context):
    expected_message = 'You logged into a secure area!'
    print(context.browser.get_page_menu())
    assert (expected_message in context.browser.get_page_menu())

