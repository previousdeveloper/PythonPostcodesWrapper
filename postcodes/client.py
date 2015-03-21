__author__ = 'gokhan'
import requests


class PostCode(object):
    def getLookupPostCode(self, postcode):
        self.postcode = postcode
        data = requests.get("http://api.postcodes.io/postcodes/" + postcode).text
        return data


    def getLookupPostcodes(self, payload):
        self.payload = payload
        data = requests.post("http://api.postcodes.io/postcodes", payload).text
        return data


    def getLocationBasedPostcodes(self, lon, lang):
        self.long = lon
        self.lang = lang

        data = requests.get("http://api.postcodes.io/postcodes?lon=" + lon + "&lat=" + lang).text
        return data


    def getBulkReverseGecoding(self, payload):
        self.payload = payload
        data = requests.post("http://api.postcodes.io/postcodes", payload).text
        return data


    def getRandomPostCodes(self):
        pass
        data = requests.get("http://api.postcodes.io/random/postcodes").text
        return data

    def validatePostCode(self, postcode):
        self.postcode = postcode
        data = requests.get("http://api.postcodes.io/postcodes/" + postcode + "/validate").text
        return data

    def getNearestPostCode(self, postcode):
        self.postcode = postcode
        data = requests.get("http://api.postcodes.io/postcodes/" + postcode + "/nearest").text
        return data

