from browser import Browser
from pages.form_page import FormPage
from pages.verify_url import SignUpPage
from pages.complete_signup import CompleteSign


def before_all(context):
    context.browser = Browser()
    context.form_page = FormPage(context.browser.driver)
    context.verify_url = SignUpPage(context.browser.driver)
    context.complete_signup = CompleteSign(context.browser.driver)


def after_all(context):
    context.browser.close()
