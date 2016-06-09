#!/usr/bin/python
__author__ = 'Mayank'

from behave import given, when, then
from hamcrest import assert_that, equal_to
from Forbulator import Forbulator


@given('a sample text is loaded into the frobulator')
def step_impl(context):
    forbulator = getattr(context, "forbulator", None)
    if not forbulator:
        context.frobulator = Forbulator()
    context.frobulator.text = context.text  # context.text has step data


@when('frobulator is activated')
def step_impl(context):
    context.frobulator.activate()


@then('the text language is {lang}')
def step_impl(context, lang):
    assert_that(context.frobulator.evaluate_language(), equal_to(lang))
