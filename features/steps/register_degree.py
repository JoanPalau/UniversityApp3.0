from functools import reduce
import operator
from django.db.models import Q
from behave import *

use_step_matcher("parse")


@step('Exists degree registered by "{username}" in "{university_name}"')
def step_impl(context, username, university_name):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from univoting.models import University
    university = University.objects.get(name=university_name)
    from univoting.models import Degree
    for row in context.table:
        degree = Degree(university=university, user=user)
        for heading in row.headings:
            setattr(degree, heading, row[heading])
        degree.save()


@when('I register a degree at University "{university_name}"')
def step_impl(context, university_name):
    from univoting.models import University
    university = University.objects.get(name=university_name)
    for row in context.table:
        context.browser.visit(context.get_url(university.get_absolute_url() + 'new/'))
        if context.browser.url == context.get_url(university.get_absolute_url() + 'new/'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])

            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for degree at University "{university_name}" by "{username}"')
def step_impl(context, university_name, username):
    # q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    # q_list.append(Q(('created_by', User.objects.get(username=username))))
    user = User.objects.get(username=username)
    from univoting.models import University
    # q_list.append(Q('university', University.objects.get(name=university_name)))
    university = University.objects.get(name=university_name)
    from univoting.models import Degree
    # degree = Degree.objects.filter(reduce(operator.and_, q_list)).get()
    degree = Degree.objects.filter(created_by=user, university=university,
                                   title=context.table.rows[0]['title']).get()
    assert context.browser.url == context.get_url(degree)


@step("There are {count:n} degree")
def step_impl(context, count):
    from univoting.models import Degree
    assert count == Degree.objects.count()


'''
@when('I edit the current degree')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('degree_edit', degree.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
'''
