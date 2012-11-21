from atlantic.utils import load_config, api_call
import datetime as dt


def ping():
    obj = load_config()
    return api_call(obj, '/ping', {
        'node': obj['node_name']
    })


def echo(data):
    obj = load_config()
    return api_call(obj, '/echo', {
        'node': obj['node_name'],
        'time': dt.datetime.now()
    })
