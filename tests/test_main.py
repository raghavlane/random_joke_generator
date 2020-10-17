"""Contains a test suite for basic tests."""

import unittest
from random_joke_generator.__main__ import getRandomChuckNorrisJoke, getApiCall, getRandomFirstLastName


class MainTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_name_none(self):
        first,last = getRandomFirstLastName()
        self.assertNotEqual(first, None)
        self.assertNotEqual(last, None)

    def test_joke_none(self):
        joke = getRandomChuckNorrisJoke()
        self.assertNotEqual(joke, None)

    def test_joke_input_none(self):
        joke = getRandomChuckNorrisJoke(None,None)
        self.assertNotEqual(joke, None)

    def test_joke_contains_name(self):
        first = 'billy'
        last = 'sparks'
        joke = getRandomChuckNorrisJoke(first,last)
        self.assertTrue((first in joke) or (last in joke))
        
    def test_joke_contains_name_with_number(self):
        first = 'billy123'
        last = 'sparks456'
        joke = getRandomChuckNorrisJoke(first,last)
        self.assertTrue((first in joke) or (last in joke))

    def test_joke_contains_name_with_onlynumber(self):
        first = 123654
        last = 456321
        joke = getRandomChuckNorrisJoke(first,last)
        self.assertTrue((str(first) in joke) or (str(last) in joke))

if __name__ == '__main__':
    unittest.main()
