import os
import json
import urllib
import urllib2
import hashlib
from subprocess import call


def load_config():
    return json.load(open(os.path.expanduser("~/.atlanticrc"), 'r'))


def post(url, data):
    print url
    return urllib2.urlopen(url, urllib.urlencode(data))


def api_call(obj, url, data, do_sign=True):
    if do_sign:
        tok = token()['token']
        signature = sign(tok, obj)
        data['signature'] = signature
    return json.load(post("%s%s" % (obj['api_base'], url), data))


def sign(string, obj):
    s = "%s-%s" % (obj['private_key'], string)
    return hashlib.sha256(s).hexdigest()


def token(obj=None):
    if obj is None:
        obj = load_config()

    return api_call(obj, '/token', {
        'node': obj['node_name'],
    }, do_sign=False)


def run(cmd):
    call(cmd)
