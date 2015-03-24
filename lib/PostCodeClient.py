__author__ = 'gokhan'
import requests

BASE_URL = "http://api.postcodes.io/postcodes/"


class PostCodeClient(object):
    def getLookupPostCode(self, postcode):
        self.postcode = postcode
        data = requests.get(BASE_URL + postcode).text
        return data


    def getLookupPostcodes(self, payload):
        self.payload = payload
        data = requests.post(BASE_URL, payload).text
        return data


    def getLocationBasedPostcodes(self, lon, lang):
        self.long = lon
        self.lang = lang

        data = requests.get("http://api.postcodes.io/postcodes?lon=" + lon + "&lat=" + lang).text
        return data


    def getBulkReverseGecoding(self, payload):
        self.payload = payload
        data = requests.post(BASE_URL, payload).text
        return data


    def getRandomPostCodes(self):
        pass
        data = requests.get("http://api.postcodes.io/random/postcodes").text
        return data

    def validatePostCode(self, postcode):
        self.postcode = postcode
        data = requests.get(BASE_URL + postcode + "/validate").text
        return data

    def getNearestPostCode(self, postcode):
        self.postcode = postcode
        data = requests.get(BASE_URL + postcode + "/nearest").text
        return data