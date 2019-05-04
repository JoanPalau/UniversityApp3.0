from behave import *

use_step_matcher("parse")


@when('I list Universities')
def step_impl(context):
    context.browser.visit(context.get_url('universities'))


@then('I\'m viewing a list containing')
def step_impl(context):
    universities_links = context.browser.find_by_css('div#card-body h5')
    for i, row in enumerate(context.table):
        assert row['name'] == universities_links[i].text


@step('The list contains {count:n} universities')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#card-body h5'))
