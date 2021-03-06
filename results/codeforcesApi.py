"""Functions to call the codeforces api."""
import hashlib
import json
import secrets
import time
import urllib.parse

import requests


__all__ = ['call']

CODEFORCES_API_URL = "https://codeforces.com/api/"


def _generate_api_sig(method, args, secret):
    rand = "%06d" % secrets.randbelow(999999)
    url_args = urllib.parse.urlencode(sorted(args.items()))
    return rand + hashlib.sha512(("%s/%s?%s#%s" % (rand, method, url_args, secret)).encode('utf-8')).hexdigest()


def call(method, lastSubmit, key=None, secret=None, **kwargs):
    """
    Call a Codeforces API method.

    Parameters
    ----------
    method: str
        Name of method to call, list of all methods can be found at
        https://codeforces.com/api/help.
    key: str, optional
        Your api key (needed for authorized calls)
    secret: str, optional
        Secret for your api key.
    **kwargs
        Arguments for the api call

    Returns
    -------
    any
        A python object containing the results of the api call.

    """
    params = kwargs.copy()
    print("fu")

    cfError = "Codeforces Api error"
    if (key is not None) and (secret is not None):
        params['time'] = int(time.time())
        params['apiKey'] = key
        params['from'] = lastSubmit
        params['apiSig'] = _generate_api_sig(method, params, secret)

    url = urllib.parse.urljoin(CODEFORCES_API_URL, "%s" % method)
    print(url)
    print(params)
    with requests.get(url, params=params) as res:
        if res.status_code == 404:
            data = {'status': 'FAILED', 'comment': "%s: No such method" % method}
        elif res.status_code in (429, 503):
            time.sleep(1)
            return call(method, key, secret, **kwargs)
        else:
            data = json.loads(res.text)

    if (data['status'] == 'FAILED'):
        return data
    else:
        return data['result']