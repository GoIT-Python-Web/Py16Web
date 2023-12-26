import unittest

from src.my_class.main import Cat, CatDog, Dog, DogCat, Animal


class TestClass(unittest.TestCase):

    def test_dog(self):
        self.assertEqual(Dog.__base__, Animal, msg='Class Dog not inherit class Animal')

    def test_cat_dog(self):
        assert Dog in CatDog.__bases__, 'Class Dog must be parent for class CatDog'  # raise AssertionError('Class Dog must be parent for class CatDog')
        assert 'info' in dir(CatDog), 'Not implemented method info'
