__author__ = 'gokhan'
import requests


class PostCode(object):
    def getLookupPostCode(self, postcode):
        data = requests.get("http://api.postcodes.io/postcodes/" + postcode).text
        return data


    def getLookupPostcodes(payload):
        data = requests.post("http://api.postcodes.io/postcodes", payload).text
        return data


    def getNearestPostcodes(lon, lang):
        data = requests.get("http://api.postcodes.io/postcodes?lon=" + lon + "&lat=" + lang).text
        return data


    def getBulkReverseGecoding(payload):
        data = requests.post("http://api.postcodes.io/postcodes", payload).text
        return data


    @staticmethod
    def getRandomPostCodes():
        pass
        data = requests.get("http://api.postcodes.io/random/postcodes").text
        return data


print PostCode.getRandomPostCodes()