from django.test import TestCase
from parameterized import parameterized
from univoting.models.university import University
from univoting.models.location import Location
from django.core.exceptions import ValidationError
from django.core import management


class TestUniversity(TestCase):


    loc = Location()

    def setup(self):
        self.loc.save()


    def tearDown(self):
        management.call_command('flush', verbosity=0, interactive=False) # borra bbdd

#
########################################################################################################################

    @parameterized.expand([[None], [123], [.265], [''], [' '], ['  '], [{}], [[]]])
    def test_university_name(self, university_name):
        with self.assertRaises(ValueError):
            University.create(name=university_name, telephone="+34 123456789", location=self.loc)

    @parameterized.expand([[None], [0], [-1], [+34123456789], [{}], [[]]])
    def test_university_telephone(self, university_telephone):
        with self.assertRaises(ValueError):
            University.create(name="Example Name", telephone=university_telephone, location=self.loc)

    """
    @parameterized.expand([["+2201234"], ["-2201234"], ["+34123456789"], [""], [" "]])
    def test_university_wrong_telephone(self, university_telephone):
        with self.assertRaises(ValidationError):
            University.create(name="Example Name", telephone=university_telephone)

    """
########################################################################################################################
#
    @parameterized.expand([["Universitat de Lleida", "+34 973003588"],
                           ["Universitat Politècnica de Catalunya", "+34 934016200"],
                           ["Stanford University", "+1 6507232300"],
                           ["National University of Singapore", "+65 65166666"],
                           ["Universitat Politècnica de València", "+34 963877000"]])
    def test_university_values(self, name, telephone):
        university = University.create(name=name, telephone=telephone, location=self.loc)
        self.assertEqual(university.name, name)
        self.assertEqual(university.telephone, telephone)
        self.assertEqual(university.location, self.loc)
        self.assertEqual("{} [{}]".format(name, telephone), university.__str__())
