import requests
from equities_test.public_method.get_MD5 import get_md5


def get_token(host):
  url = f"{host}/blade-rayo-platform-rights/rayo-platform-public-api/get-token"
  payload = '{"appKey":"SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4"}'
  msg = "AC2022060000000017:SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4:"+payload+":1679997434261:Nqr40NTRXgssYPo4NFLqbIbmDzxRq3QkG8CVhnJ3vlDeEsqPrCCltKjN39nVww4z4IE7EpoPZBJw5d0clA"
  sign = get_md5(msg)
  headers = {
    'Authorization': 'AC2022060000000017',
    'clientId': 'AC2022060000000017',
    'appKey': 'SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4',
    'timeStamp': '1679997434261',
    'sign': sign,
    'Content-Type': 'application/json'
  }
  response = requests.request("POST", url, headers=headers, data=payload)
  return response.json()['data']['accessToken']


if __name__ == '__main__':
  print(get_token("https://5r5152q357.goho.co/right/api"))
