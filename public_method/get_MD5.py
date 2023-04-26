import hashlib


def get_md5(str):
    hl = hashlib.md5()
    hl.update(str.encode('utf-8'))
    msg = hl.hexdigest()
    # print("MD5加密后为：" + msg)
    return msg


if __name__ == '__main__':
    a = 'AC2022060000000017:SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4:{"appKey":"SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4"}:1680075255933:Nqr40NTRXgssYPo4NFLqbIbmDzxRq3QkG8CVhnJ3vlDeEsqPrCCltKjN39nVww4z4IE7EpoPZBJw5d0clA'
    get_md5(a)