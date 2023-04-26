import requests, time
from equities_test.public_method.get_MD5 import get_md5
from equities_test.public_method.get_AES import aesEncrypt
from equities_test.apis.create_code import get_code
from equities_test.apis.get_order_token import get_token


def set_order(phone, productCode, host):
   thirdOrderCode = get_code()
   orderMobile = aesEncrypt(f'{phone}')
   orderPersonName = aesEncrypt('test_order')
   accessToken = get_token(host)
   url = f"{host}/blade-rayo-platform-rights/rayo-platform-public-api/set-rights-order"
   payload = f"""{{"accessToken":"{accessToken}","productCode":"{productCode}","quantity":1,"thirdOrderCode":"{thirdOrderCode}","orderMobile":"{orderMobile}","orderPersonName":"{orderPersonName}"}}"""
   timeStamp = str(int(time.time()*1000))
   msg = "AC2022060000000017:SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4:"+payload+":"+timeStamp+":Nqr40NTRXgssYPo4NFLqbIbmDzxRq3QkG8CVhnJ3vlDeEsqPrCCltKjN39nVww4z4IE7EpoPZBJw5d0clA"
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
   response = requests.request("POST", url, headers=headers, data=payload)
   if response.status_code == 200:
      if response.json()['status'] == 1:
         # print(response.json())
         print("下单" + response.json()['message'])
      else:
         print("下单" + response.json()['message'])
   else:
      print(response.json()['msg'])
   try:
      return response.json()['data']['rightsOrderCode']  # PTU20230410172442726566500
   except:
      return response.json()


if __name__ == '__main__':
   print(set_order(13763910426, 'P2303000000000009', "https://5r5152q357.goho.co/right/api"))
   # set_order(input('请输入手机号：'),input('请输入要下单的产品编号：'))