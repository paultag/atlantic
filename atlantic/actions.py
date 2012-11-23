from atlantic.utils import load_config, api_call
import datetime as dt
import json


def ping():
    obj = load_config()
    return api_call(obj, '/ping', {
        'node': obj['node_name']
    })


def finish(job_id):
    obj = load_config()
    return api_call(obj, '/finish', {
        'node': obj['node_name'],
        'job': job_id
    })


def result(report):
    obj = load_config()
    return api_call(obj, '/result', {
        'node': obj['node_name'],
        'data': json.dumps(report)
    })


def aquire():
    obj = load_config()
    return api_call(obj, '/aquire', {
        'node': obj['node_name']
    })


def echo(data):
    obj = load_config()
    return api_call(obj, '/echo', {
        'node': obj['node_name'],
        'time': dt.datetime.now()
    })


def package(package_id):
    obj = load_config()
    return api_call(
        obj, "/package/%s" % (package_id),
        {},
        do_sign=False
    )
