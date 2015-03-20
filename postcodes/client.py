__author__ = 'gokhan'
import requests


class PostCode(object):
    def getRandomPostCodes(url):
        data = requests.get(url).text
        return data


    print  getRandomPostCodes("http://api.postcodes.io/random/postcodes")