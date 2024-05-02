
from behave import given, when, then
import logging as logger


@given(u'I create a new user')
def step_impl(context):
    print("I create a new user")
    # raise NotImplementedError(u'STEP: Given I create a new user')

@when(u'I type email')
def step_impl(context):
    print("I type email")
    # raise NotImplementedError(u'STEP: When I type email')


@when(u'I type password')
def step_impl(context):
    print("I type password")
    # raise NotImplementedError(u'STEP: When I type password')


@when(u'I click on \'Login\'')
def step_impl(context):
    print("click on \'Login\'")
    # raise NotImplementedError(u'STEP: When I click on \'Login\'')


@then(u'I should see teh text welcome')
def step_impl(context):
    print("I should see teh text welcome")
    # raise NotImplementedError(u'STEP: Then I should see teh text welcome')
