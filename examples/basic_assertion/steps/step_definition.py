from behave import given, when, then


@given(u'The user is present')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: Given The user is present')


@when(u'The user will add 3 + 2')
def step_impl(context):
    pass
    # raise NotImplementedError(u'STEP: When The user will add 2 + 2')

@then(u'The result should be 4')
def step_impl(context):
    assert 3+2 == 4, "3+3 is not 4"
    # raise NotImplementedError(u'STEP: Then The result should be 4')