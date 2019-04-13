import os
from django.core.management.base import BaseCommand
from univoting.models.university import University
from univoting.models.degree import Degree


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


def add_universities(filename, head_description, description):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_university(params, head_description, description)


def add_university(params, head_description, description):
    new_description = head_description.format(params[0])
    new_description = new_description + ' ' + description
    uni = University(name=params[0], description=new_description, picture=params[1].rstrip())
    uni.save()


def add_degrees(filename, head_description, description):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            universities = University.objects.all()
            for uni in universities:
                add_degree(params, head_description, description, uni)


def add_degree(params, head_description, description, uni):
    new_description = head_description.format(params[0])
    new_description = new_description + ' ' + description
    degree = Degree(title=params[0], ects=params[1], description=new_description, university=uni)
    degree.save()
