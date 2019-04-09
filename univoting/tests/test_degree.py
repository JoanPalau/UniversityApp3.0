from django.test import TestCase
from parameterized import parameterized
from univoting.models.degree import Degree
from univoting.models.university import University
from django.core import management


class TestDegree(TestCase):

    uni = University()

    def setup(self):
        self.uni.save()

    def tearDown(self):
        management.call_command('flush', verbosity=0, interactive=False)

#
########################################################################################################################
    '''
        Tests for validators:
        Validators can not be tested with sqlite db
    '''
    '''
    @parameterized.expand([[None], [123], [.265], [''], [' '], ['  '], [{}], [[]]])
    def test_degree_name(self, degree_title):
        degree = Degree()
        with self.assertRaises(ValueError):
            degree.title = degree_title

    @parameterized.expand([[None], [0], [-1], [601], [""], [" "], [{}], [[]]])
    def test_degree_ects(self, ects):
        degree = Degree()
        with self.assertRaises(ValueError):
            degree.ects = ects
    '''

########################################################################################################################
#

#
########################################################################################################################

    @parameterized.expand([[None], [123], [.265], [''], [' '], ['  '], [{}], [[]]])
    def test_degree_name(self, degree_name):
        with self.assertRaises(ValueError):
            Degree.create(title=degree_name, ects=240, description="This is a description.", university=self.uni)

    @parameterized.expand([[None], [0], [-1], [601], [""], [" "], [{}], [[]]])
    def test_degree_ects(self, ects):
        with self.assertRaises(ValueError):
            Degree.create(title='Exemple Title', ects=ects, description="This is a description.", university=self.uni)

    @parameterized.expand([[None], [123], [.265], [{}], [[]]])
    def test_degree_description(self, description):
        with self.assertRaises(ValueError):
            Degree.create(title='Exemple Title', ects=240, description=description, university=self.uni)

    @parameterized.expand([[None], [123], [.265], [""], [" "], [{}], [[]]])
    def test_degree_university(self, university):
        with self.assertRaises(ValueError):
            Degree.create(title='Exemple Title', ects=240, description="This is a description.", university=university)

########################################################################################################################
#
    @parameterized.expand([["Enginyeria Informatica", 240, "Aquest es el grau de enginyeria informatica."],
                           ["Enginyeria Electronica", 240, "Aquest es el grau de enginyeria electronica."],
                           ["Medicina", 300, "Aquest es el grau de medicina."],
                           ["Dret", 300, "Aquest es el grau de dret."]])
    def test_degree_values(self, title, ects, description):
        degree = Degree.create(title=title, ects=ects, description=description, university=self.uni)
        self.assertEqual(degree.title, title)
        self.assertEqual(degree.ects, ects)
        self.assertEqual(degree.description, description)
        self.assertEqual(degree.university, self.uni)
        self.assertEqual("{} [{}] {}".format(title, ects, description), degree.__str__())
