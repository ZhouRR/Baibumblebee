import os
import datetime
from pytz import timezone

import settings

cst_tz = timezone('Asia/Shanghai')


def log(*args, console=True):
    if not settings.DEBUG:
        return
    output(args, console=console)


def output(*args, console=True):
    log_out = ''
    for arg in args:
        if arg is None:
            continue
        log_out += str(arg)
    if console:
        print(log_out)
    save_log(log_out)


def save_log(log_str):
    now = datetime.datetime.now(cst_tz)
    date = now.strftime("%Y-%m-%d")
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cache_path = os.path.join(settings.BASE_DIR, 'cache/')
    log_path = os.path.join(settings.BASE_DIR, 'cache/log/')
    log_last = ''
    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    elif os.path.exists(log_path + date + '.log'):
        with open(log_path + date + '.log', 'r', encoding='utf-8', errors='ignore') as fp:
            log_last = fp.read()
    with open(log_path + date + '.log', 'w', encoding='utf-8', errors='ignore') as fpo:
        fpo.write(log_last)
        fpo.write(date_time + '   ' + log_str + u'\n')
