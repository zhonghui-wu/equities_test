from locust import HttpUser, task, TaskSet
import os, time, requests
from equities_test.public_method.get_MD5 import get_md5
log = open('log.txt', mode='a', encoding='utf-8')


class PlaceOrderAPI(TaskSet):
    def get_token(self):
        url = "https://right.rayoservice.com/api/blade-rayo-platform-rights/rayo-platform-public-api/get-token"
        timeStamp = str(int(time.time() * 1000))
        payload = '{"appKey":"lyuYZgIXKiiKJ2YM8WidEy5dBjiQbsynCclWiT2rKU"}'
        msg = "AC2022070000000001:lyuYZgIXKiiKJ2YM8WidEy5dBjiQbsynCclWiT2rKU:" + payload + ":" + timeStamp + ":sLQ494X5hkySPDI34wo3gZdiqihhSej4rNk0inhREdySsh1oW9D6XjTD8YEryMsdJG1z29hjJKVpwOMA"
        sign = get_md5(msg)
        headers = {
        'Authorization': 'AC2022070000000001',
        'clientId': 'AC2022070000000001',
        'appKey': 'lyuYZgIXKiiKJ2YM8WidEy5dBjiQbsynCclWiT2rKU',
        'timeStamp': timeStamp,
        'appSecret': 'sLQ494X5hkySPDI34wo3gZdiqihhSej4rNk0inhREdySsh1oW9D6XjTD8YEryMsdJG1z29hjJKVpwOMA',
        'Content-Type': 'application/json',
        'sign': sign
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # print(response.json()['data']['accessToken'])
        return response.json()['data']['accessToken']

    @task
    def query_product_stores(self):
        accessToken = self.get_token()
        url = "/api/blade-rayo-platform-rights/rayo-platform-public-api/query-product-stores"
        payload = f"""{{"accessToken":"{accessToken}","productCodes":["P2023010000000025"],"pageNum":1,"pageSize":"30","longitude":"110.05125","latitude":"22.57957"}}"""
        timeStamp = str(int(time.time() * 1000))
        msg = "AC2022070000000001:lyuYZgIXKiiKJ2YM8WidEy5dBjiQbsynCclWiT2rKU:" + payload + ":" + timeStamp + ":sLQ494X5hkySPDI34wo3gZdiqihhSej4rNk0inhREdySsh1oW9D6XjTD8YEryMsdJG1z29hjJKVpwOMA"
        sign = get_md5(msg)
        headers = {
            'Authorization': 'AC2022070000000001',
            'clientId': 'AC2022070000000001',
            'appKey': 'lyuYZgIXKiiKJ2YM8WidEy5dBjiQbsynCclWiT2rKU',
            'timeStamp': timeStamp,
            'appSecret': 'sLQ494X5hkySPDI34wo3gZdiqihhSej4rNk0inhREdySsh1oW9D6XjTD8YEryMsdJG1z29hjJKVpwOMA',
            'Content-Type': 'application/json',
            'sign': sign
        }
        # resp = requests.post(url, headers=headers, data=payload)
        # print(resp.json())
        try:
            with self.client.post(url, headers=headers, data=payload, name='查询产品适用商户', catch_response=True) as response:
                # counter = counter + 1
                print(response.elapsed.total_seconds(), file=log)  # 打印接口响应时间
                print(response.status_code, file=log)
                if response.status_code == 200:
                    response.success()
                    print(response.json(), file=log)
                    if response.json()['resultCode'] == 500:
                        response.failure('接口返回500')
                    if response.json()['resultCode'] == 400:
                        response.failure('接口返回400')
                else:
                    response.failure('接口访问失败')
                    print(response.json(), file=log)
        except Exception as e:
            print(response.status_code, file=log)
            print(e, file=log)


class PlaceOrder(HttpUser):
    host = 'https://right.rayoservice.com'
    tasks = [PlaceOrderAPI]
    max_wait = 2000
    min_wait = 1000


if __name__ == '__main__':
    os.system('locust -f test.py')