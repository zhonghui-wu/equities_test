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


if __name__ == '__main__':
    get_nowtime()
    get_nexyeartime()