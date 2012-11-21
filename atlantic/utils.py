import os
import json
import urllib
import urllib2


def load_config():
    return json.load(open(os.path.expanduser("~/.atlanticrc"), 'r'))


def post(url, data):
    return urllib2.urlopen(url, urllib.urlencode(data))


def api_call(obj, url, data):
    return json.load(post("%s%s" % (obj['api_base'], url), data))
