from django.test import TestCase
from parameterized import parameterized
from univoting.models.university import University
from univoting.models.location import Location
from django.core import management


class TestUniversity(TestCase):

    loc = Location()

    def setup(self):
        self.loc.save()

    def tearDown(self):
        management.call_command('flush', verbosity=0, interactive=False)  # borra bbdd

#
########################################################################################################################

    @parameterized.expand([[None], [123], [.265], [''], [' '], ['  '], [{}], [[]]])
    def test_university_name(self, university_name):
        with self.assertRaises(ValueError):
            University.objects.create(name=university_name, telephone="+34 123456789", location=self.loc)

    @parameterized.expand([[None], [0], [-1], [+34123456789], [{}], [[]]])
    def test_university_telephone(self, university_telephone):
        with self.assertRaises(ValueError):
            University.objects.create(name="Example Name", telephone=university_telephone, location=self.loc)

########################################################################################################################
#
    @parameterized.expand([
        ["Universitat de Lleida", "This is the Universitat de Lleida description", "+34 973003588"],
        ["Universitat Politècnica de Catalunya", "This is the Universitat Politècnica de Catalunya description", "+34 934016200"],
        ["Stanford University", "This is the Stanford University description", "+1 6507232300"],
        ["National University of Singapore", "This is the National University of Singapore description", "+65 65166666"],
        ["Universitat Politècnica de València", "This is the Universitat Politècnica de València description", "+34 963877000"]])
    def test_university_values(self, name, description, telephone):
        # uni = University.objects.create(name=name, telephone=telephone, location=self.loc)
        University.objects.create(name=name, description=description, telephone=telephone)
        university = University.objects.get(name=name)
        self.assertEqual(university.name, name)
        self.assertEqual(university.description, description)
        self.assertEqual(university.telephone, telephone)
        # self.assertEqual(university.location, self.loc)
        self.assertEqual("{} [{}]".format(name, telephone), university.__str__())
