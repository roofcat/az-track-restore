# encoding:utf-8


import tablib


def optional_name(optional, field):
    if optional is not None:
        return optional[field]
    else:
        return ''


def create_tablib(data):
    try:
        file = tablib.Dataset(title='Correos')
        file.headers = ()

        if data is not None:
            for row in data:
                print row

    except Exception as e:
        print e
