from behave import given, when, then
from page.login_page import LoginPage
import time
from utility.config import SAUCEDO_URL

@given('the user is on the SauceDemo login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate_to(SAUCEDO_URL)

@when('the user enters valid credentials')
def step_impl(context):
    context.login_page.enter_username("standard_user")
    context.login_page.enter_password("secret_sauce")

@when('the user enters invalid credentials')
def step_impl(context):
    context.login_page.enter_username("wrong_user")
    context.login_page.enter_password("wrong_pass")

@when('clicks the login button')
def step_impl(context):
    context.login_page.click_login_button()

@then('the user should see the products page')
def step_impl(context):
    time.sleep(2)
    assert "inventory" in context.driver.current_url

@then('an error message should be shown')
def step_impl(context):
    time.sleep(1)
    error_message = context.login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"
