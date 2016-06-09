#!/usr/bin/python
__author__ = 'Mayank'

from behave import given, when, then
from hamcrest import assert_that, equal_to
from Blender_ import Blender


@given('I put "{thing}" in a blender')
def some_thing(context, thing):
    context.blender = Blender()
    context.blender.insert(thing)


@when('I switch the blender on')
def is_blended(context):
    context.blender.switch_on()


@then('It should transform into "{other thing}"')
def result_is(context, other_thing):
    assert_that(context.blender.other_thing, equal_to(other_thing))
