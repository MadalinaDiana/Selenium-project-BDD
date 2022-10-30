from behave import *
import time

@when('I click personal value')
def step_impl(context):
    context.complete_signup.click_personal()


@when('I click continue button')
def step_impl(context):
    context.complete_signup.continue_button().click()
    time.sleep(3)

@when('I input correct first name')
def step_impl(context):
    context.complete_signup.input_first_name('Madalina')


@when('I input correct last name')
def step_impl(context):
    context.complete_signup.input_last_name('Laszlo')


@when('I input wrong email')
def step_impl(context):
    context.complete_signup.input_wrong_email()


@then('I verify error message')
def step_impl(context):
    assert context.complete_signup.verify_error() == "Please enter a valid email address."


@when('I clear email input')
def step_impl(context):
    context.complete_signup.clear_email()


@then('I verify that error is not displayed anymore')
def step_impl(context):
    try:
        message = context.browser.verify_error()
        message.is_displayed()
        print('message exist')
    except:
        print('message is not appear')
