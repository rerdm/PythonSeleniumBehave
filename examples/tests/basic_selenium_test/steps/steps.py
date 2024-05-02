import time

from build.lib.BDDGeneral.CommonSeleniumFunctions.SeleniumCommonFunctions import SeleniumCommonFunctions

from behave import given, when, then


@given(u'The user open the Website "{url}" with the "{browser}" browser')
def step_impl(context, url, browser):
    driver = SeleniumCommonFunctions(driver_name=browser, zoom=True)
    driver.open_website(url)
    context.driver = driver
    time.sleep(5)


@then(u'The page title of the Website-Title should be "{expected_text}"')
def step_impl(context, expected_text):
    element_text = context.driver.get_element_text_by_xpath()
    assert element_text == expected_text, \
        f" Website title = {element_text} expected {expected_text}"
