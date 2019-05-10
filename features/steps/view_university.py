from behave import *

use_step_matcher("parse")


@when('I view the details for university "{university_name}"')
def step_impl(context, university_name):
    from univoting.models import University
    university = University.objects.get(name=university_name)
    context.browser.visit(context.get_url(university))


@Then('I\'m viewing a University degrees list containing')
def step_impl(context):
    degrees_links = context.browser.find_by_css('div#degrees-group ul li a')
    for i, row in enumerate(context.table):
        assert row['name'] == degrees_links[i].text


@Then('The list contains {count:n} degrees')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#degrees-group ul li a'))


@Then('There is no "{button}" link available')
def step_impl(context, button):
    assert not context.browser.find_by_value(button)
