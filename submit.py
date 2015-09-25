# coding=utf-8
"""submit.feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('submit.feature', 'Displaying error in username in a form')
def test_displaying_error_in_username_in_a_form():
    """Displaying error in username in a form."""


@given('I am in a user form')
def i_am_in_a_user_form():
    """I am in a user form."""


@when('I click the Submit button')
def i_click_the_submit_button():
    """I click the Submit button."""


@when('I do not enter value in the text field')
def i_do_not_enter_value_in_the_text_field():
    """I do not enter value in the text field."""


@then('I get alert box stating username is not entered')
def i_get_alert_box_stating_username_is_not_entered():
    """I get alert box stating username is not entered."""

