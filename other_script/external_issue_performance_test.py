from locust import HttpUser, task, TaskSet
import os, random
from equities_test.public_method.get_MD5 import get_md5
from equities_test.public_method.get_timestamp import get_nowtime_timestamp
log = open('../apis/log.txt', mode='a', encoding='utf-8')
timestamp = get_nowtime_timestamp()
rdm = int(random.randint(11111111, 99999999))


class ExternalIssueAPI(TaskSet):
    # @task
    # def external_issue(self):
    #     msg = f'applyNo={rdm}&couponCode=PC2023051100007&appKey=123456&timestamp={timestamp}&password=123456'
    #     sign = get_md5(msg)
    #     payload = {
    #         "appKey": "123456",
    #         "timestamp": timestamp,
    #         "sign": sign,
    #         "params": {
    #             "couponCode": "PC2023051100007",
    #             "applyNo": rdm
    #         }
    #     }
    #     header = {"Content-Type": "application/json"}
    #     url = '/api/rayo-dbo-product/external/api/park/coupon/grantParkCoupon'
    #     with self.client.post(url, headers=header, json=payload, name='外部发券接口', catch_response=True) as resp:
    #         print(resp.json(), file=log)
    #         if resp.status_code == 200:
    #             resp.success()
    #         else:
    #             print(resp.status_code)
    #             resp.failure('接口返回错误')

    @task
    def external_coupon(self):
        msg = f'carNo=赣BLB101&flowNo=UPC2023051200003&phone=137{rdm}&appKey=123456&timestamp={timestamp}&password=123456'
        sign = get_md5(msg)
        header = {"Content-Type": "application/json"}
        payload = {
                    "appKey": "123456",
                    "timestamp": timestamp,
                    "sign": sign,
                    "params": {
                        "flowNo": "UPC2023051200003",
                        "phone": "137"+str(rdm),
                        "carNo": "赣BLB101"
                    }
                }
        url = '/api/rayo-dbo-product/external/api/park/coupon/receiveParkCoupon'
        with self.client.post(url, headers=header, json=payload, name='外部领券接口', catch_response=True) as resp:
            print(resp.json())
            print(resp.json(), file=log)
            if resp.status_code == 200:
                resp.success()
            else:
                print(resp.status_code)
                resp.failure('接口返回错误')


class PlaceOrder(HttpUser):
    host = 'https://5r5152q357.goho.co'
    tasks = [ExternalIssueAPI]
    max_wait = 2000
    min_wait = 1000


if __name__ == '__main__':
    os.system('locust -f external_issue_performance_test.py')