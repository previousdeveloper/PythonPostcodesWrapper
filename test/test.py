__author__ = 'gokhan'
import unittest
from postcodes import PostCode


class PostClientTest(unittest.TestCase):
    def setUp(self):
        self.client = PostCode()

    def test_Nearest_Post_Code(self):
        self.assertIsNotNone(self.client.getNearestPostCode("OX49 5NU"))

    def test_Lookup_Post_codes(self):
        self.assertEquals(self.client.getNearestPostCode("OX49 5NU"))


if __name__ == '__main__':
    unittest.main()