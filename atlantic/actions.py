from atlantic.utils import api_call
import datetime as dt
import json


def ping():
    return api_call('/ping', {})


def upload_log(package_id, firefile, when):
    return api_call('/log', {
        "package": package_id,
        "when": when,
        "firehose": open(firefile, 'r').read()
    })
