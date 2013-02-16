from atlantic.utils import api_call
import datetime as dt
import json


def ping():
    return api_call('/ping', {})
