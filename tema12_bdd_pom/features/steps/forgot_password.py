from behave import *
import time

@given(u'I am on the Jules App-forgot-password')
def step_impl(context):
    context.browser.verify_url()
    time.sleep(2)

@when('I input email.')
def step_impl(context):
    context.forgot_password.input_email('madalinadiana728@yahoo.com')


@when(u'I click "SEND EMAIL" button.')
def step_impl(context):
    context.forgot_password.send_email_btn()
    time.sleep(2)


@then(u'I recive the the mail send message.')
def step_impl(context):
    assert context.forgot_password.send_message()
