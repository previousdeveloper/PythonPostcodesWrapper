__author__ = 'gokhan'

from postcodes import PostCode
import unittest


class PostClientTest(unittest.TestCase):
    def setUp(self):
        self.client = PostCode()

    def getLookupPostCodeTest(self):
        response = self.client.getNearestPostCode("")
        self.assertTrue(response)


if __name__ == 'main':
    unittest.main()