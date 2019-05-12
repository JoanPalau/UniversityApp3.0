from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@when('I register a subject at "{university_name}" in "{degree_title}"')
def step_impl(context, university_name, degree_title):
    from univoting.models import University
    university = University.objects.get(name=university_name)
    from univoting.models import Degree
    degree = Degree.objects.get(name=degree_title, university=university)
    for row in context.table:
        context.browser.visit(context.get_url('subject_create', degree.pk))
        if context.browser.url == context.get_url('subject_create', degree.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value().first.click()


@then('I\'m viewing the details page for the subject '
      'at University "{university_name}" '
      'in "{degree_title}" by "{user_name}"')
def step_impl(context, university_name, degree_title, user_name):
    '''
    q_list = [Q((attribute, context.table.row[0][attribute]))
              for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=user_name))))
    from univoting.models import University
    university = University.objects.get(name=university_name)
    from univoting.models import Degree
    q_list.append(Q(('degree', Degree.objects.get(title=degree_title, university=university))))
    from univoting.models import Subject
    subject = Subject.objects.filter(reduce(operator.and_, q_list)).get()
    '''
    '''
        THIS DOESN'T WORK BECAUSE THE IMPLEMENTATION
        ############################################
    '''
    from univoting.models.subject import Subject
    subject = Subject.objects.get(name=context.table.rows[0]['title']).get()
    from univoting.models.course import Course
    course = Course.objects.get(subject_id=subject)
    assert context.browser.url == context.get_url(course.degree_id + 'subject/' + subject.pk)


@step("There are {count:n} subject")
def step_impl(context, count):
    from univoting.models import Subject
    assert count == Subject.objects.count()
