import datetime


def get_nowtime():
    nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(nowtime)
    return nowtime


def get_nexyeartime():
    nextyeartime = datetime.datetime.today() + datetime.timedelta(days=365)
    nextyeartime = nextyeartime.strftime("%Y-%m-%d %H:%M:%S")
    # print(nextyeartime)
    return nextyeartime


def get_nowtime_timestamp():
    return int(datetime.datetime.now().timestamp())


if __name__ == '__main__':
    print(get_nowtime())
    print(get_nexyeartime())
    print(get_nowtime_timestamp())