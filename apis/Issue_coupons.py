from equities_test.public_method.get_MD5 import get_md5
from equities_test.public_method.get_timestamp import get_nowtime_timestamp
import random, requests
timestamp = get_nowtime_timestamp()
rdm = int(random.randint(11111111, 99999999))
a = 'applyNo=1&couponCode=PC2023051100007&appKey=123456&timestamp=1683859888&password=123456'
b = 'carNo=赣BLB101&flowNo=UPC2023051200002&phone=13763910426&appKey=123456&timestamp=1683859888&password=123456'


def external_issue():
    global flowNo
    msg = f'applyNo={rdm}&couponCode=PC2023051200004&appKey=123456&timestamp={timestamp}&password=123456'
    sign = get_md5(msg)
    payload = {
        "appKey": "123456",
        "timestamp": timestamp,
        "sign": sign,
        "params": {
            "couponCode": "PC2023051200004",
            "applyNo": rdm
        }
    }
    header = {"Content-Type": "application/json"}
    url = 'https://5r5152q357.goho.co/api/rayo-dbo-product/external/api/park/coupon/grantParkCoupon'
    resp = requests.post(url, headers=header, json=payload)
    flowNo = resp.json()['data']['flowNo']
    # print(flowNo)
    print(resp.json())


def external_coupon():
    msg = f'carNo=鲁Q5NL59&flowNo={flowNo}&phone=13392673544&appKey=123456&timestamp={timestamp}&password=123456'
    sign = get_md5(msg)
    header = {"Content-Type": "application/json"}
    payload = {
                "appKey": "123456",
                "timestamp": timestamp,
                "sign": sign,
                "params": {
                    "flowNo": flowNo,
                    "phone": "13392673544",
                    "carNo": "鲁Q5NL59"
                }
            }
    url = 'https://5r5152q357.goho.co/api/rayo-dbo-product/external/api/park/coupon/receiveParkCoupon'
    resp = requests.post(url, headers=header, json=payload)
    print(resp.json())


if __name__ == '__main__':
    external_issue()
    external_coupon()