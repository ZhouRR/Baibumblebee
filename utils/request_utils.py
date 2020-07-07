import urllib3

from utils.log_utils import log


def get(url, content=''):
    log('GET:', url)

    pool_manger = urllib3.PoolManager()
    resp = pool_manger.request('GET', url, headers={
        'Content-Type': content
    })
    log('status:', resp.status)
    data = resp.data.decode()
    log('data:', data, console=False)
    return data


def post(url, post_data, content):
    log('POST:', url)
    log('post_data', post_data)

    pool_manger = urllib3.PoolManager()
    resp = pool_manger.request('POST', url, body=post_data, headers={
        'Content-Type': content
    })
    log('status:', resp.status)
    data = resp.data.decode()
    log('data:', data, console=False)
    return data
