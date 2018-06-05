
import datetime

def func(days):
    print('tmp/ww2.py-->func():.....')
    now = datetime.datetime.now()
    print('now:{}'.format(now.isoformat()))
    ret = now+datetime.timedelta(days=days)
    print('ret:{}'.format(ret.isoformat()))
    return ret








