from locust import HttpUser, task, TaskSet, events
import os, time, random, sys
from equities_test.public_method.get_MD5 import get_md5
from equities_test.public_method.get_AES import aesEncrypt
from equities_test.apis.create_code import get_code
from equities_test.apis.get_order_token import get_token


class PlaceOrderAPI(TaskSet):

    @task
    def place_order(self):
        thirdOrderCode = get_code()
        orderMobile = aesEncrypt("13763910426")
        orderPersonName = aesEncrypt('test_order')
        accessToken = get_token("https://5r5152q357.goho.co/right/api")
        productCode = random.choice(["P2023070000000002", "P2023070000000001"])
        url = "/right/api/blade-rayo-platform-rights/rayo-platform-public-api/set-rights-order"
        payload = f"""{{"accessToken":"{accessToken}","productCode":"{productCode}","quantity":1,"thirdOrderCode":"{thirdOrderCode}","orderMobile":"{orderMobile}","orderPersonName":"{orderPersonName}"}}"""
        timeStamp = str(int(time.time() * 1000))
        msg = "AC2022060000000017:SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4:" + payload + ":" + timeStamp + ":Nqr40NTRXgssYPo4NFLqbIbmDzxRq3QkG8CVhnJ3vlDeEsqPrCCltKjN39nVww4z4IE7EpoPZBJw5d0clA"
        sign = get_md5(msg)
        headers = {
            'Authorization': 'AC2022060000000017',
            'clientId': 'AC2022060000000017',
            'appKey': 'SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4',
            'timeStamp': timeStamp,
            'appSecret': 'Nqr40NTRXgssYPo4NFLqbIbmDzxRq3QkG8CVhnJ3vlDeEsqPrCCltKjN39nVww4z4IE7EpoPZBJw5d0clA',
            'Content-Type': 'application/json',
            'sign': sign
        }
        try:
            with self.client.post(url, headers=headers, data=payload, name='下单', catch_response=True) as response:
                print(response.status_code)
                print(thirdOrderCode)
                if response.status_code == 200:
                    response.success()
                    print(response.json())
                    if response.json()['resultCode'] == 500:
                        response.failure('接口返回500')
                    if response.json()['resultCode'] == 400:
                        response.failure('接口返回400')
                else:
                    response.failure('接口访问失败')
                    print(response.json())
        except Exception as e:
            print(response.status_code)
            print(e)


class PlaceOrder(HttpUser):
    host = 'https://5r5152q357.goho.co'
    tasks = [PlaceOrderAPI]
    max_wait = 2000
    min_wait = 1000


if __name__ == '__main__':
    os.system('locust -f place_order_performance_test.py')
    # print(random.choice(["P2303000000000009", "P2303000000000007"]))