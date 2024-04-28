
from behave import given, when, then

# Note "And" statement need no step-definition can be used to concatenate given preconditions


@given('I have a new "{item}" in my cart')
def step_impl(context, item):
    print(f" the item is {item} was collected")
