import pandas as pd
import requests
from equities_test.apis.rights_login import rights_login

# 指定CSV文件的路径
file_path = 'D:\Python_Projects\RockProjects\equities_test\pack.csv'

# 使用pandas读取CSV文件
df = pd.read_csv(file_path, encoding='gbk')

# 获取第一列的数据（列名或整数索引）
# 如果CSV有标题行，并且第一列的列名是'first_column'，则使用：
first_column_data = df['name']
# 如果没有标题行或者想要使用整数索引，则使用：
# first_column_data = df.iloc[:, 0]
new_values = []
# 循环遍历第一列的每一行数据
for index, value in first_column_data.items():
    # index是行的索引，value是对应行的数据值
    value = value.strip()
    # print(value)
    url = f'https://right.rayoservice.com/api/blade-rayo-platform-parking/parking/lot/listParkPage?parkName={value}' \
          f'&thirdSysCode=ydt&current=1&size=30 '
    header = rights_login('https://right.rayoservice.com/api', 'rock', '123456')
    resp = requests.get(url, headers=header)
    # print(resp.json()['data']['records'])
    try:
        park_auth_code = resp.json()['data']['records'][0]['parkAuthCode']
    except:
        park_auth_code = 0
    # print(value, park_auth_code)
    new_values.append(park_auth_code)


df['key'] = new_values
# 将更新后的DataFrame写回CSV文件
df.to_csv(file_path, index=False)


# url = f'https://right.rayoservice.com/api/blade-rayo-platform-parking/parking/lot/listParkPage?parkName=富丽大酒店' \
#           f'&thirdSysCode=ydt&current=1&size=30 '
# header = rights_login('https://right.rayoservice.com/api', 'rock', '123456')
# resp = requests.get(url, headers=header)
# # print(resp.json())
# park_auth_code = resp.json()['data']['records'][0]['parkAuthCode']
# print(park_auth_code)
