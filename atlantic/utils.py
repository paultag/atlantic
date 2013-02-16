import os
import json
import shutil
import urllib
import urllib2
import hashlib
import tempfile
from subprocess import call
from contextlib import contextmanager


def load_config():
    return json.load(open(os.path.expanduser("~/.atlanticrc"), 'r'))


def post(url, data):
    try:
        return urllib2.urlopen(url, urllib.urlencode(data))
    except urllib2.HTTPError as e:
        print url, data
        print e.read()
        raise


def api_call(url, data, do_sign=True):
    obj = load_config()
    data['name'] = obj['node_name']
    if do_sign:
        tok = token()['token']
        signature = sign(tok, obj['private_key'])
        data['signature'] = signature
    ret = json.load(post("%s%s" % (obj['api_base'], url), data))
    return ret


def sign(string, obj):
    s = "%s-%s" % (obj, string)
    return hashlib.sha256(s).hexdigest()


def token():
    obj = load_config()
    return api_call('/token', {
        'name': obj['node_name'],
    }, do_sign=False)


def run(cmd):
    call(cmd)


def rmdir(path):
    return shutil.rmtree(path)


@contextmanager
def tmpdir():
    path = tempfile.mkdtemp()
    pop_path = os.path.abspath(os.getcwd())
    try:
        os.chdir(path)
        yield path
    finally:
        os.chdir(pop_path)
    rmdir(path)
