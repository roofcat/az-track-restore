# encoding:utf-8


from datetime import datetime
import pytz


tz = pytz.timezone("America/Santiago")


def timestamp_to_date(x):
    x = int(x, base=10)
    x = to_unix_timestamp(x)
    return datetime.fromtimestamp(x, tz=tz)


def to_unix_timestamp(x):
    if x is not None:
        if len(str(x)) > 10:
            x = int(str(x)[0:10], base=10)
        return x
    else:
        return None


def get_date_to_string(x):
    fecha = timestamp_to_date(x)
    date_str = datetime.strftime(fecha, '%Y-%m-%d')
    return '"' + str(date_str) + '"'
