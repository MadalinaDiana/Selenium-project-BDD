import time
from behave import *


@given('I am on the Home Page')
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")
    time.sleep(1)


@when('I click on the Checkboxes')
def step_impl(context):
    context.browser.click_check_link()


@when('I am redirected to the "{expected_page}" page')
def step_impl(context, expected_page):
    expected_url = "https://the-internet.herokuapp.com/" + expected_page
    assert context.browser.get_current_url() == expected_url


@then('I click checkbox2')
def step_impl(context):
    context.browser.select_checkbox()


# al doilea scenariu
# @given('I am on the Home Page') acesta este deja implementat


@when('I click on the Dropdown')
def step_impl(context):
    context.browser.click_dropdown()
# @when('I am redirected to the "{expected_page}" page') - am deja acest when implementat

@then('I click option2')
def step_impl(context):
    context.browser.click_option_dropdown()


@when('I click on the Form Authentication')
def step_impl(context):
    context.browser.click_form_authentication()


# @when('I am redirected to the "{expected_page}" page') - am deja acest when implementat


@then('I click Login button')
def step_impl(context):
    context.browser.click_login()
