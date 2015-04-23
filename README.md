# Postcodes.io
[![Build Status](https://travis-ci.org/previousdeveloper/PythonPostcodesWrapper.svg)](https://travis-ci.org/previousdeveloper/PythonPostcodesWrapper)

A simple wrapper around [postcodes.io](http://postcodes.io/)


## Installation
------------

To install Postcode.io, simply:

```python
$ pip install postcode.io
```
    
## Usage

```python
from lib import PostCodeClient
```

Create new instance of the Postcodes

```python
client = PostCodeClient()
```

Lookup a postcode example
```python
postcode = client.getLookupPostCode('OX49 5NU')
```

Lookup a postcode example
```python
postcode = client.getBulkReverseGecoding('{
            "geolocations": [{
                                 "longitude": 0.629834723775309,
                                 "latitude": 0.629834723775309
                             }, {
                                 "longitude": -2.49690382054704,
                                 "latitude": -2.49690382054704,
                                 "radius": 1000,
                                 "limit": 5
                             }]
        }')
```


For more details see [the documentation on postcodes.io](http://postcodes.io/docs)
## Contributing

I am not expert in pyhton if you want to contribute please pull request :)



1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
