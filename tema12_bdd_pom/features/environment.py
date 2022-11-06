from browser import Browser
from pages.form_page import FormPage
from pages.verify_url import VerifyUrl
from pages.complete_signup import CompleteSign
from pages.forgot_password import FormForgot


def before_all(context):
    context.browser = Browser()
    context.form_page = FormPage(context.browser.driver)
    context.verify_url = VerifyUrl(context.browser.driver)
    context.complete_signup = CompleteSign(context.browser.driver)
    context.forgot_password = FormForgot(context.browser.driver)


def after_all(context):
    context.browser.close()
