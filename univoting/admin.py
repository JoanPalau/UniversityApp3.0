from django.contrib import admin
from univoting.models.degree import Degree, University
from univoting.models.course import Course
from univoting.models.subject import Subject
from univoting.models.subject_comment import SubjectComment
from univoting.models.subject_review import SubjectReview
from univoting.models.location import Location

# Register your models here.
admin.site.register(University)
admin.site.register(Degree)
admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(SubjectComment)
admin.site.register(SubjectReview)
admin.site.register(Location)
