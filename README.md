# PostcodesIo

A simple wrapper around [postcodes.io](http://postcodes.io/)


## Installation
------------

To install Postcode.io, simply:

    $ pip install postcode.io
    
    
## Usage

    Require the python

```python
from lib import PostCodeClient
```

Create new instance of the Postcodes

```python
client = PostCodeClient()
```

Lookup a postcode example
```python
postcode = client.lookup('OX49 5NU')
```

For more details see [the documentation on postcodes.io](http://postcodes.io/docs)
## Contributing


1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
