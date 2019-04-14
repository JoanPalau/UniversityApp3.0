import os
import random
from django.core.management.base import BaseCommand
from univoting.models.university import University
from univoting.models.degree import Degree
from univoting.models.subject import Subject
from univoting.models.subject_review import SubjectReview
from univoting.models.course import Course


class Command(BaseCommand):
    def handle(self, *args, **options):
        make_database()


def make_database():
    path = os.getcwd()
    with open(path + '/data/head_description.data', 'r') as head_descr:
        with open(path + '/data/description.data', 'r') as description:
            hdescr = head_descr.readline()
            descr = description.readline()
            add_universities(path + '/data/university.data', hdescr, descr)
            add_degrees(path + '/data/degree.data', hdescr, descr)
            # add_subjects(path + '/data/subjects.data', hdescr, descr)


def add_universities(filename, head_description, description):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_university(params, head_description, description)


def add_university(params, head_description, description):
    new_description = get_description(head_description, description, params[0])
    uni = University(name=params[0], description=new_description, picture=params[1].rstrip())
    uni.save()


def add_degrees(filename, head_description, description):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            universities = University.objects.all()
            for uni in universities:
                if random.random() > 0.66:
                    add_degree(params, head_description, description, uni)


def add_degree(params, head_description, description, uni):
    new_description = get_description(head_description, description, params[0])
    degree = Degree(title=params[0], ects=params[1],
                    description=new_description, university=uni)
    degree.save()


def add_subjects(filename, head_description, description):
    degrees = Degree.objects.all()
    i_course = 0
    with open(filename, 'r') as f:
        for i_subject, line in enumerate(f.readlines()):
            params = line.split('|')
            if i_subject % 6 == 0:
                i_course += 1
            for degree in degrees:
                new_subject = add_subject(params, i_course, i_subject+1,
                                          head_description, description)
                add_new_course(degree, new_subject, i_course)


def add_subject(params, i_curse, i_subject, head_description, description):
    new_description = get_description(head_description, description, params[0])
    review = get_new_review()
    review.save()
    new_name = 'Subject-{}.{}'.format(i_curse, i_subject)
    subject = Subject(name=new_name, ects=params[0],
                      description=new_description, review=review)
    subject.save()
    return subject


def add_new_course(degree, subject, course):
    course = Course(degree_id=degree, subject_id=subject, course=course)
    course.save()


def get_new_review():
    mark = random.random()*10
    difficulty = random.random()*10
    work_score = random.random()*2
    work_volume = int(work_score + .5)
    review = SubjectReview(mark=mark, difficulty=difficulty,
                           work_score=work_score, workVolume=work_volume,
                           amount=1)
    return review


def get_description(head_description, description, name):
    return head_description.format(name) + description
