from atlantic.utils import load_config, api_call


def ping():
    obj = load_config()
    print api_call(obj, '/ping', {})
