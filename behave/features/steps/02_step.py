#!/usr/bin/python
__author__ = 'Mayank'

from behave import given, when, then

"""PyHamcrest is a framework for writing matcher objects, allowing you to declaratively define “match” rules."""
from hamcrest import assert_that, equal_to
from NinjaFight import NinjaFight

@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
    context.ninja_fight = NinjaFight(achievement_level) # Initialize Object, set obj.achievement_level

@when('attacked by a {opponent_role}')
def step_attacked_by_a(context, opponent_role):
    context.ninja_fight.opponent = opponent_role # set obj.opponent

@when('attacked by {opponent}')
def step_attacked_by(context, opponent):
    context.ninja_fight.opponent = opponent

@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
    assert_that(reaction, equal_to(context.ninja_fight.decision()))