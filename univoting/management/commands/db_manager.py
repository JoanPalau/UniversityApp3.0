import os
from django.core.management.base import BaseCommand
from univoting.models.university import University


class Command(BaseCommand):
    def handle(self, *args, **options):
        make_database()


def make_database():
    path = os.getcwd()
    with open(path + '/data/head_description.data', 'r') as head_descr:
        with open(path + '/data/description.data', 'r') as description:
            add_universities(path + '/data/university.data', head_descr.readline(), description.readline())


def add_universities(filename, head_description, description):
    with open(filename, 'r') as f:
        for line in f.readlines():
            params = line.split('|')
            add_university(params, head_description, description)


def add_university(params, head_description, description):
    new_description = head_description.format(params[0])
    new_description = new_description + description
    uni = University(name=params[0], description=new_description, picture=params[1])
    uni.save()
