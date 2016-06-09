#!/usr/bin/python
__author__ = 'Mayank'

from behave import given, when, then
from hamcrest import assert_that, equal_to
from Blender_ import Blender


@given('I put "{this}" in a blender')
def some_thing(context, this):
    context.blender = Blender()
    context.blender.insert(this)


@when('I switch the blender on')
def is_blended(context):
    context.blender.switch_on()


@then('It should transform into "{that}"')
def result_is(context, that):
    assert_that(context.blender.other_thing, equal_to(that))
