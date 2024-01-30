"""
权益测试脚本规划：
1.添加设置--系统字典中对接商品标识的字典配置的字典名称和字典键值
2.系统管理--租户管理--租户选择分乐油站添加对接商品标识
3.添加商品，商品的对应商品标识要和第三方供方商品编号要填写对
4.添加产品
5.产品档案--购买产品
6.选择产品关联刚刚添加的商品
7.下单。校验下单能否正常
8.下单成功后，校验用户产品订单是否有流水
9.再校验供方商品订单有流水
10.最后校验原始码管理、原始码管理及使用记录都有流水
"""
import requests, json
from equities_test.public_method.config import headers, testhost, onlinehost
from equities_test.public_method.get_timestamp import get_nexyeartime, get_nowtime
global id, supplierCode


# 1.添加设置--系统字典中对接商品标识的字典配置的字典名称和字典键值
def add_system_dict(name, key, host):
    url = f'{host}/blade-system/dict/submit'
    payload = json.dumps({"isSealed": 0,
               "code": "good_signature",
               "dictValue": f"{name}",
               "parentId": "1123598814738778238",
               "dictKey": f"{key}",
               "sort": 1,
               "remark": ""})
    resp = requests.post(url, data=payload, headers=headers)
    # print(resp.json())
    if resp.status_code == 200:
        print('对接商品标识的字典配置添加成功')
    else:
        print('添加失败，错误原因是：' + resp.json()['msg'])
    return


# 2.系统管理--租户管理--租户选择分乐油站添加对接商品标识
def add_equities_code(name, key, host):
    url = f'{host}/blade-rayo-platform-supplier/good-interface-sign-config/add'
    payload = json.dumps({"goodInterfaceSign": f"{key}",
                          "goodInterfaceSignName": f"{name}",
                          "tenantName": "分乐油站",
                          "tenantId": "000000",
                          "keyType": 0})
    resp = requests.post(url, data=payload, headers=headers)
    # print(resp.json())
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('分乐油站添加对接商品标识添加成功')
        else:
            print('添加失败，错误原因是：' + resp.json()['msg'])
    else:
        # print(resp.json())
        print('添加失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 3.添加供方
def add_supplier(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup/submit'
    body = {"supplierCode": "",
            "supplierName": f"{name}",
            "contactName": "测试",
            "contactPhone": "13111111111",
            "email": "13111111111@qq.com",
            "tenantId": "000000",
            "thirdApiUrl": "",
            "currUserAgreementDocVersion": ""}
    resp = requests.post(url, headers=headers, data=json.dumps(body))
    # print(resp.json())
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('供方添加成功！')
        else:
            print('供方添加失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 3.1获取添加供方的id和supplierCode
def get_supplier_msg(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup/list?supplierName={name}&supplierGoodType=&enable=&tenantId=&supplierCode=&contactName=&contactPhone=&total=92&current=1&size=5'
    resp = requests.get(url, headers=headers)
    if resp.json()['code'] == 200:
        if resp.json()['data']['records']:
            print('供方信息获取成功')
            id = resp.json()['data']['records'][0]['id']
            supplierCode = resp.json()['data']['records'][0]['supplierCode']
            # print(id)
            # print(supplierCode)
        else:
            print('获取供方内容为空')
    else:
        print('获取供方信息失败')
    return id, supplierCode


# 3.2启用供方
def Enable_supplier(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup/enable'
    id, supplierCode = get_supplier_msg(name, host)
    body = {"id": f"{id}",
            "supplierCode": f"{supplierCode}",
            "enable":True}
    resp = requests.post(url, headers=headers, data=json.dumps(body))
    if resp.status_code == 200:
        if resp.json()['msg'] == "操作成功":
            print(f'启用{name}供方成功')
        else:
            print(f'启用{name}供方失败，请重新启用')
    else:
        print('启用供方接口失败')
    return


# 4.添加商品，商品的对应商品标识要和第三方供方商品编号要填写对
# 4.1获取商品标识信息
def get_commodity_code(key, host):
    url = f'{host}/blade-rayo-platform-supplier/good-interface-set/get?goodInterface={key}'
    resp = requests.get(url, headers=headers)
    msg = resp.json()['data']
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('商品标识信息获取成功')
            del msg['id']
        else:
            print('商品标识信息获取失败，错误原因是：' + resp.json()['msg'])
            assert False
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return msg


# 4.2添加商品
def add_commodity(name, thirdGoodCode, key, host):

    id, supplierCode = get_supplier_msg(name, host)
    url = f'{host}/blade-rayo-platform-supplier/sup-good/submit'
    body = {"supplierCode":f"{supplierCode}","goodName":f"{name}测试","goodType":"虚拟类","goodSubType":"其他","goodDescription":"测试测试","settlementType":"1","goodSpec":"其他","goodSpecCode":"11508969352814634","goodSubSpec":"其他","costPrice":"1","marketPrice":"1","paperAmount":"1","ruleDescription":"","codeGetType":"API","hasInUserAccount":"true","thirdGoodCode":f"{thirdGoodCode}","sourceStore":f"{name}","listPicUrl":"","listSupLicPic":[],"listPsSupplierGoodMainPicOneToOne":[],"listPsSupplierGoodMainPicSixteenToNine":[],"listPsSupplierGoodDetailPic":[],"listPsSupplierGoodVideo":[],"listSupplierGoodStoreMapping":[],"removeApplicableStoreList":[],"applicableFormRequest":{},"goodRating":"五星","rate":"1"}
    payload = json.dumps(dict(body, **get_commodity_code(key, host)))
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('商品添加成功')
        else:
            print('商品添加失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('添加失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 4.3查询所有商品，获取listSupplierGoodId
def get_listSupplierGoodId(name, host, thirdGoodCode):
    url = f'{host}/blade-rayo-platform-supplier/sup-good/list?thirdGoodCode=&goodName={name}测试&hasOnShelf=&goodCode=&supplierCode=&total=221&current=1&size=10'
    resp = requests.get(url, headers=headers)
    # print(resp.json())
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            try:
                goodid = resp.json()['data']['records'][0]['id']
                for i in resp.json()['data']['records']:
                    if i['thirdGoodCode'] == thirdGoodCode:
                        exist = True
                        break
            except Exception as e:
                print(e)
                goodid = False
                exist = False
        else:
            print('商品查询失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return goodid, exist


# 4.4商品上架
def commodity_up(goodid, host):
    url = f'{host}/blade-rayo-platform-supplier/sup-good/batch-on-shelf'
    payload = json.dumps({"listSupplierGoodId":[f"{goodid}"],"hasOnShelf":"true"})
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('商品上架成功')
        else:
            print('商品上架失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 5.添加产品
def add_product(name, host):
    url = f'{host}/blade-rayo-platform-client/psclient-product/submit'
    payload = json.dumps({"effectiveEndTime":f"{get_nexyeartime()}","effectiveStartTime":f"{get_nowtime()}","leaveShelfTime":f"{get_nexyeartime()}","onShelfTime":f"{get_nexyeartime()}","psClientProductDetailPicList":[],"psClientProductDetailVideo":{},"psClientProductListPicList":[],"psClientProductMainPicList":[],"psClientProductMainPicList_1":[],"forbiddenSaleDayList":[],"productName":f"{name}测试","productType":"其他","productSubType":"其他","productRating":"五星","userMaxAmountInOrder":"100","userMaxQuantityInDay":"100","productDescription":"测试","productSpec":"其他","productSubSpec":"其他","costPrice":"1","marketPrice":"1","paperAmount":"1","stockQuantity":"100","canUseAfterMins":"100","sourceStore":f"{name}","hasForCommonStore":"true","hasInUserAccount":"true","canReturn":"true","isSupportCode":1,"hasCouponCodeRecode":"true","hasClientOnly":"false","tenantId":"000000"})
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('产品添加成功')
        else:
            print('产品添加失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('添加失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 5.1查询所有产品，获取产品id
def get_productid(name, host):
    url = f'{host}/blade-rayo-platform-client/psclient-product/list?total=242&current=1&size=10'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            for msg in resp.json()['data']['records']:
                if msg["productName"] == name+'测试':
                    productid = msg["id"]
                    # print(goodid)
                    if productid:
                        productCode = msg['productCode']
                        print('产品id查询成功')
                        break
        else:
            print('产品查询失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return productid, productCode


# 5.2产品上架
def product_up(productid, host):
    url = f'{host}/blade-rayo-platform-client/psclient-product/shelfConfig'
    payload = json.dumps({"id": f"{productid}", "hasOnShelf": "true"})
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('产品上架成功')
        else:
            print('产品上架失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 6.产品档案--购买产品
def buy_product(productCode, host):
    url = f'{host}/blade-rayo-platform-client/client-product-order/submit'
    payload = json.dumps({"appKey": "F8gsmo1fpEHDUYAmmXpyjmBGDNE5a3vuBV5TH/YouL9P4spXYCSrUJ6i7yo7M0I0sjFIU83C98kmpey0C3fTCQ==","clientCode": "AC2022060000000017","productCode": f"{productCode}","marketPrice": "1.00","currPrepay": "877701.71","quantity": 10,"payMethodRemark": "测试","tenantId": "000000","appName": "Rayo应用"})
    resp = requests.post(url, headers=headers, data=payload)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('产品购买成功')
        else:
            print('产品购买失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 7.选择产品关联刚刚添加的商品
# 7.1搜索出对应商品
def get_commodity_msg(name, goodid, host):
    i = 0
    url = f'{host}/blade-rayo-platform-supplier/sup-good/list-belong-tenant-good?goodType=&goodName={name}&current=1&size=8'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            # print(resp.json()['data']['records'])
            # print(len(resp.json()['data']['records']))
            if len(resp.json()['data']['records']) != 1:
                for records in resp.json()['data']['records']:
                    i += 1
                    if records['id'] == goodid:
                        break
            else:
                print('商品搜索成功')
        else:
            print('商品搜索失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return resp.json()['data']['records'][i-1]


# 7.2关联对应商品
def product_goods(name, productCode, goodid, host):
    url = f'{host}/blade-rayo-platform-client/product-good-map/save'
    msg = get_commodity_msg(name, goodid, host)
    payload = json.dumps(
        {
            "tenantId": "000000",
            "clientCode": "",
            "mapType": "互斥模式",
            "productCode": f"{productCode}",
            "listRule": [
                {
                    "productCode": f"{productCode}",
                    "clientCode": "",
                    "enable": "true",
                    "perferLevel": 0,
                    "goodCode": f"{msg['goodCode']}",
                    "goodName": f"{msg['goodName']}",
                    "goodId": f"{msg['id']}",
                    "tenantId": "000000",
                    "supplierName": f"{msg['supplierName']}",
                    "supplierCode": f"{msg['supplierCode']}",
                    "sourceStore": f"{msg['sourceStore']}",
                    "weight": 1,
                    "weightRate": 1,
                    "goodType": f"{msg['goodType']}",
                    "marketPrice": "1.00",
                    "paperAmount": "1.00"
                }
            ]
        }
    )
    resp = requests.post(url, headers=headers, data=payload)
    # print(resp.json())
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            # print(resp.json()['data']['records'])
            print('关联商品成功')
        else:
            print('关联商品失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 8.查找供方商品订单状态
def commodity_order_msg(productOrderCode, host):
    url = f'{host}/blade-rayo-platform-supplier/sup-order/list?goodOrderCode=&startTime=&endTime=&goodName=&productOrderCode={productOrderCode}&useOrderPhone=&productOrderStartTime=&productOrderEndTime=&tenantId=&supplierCode=&clientCode=&appKey=&total=86033&current=1&size=30'
    resp = requests.get(url, headers=headers)
    # print(resp.json()['data']['records'][0]['orderStatusCn'])
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('查询商品订单成功')
            if resp.json()['data']['records'][0]['orderStatusCn'] == '已完成':
                print(productOrderCode + '的供方商品订单状态为：成功')
            elif resp.json()['data']['records'][0]['orderStatusCn'] == '下单失败':
                print(productOrderCode + '的供方商品订单状态为：失败,原因为：' + resp.json()['data']['records'][0]['failureReason'])
            else:
                print(productOrderCode + '的供方商品订单状态为:' + resp.json()['data']['records'][0]['orderStatusCn'])
        else:
            print('查询商品订单失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 9.查找用户产品订单状态
def product_order_msg(productOrderCode, host):
    url = f'{host}/blade-rayo-platform-client/client-user-product-order/list?total=5026&current=1&size=30&productOrderCode={productOrderCode}'
    resp = requests.get(url, headers=headers)
    # print(resp.json()['data']['records'][0]['orderStatus'])
    if resp.status_code == 200:
        if resp.json()['code'] == 200:
            print('查询用户产品订单成功')
            if resp.json()['data']['records'][0]['orderStatus'] == '已完成':
                print(productOrderCode + '的用户产品订单状态为：成功')
            elif resp.json()['data']['records'][0]['orderStatus'] == '下单失败':
                print(productOrderCode + '的用户产品订单状态为：失败,原因为：' + resp.json()['data']['records'][0]['failureReason'])
            # else:
            #     print(productOrderCode + '的用户产品订单状态为:' + resp.json()['data']['records'][0]['orderStatus'])
        else:
            print('查询用户产品订单失败，错误原因是：' + resp.json()['msg'])
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
        assert False
    return


# 10.查看原始码状态
def coupon_code_msg(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup-coupon-code/list?couponCode=&couponName={name}&drawStatus=&batchCode=&useStatus=&total=5584&current=1&size=30'
    resp = requests.get(url, headers=headers)
    # print(resp.json()['data']['records'][0]['orderStatus'])
    if resp.status_code == 200:
        try:
            if resp.json()['code'] == 200:
                if resp.json()['data']['records'][0]['drawStatus'] == '已领取':
                    print('查询原始码状态成功!')
                    print(name + '的原始码状态为已领取!')
                else:
                    print(name + '的原始码状态为为：' + resp.json()['data']['records'][0]['drawStatus'])
            else:
                print('查询原始码状态失败，错误原因是：' + resp.json()['msg'])
        except Exception as e:
            print(e)
            print("查看原始码状态失败")
            print(resp.json())
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
    return


# 11.查看原始码领取状态
def coupon_code_used(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup-coupon-code-used/list?couponCode=&couponCode2=&couponName={name}&supplierName=&useStartTime=&useEndTime=&drawStatus=&batchCode=&useStatus=&total=5566&current=1&size=30'
    resp = requests.get(url, headers=headers)
    # print(resp.json()['data']['records'][0]['orderStatus'])
    if resp.status_code == 200:
        try:
            if resp.json()['code'] == 200:
                print('查询原始码领取状态成功')
                if not resp.json()['data']['records']:
                    print("没有原始码")
                elif resp.json()['data']['records'][0]['drawStatus'] == '已领取':
                    print(name + '的原始码领取状态为已领取!')
                else:
                    print(name + '的原始码领取状态为为：' + resp.json()['data']['records'][0]['drawStatus'])
            else:
                print('查询原始码状态失败，错误原因是：' + resp.json()['msg'])
        except Exception as e:
            print(e)
            print(resp.json())
    else:
        print(resp.json())
        print('返回失败，错误原因是：' + resp.json()['msg'])
    return


# 初始化供方额度
def init_supplier_limit(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup-balance-total/init'
    body = {"supplierCode": f"{supplierCode}",
            "initAmount": "1000",
            "warningBalance": "1000",
            "remark": "初始化供方额度",
            "listSupFile":[{"fileSize": 17910,
                            "sourceFileName": "4.12压力测试方案.docx",
                            "fileUrl": "https://yf-rayoright.oss-cn-guangzhou.aliyuncs.com/upload/20231108/f1d342086ce28f76369c5255291406ff.docx"}]}
    resp = requests.post(url, headers=headers, data=json.dumps(body))
    if resp.json()['msg'] == "操作成功":
        print(f'初始化{name}供方额度成功')
    else:
        print(f'初始化{name}供方额度失败')
    return


# 查找供方额度
def get_supplier_limit(name, host):
    url = f'{host}/blade-rayo-platform-supplier/sup-balance-total/list?supplierName={name}&goodType=&supEnable=&supplierCode=&total=53&current=1&size=30'
    resp = requests.get(url, headers=headers)
    if resp.json()['code'] == 200:
        if not resp.json()['data']['records']:
            print(f'需要初始化{name}供方额度')
            # 执行初始化供方额度
            init_supplier_limit(name, host)
        else:
            # 剩余额度
            currBalance = resp.json()['data']['records'][0]['currBalance']
            # 剩余共享额度
            currShareBalance = resp.json()['data']['records'][0]['currShareBalance']
            # 剩余专属额度
            currGoodBalance = resp.json()['data']['records'][0]['currGoodBalance']
            print(f'{name}剩余供方额度为：{currBalance}, 剩余共享额度为{currShareBalance}, 剩余专属额度为{currGoodBalance}')
    else:
        print('接口返回失败')


# 查找有没有相同供方
def search_supplier(host, name):
    url = f'{host}/blade-rayo-platform-supplier/sup/list?supplierName={name}&supplierGoodType=&enable=&tenantId=&supplierCode=&contactName=&contactPhone=&total=87&current=1&size=30'
    resp = requests.get(url, headers=headers)
    data = resp.json()['data']['records']
    return data


if __name__ == '__main__':
    search_supplier('https://5r5152q357.goho.co/right/api', "科拓优惠券")
    # add_system_dict('测试', '测试', testhost)
    # add_equities_code('测试', '测试')
    # add_supplier('测试', 'https://5r5152q357.goho.co/right/api')
    # a = get_supplier_msg('用来替代的公司名称', 'https://5r5152q357.goho.co/right/api')[1]
    # print(a)
    # Enable_supplier('用来替代的公司名称', 'https://5r5152q357.goho.co/right/api')
    # get_commodity_code('jqcb_coupon',"https://5r5152q357.goho.co/right/api")
    # add_commodity('weineng','qj_wn')
    # get_supplier_limit('测试初始化供方额度', 'https://5r5152q357.goho.co/right/api')
    # print(get_listSupplierGoodId('微能测试',"https://5r5152q357.goho.co/right/api"))
    # commodity_up(get_listSupplierGoodId('weineng'))
    # add_product('weineng')
    # product_up(get_productid('weineng'))
    # print(get_commodity_msg('微能测试','1645684477996429313'))
    # print(get_commodity_msg('weineng测试'))
    # product_goods('weineng测试', 'P2304000000000006')
    # commodity_order_msg('PTU20230410172442726566500')