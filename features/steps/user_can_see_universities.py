from behave import *


use_step_matcher("parse")


@when('I enter "/universities"')
def step_imp(context):
    context.browser.visit(context.get_url('univoting:link a univirsities'))


@given('There is no university registered')
def step_impl(context):
    from univoting.models.university import University
    assert 0 == University.objects.count()


@given('There are {count:n} universities registered')
def step_impl(context, count):
    raise NotImplementedError


@then('The list contains {count:n} University')
def step_impl(context, count):
    from univoting.models.university import University
    assert count == University.objects.count()


@then("I'm viewing a list of Universities containing")
def step_impl(context):
    raise NotImplementedError


@step("There are {count:n} universities registered:")
def step_impl(context, count):
    from univoting.models.university import University
    assert 0 == University.objects.count()


@then('I should see "Sorry, No universities registered yet."')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError


@given('their location is also registered:')
def step_impl(context):
    raise NotImplementedError


@step("There are 0 University")
def step_impl(context):
    raise NotImplementedError
