from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given('Exists University registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from univoting.models.university import University
    for row in context.table:
        university = University(user=user)
        for heading in row.headings:
            setattr(university, heading, row[heading])
        university.save()


@when('I register a University')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('university_create'))
        if context.browser.url == context.get_url('university_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@Then('There are {count:n} universities')
def step_impl(context, count):
    from univoting.models.university import University
    assert count == University.objects.count()


@then('I\'m viewing the details page for University by {username}')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute]))
              for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from univoting.models.university import University
    university = University.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(university)


@when('I edit the University with name "{name}"')
def step_impl(context, name):
    from univoting.models import University
    university = University.objects.get(name=name)
    context.browser.visit(context.get_url('university_edit', university.pk))
    if context.browser.url == context.get_url('university_edit', university.pk) \
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()


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
