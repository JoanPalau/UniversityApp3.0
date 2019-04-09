from django.test import TestCase
from parameterized import parameterized
from univoting.models.university import University
from django.core.exceptions import ValidationError
from django.core import management


class TestUniversity(TestCase):

    """
    uni = University()

    def setup(self):
        self.uni.save()
    """

    def tearDown(self):
        management.call_command('flush', verbosity=0, interactive=False) # borra bbdd

#
########################################################################################################################

    @parameterized.expand([[None], [123], [.265], [''], [' '], ['  '], [{}], [[]]])
    def test_university_name(self, university_name):
        with self.assertRaises(ValueError):
            University.create(name=university_name, telephone="+34 123456789")

    @parameterized.expand([[None], [0], [-1], [+34123456789], [{}], [[]]])
    def test_university_telephone(self, university_telephone):
        with self.assertRaises(ValueError):
            University.create(name="Example Name", telephone=university_telephone)

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
        university = University.create(name=name, telephone=telephone)
        self.assertEqual(university.name, name)
        self.assertEqual(university.telephone, telephone)
        self.assertEqual("{} [{}]".format(name, telephone), university.__str__())
