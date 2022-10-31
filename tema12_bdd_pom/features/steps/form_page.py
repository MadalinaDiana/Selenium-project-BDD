from behave import *


@Given('I am on the Jules App-sign-in')
def step_impl(context):
    context.form_page.go_home()


@When('I input correct email')
def step_impl(context):
    context.form_page.input_email('mada@yahoo.com')


@When('I write a password')
def step_impl(context):
    context.form_page.write_pass()


@When('I clear the password')
def step_impl(context):
    context.form_page.delete_password()


@Then('Message error is displayed')
def step_impl(context):
    assert context.form_page.check_error_message_after_delete_password() == "Please enter your password!"


@Then('Log in button id disabled')
def step_impl(context):
    try:
        login = context.browser.check_btn_login_disabled()
        login.click()
        print('clickable')
    except:
        print('not clickable')
