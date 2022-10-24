import time
from behave import *


@when('I can see a confirmation message on the page')
def step_impl(context):
    expected_message = 'You logged into a secure area!'
    print(context.browser.get_page_menu())
    assert (expected_message in context.browser.get_page_menu())


@when('I press logout button')
def step_impl(context):
    context.browser.click_logout_button()


@then('I press x on message')
def step_impl(context):
    context.browser.click_x_message()


@then('I am redirected to the "{expected_page}" page')
def step_impl(context, expected_page):
    expected_url = "https://the-internet.herokuapp.com/" + expected_page
    assert context.browser.get_current_url() == expected_url
