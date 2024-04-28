
from behave import given, when, then
import logging as logger

@given(f'I am at the login page')
def step_impl(context):
    print("I am at the login page")
    logger.info("")
    logger.info("GIVEN info 1")
    logger.info("GIVEN info 1")
    logger.debug("GIVEN debug")
    assert 1 == 2, "one is not the same than 2"
    #raise NotImplementedError(u'STEP: Given I am at the login page')

@when(u'I type valid email')
def step_impl(context):
    print("I type valid email')")
    #raise NotImplementedError(u'STEP: When I type valid email')

@when(u'I type invalid password')
def step_impl(context):
    print("I type invalid password")
    #raise NotImplementedError(u'STEP: When I type invalid password')

@then(u'I should not see the text welcome')
def step_impl(context):
    print("I should not see the text welcome")
    #raise NotImplementedError(u'STEP: Then I should not see the text welcome')

