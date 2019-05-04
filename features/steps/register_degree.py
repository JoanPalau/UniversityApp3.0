from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@when('I register a degree at University "{university_name}"')
def step_impl(context, university_name):
    from univoting.models import University
    university = University.objects.get(name=university_name)
    for row in context.table:
        context.browse.visit(context.get_url('degree_create', university.pk))
        if context.browse.url == context.get_url('degree_create', university.pk):
            form = context.browse.find_by_tag('form').first
            for heading in row.headings:
                context.browse.fill(heading, row[heading])

            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for degree at University "{university_name}" by "{username}"')
def step_impl(context, university_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from univoting.models import University
    q_list.append(Q('university', University.objects.get(name=university_name)))
    from univoting.models import Degree
    degree = Degree.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(degree)


@step("There are 1 degree")
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('degree_edit', degree.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
