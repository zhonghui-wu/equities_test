import random
import datetime


def get_code():
    nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    rdm = int(random.random()*10000)
    return 'TEST'+nowtime+str(rdm)


if __name__ == '__main__':
    a = get_code()
    print(a)
