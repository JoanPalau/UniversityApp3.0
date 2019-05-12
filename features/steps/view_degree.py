from behave import *

use_step_matcher("parse")


@when('I view the details for degree "{degree_title}"')
def step_impl(context, degree_title):
    from univoting.models.degree import Degree
    degree = Degree.objects.get(title=degree_title)
    context.browser.visit(context.get_url(degree))
