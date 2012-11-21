from atlantic.utils import load_config, api_call


def ping():
    obj = load_config()
    print api_call(obj, '/ping', {
        'data': {
            'foo': 'bar'
        }
    })


def echo(data):
    obj = load_config()
    return api_call(obj, '/echo', {
        'data': data
    })
