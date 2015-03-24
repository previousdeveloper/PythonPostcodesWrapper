__author__ = 'gokhan'
import unittest

from lib import PostCodeClient


class PostClientTest(unittest.TestCase):
    def setUp(self):
        self.client = PostCodeClient()

    def test_Nearest_Post_Code(self):
        self.assertIsNotNone(self.client.getNearestPostCode("OX49 5NU"))

    def test_Lookup_Post_codes(self):
        self.assertIsNotNone(self.client.getLookupPostCode("OX49 5NU"))

    def test_Bulk_Lookup_Post_codes(self):
        self.payload = {
            "lib": ["OX49 5NU", "M32 0JG", "NE30 1DP"]
        }
        self.assertIsNotNone(self.client.getLookupPostcodes(self.payload))

    def test_Location_Based_Postcodes(self):
        self.long = str(0.629834723775309)
        self.lang = str(0.629834723775309)
        self.assertIsNotNone(self.client.getLocationBasedPostcodes(self.long, self.lang))

    def test_BulkReverse_Gecoding(self):
        self.payloadgecoding = {
            "geolocations": [{
                                 "longitude": 0.629834723775309,
                                 "latitude": 0.629834723775309
                             }, {
                                 "longitude": -2.49690382054704,
                                 "latitude": -2.49690382054704,
                                 "radius": 1000,
                                 "limit": 5
                             }]
        }

        self.assertIsNotNone(self.client.getBulkReverseGecoding(self.payloadgecoding))

    def test_Random_PostCodes(self):
        self.assertIsNotNone(self.client.getRandomPostCodes())


    def test_validate_Post_Code(self):
        self.assertIsNotNone("OX49 5NU")


if __name__ == '__main__':
    unittest.main()