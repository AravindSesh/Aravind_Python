# coding=utf-8
"""submit.feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


import unittest
import pytest
from selenium import webdriver



class Sample:
	browser=webdriver.Firefox()
	browser.get("file:///C:/Users/Aravind/Documents/GitHub/Aravind_Python/test_page.html")
	@scenario('submit.feature', 'Displaying error in username in a form')
	def test_displaying_error_in_username_in_a_form():
		"""Displaying error in username in a form."""
		pass
	
	@given('I am in a user form')
	def i_am_in_a_user_form(self):
		"""I am in a user form."""
		assert self.browser.title in "hello"
		if False:
			sys.exit(1)
				
	@when('I click the Submit button')
	def i_click_the_submit_button():
		"""I click the Submit button."""

	@when('I do not enter value in the text field')
	def i_do_not_enter_value_in_the_text_field():
		"""I do not enter value in the text field."""

	@then('I get alert box stating username is not entered')
	def i_get_alert_box_stating_username_is_not_entered():
		"""I get alert box stating username is not entered."""
	
if __name__ == '__main__':
	unittest.main()
s=Sample()
s.i_am_in_a_user_form()