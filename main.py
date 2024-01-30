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
10.最后校验原始码管理是否有流水
11.原始码管理及使用记录是否有流水
"""
import time

from apis.set_order import set_order
from public_method.config import testhost, onlinehost
from apis.equities_process_api import add_system_dict, add_equities_code, add_commodity, search_supplier
from apis.equities_process_api import get_listSupplierGoodId, commodity_up, add_product, get_productid, product_up
from apis.equities_process_api import buy_product, product_goods, commodity_order_msg, product_order_msg
from apis.equities_process_api import coupon_code_msg, coupon_code_used, add_supplier, Enable_supplier, get_supplier_limit


def equities_test():
    # host = input("请输入要测的服务：(正式环境/测试环境)")
    # if host == '正式环境':
    #     host = onlinehost
    # elif host == '测试环境':
    #     host = testhost
    host = testhost
    name = input("请输入要测的权益的名称：")
    dict_key = input("请输入对应的键值：")
    thirdGoodCode = input("请输入对应的第三方供方商品编号：")
    phone = input("请输入要下单的手机号：")
    # 1.添加设置--系统字典中对接商品标识的字典配置的字典名称和字典键值
    add_system_dict(name, dict_key, host)
    # 2.系统管理--租户管理--租户选择分乐油站添加对接商品标识
    add_equities_code(name, dict_key, host)
    # 查询是否存在要添加的供方名称，如果不存在则添加供方，启用供方
    if not search_supplier(host, name):
        # 添加供方
        add_supplier(name, host)
        # 启用供方
        Enable_supplier(name, host)
        # 查询有没有该供方额度，如果没有则初始化额度，如果有则打印剩余额度
        get_supplier_limit(name, host)
    else:
        print('供方已存在，跳过添加供方')
        # 查询有没有该供方额度，如果没有则初始化额度，如果有则打印剩余额度
        get_supplier_limit(name, host)
    if get_listSupplierGoodId(name, host,thirdGoodCode)[1]:
        print('已存在相同的商品，不执行添加商品和产品等操作。')
        # 获取下单的产品id
        productid, productCode = get_productid(name, host)
        # 下单
        productOrderCode = set_order(phone, productCode, host)
        time.sleep(3)
        # 查找用户产品订单状态
        product_order_msg(productOrderCode, host)
        # 查找供方商品订单状态
        commodity_order_msg(productOrderCode, host)
        # 查看原始码状态
        # coupon_code_msg(name, host)
        if input("请输入是否有领取码状态返回：(是/否)。") == "是":
            # 查看原始码领取状态
            coupon_code_used(name, host)
            print("测试结束！")
        else:
            print("测试结束！")
    else:
        # 3.添加商品，商品的对应商品标识要和第三方供方商品编号要填写对
        # 3.1获取商品标识信息
        # 3.2添加商品
        add_commodity(name, thirdGoodCode, dict_key, host)
        # 3.3查询所有商品，获取listSupplierGoodId
        goodid = get_listSupplierGoodId(name, host, thirdGoodCode)[0]
        # 3.4商品上架
        commodity_up(goodid, host)
        # 4.添加产品
        add_product(name, host)
        # 4.1查询所有产品，获取产品id
        productid, productCode = get_productid(name, host)
        # 4.2产品上架
        product_up(productid, host)
        # 5.产品档案--购买产品
        buy_product(productCode, host)
        # 6.选择产品关联刚刚添加的商品
        # 6.1搜索出对应商品
        # 6.2关联对应商品
        product_goods(name, productCode, goodid, host)
        # 7.下单
        productOrderCode = set_order(phone, productCode, host)
        time.sleep(3)
        # 8.查找用户产品订单状态
        product_order_msg(productOrderCode, host)
        # 9.查找供方商品订单状态
        commodity_order_msg(productOrderCode, host)
        # 10.查看原始码状态
        # coupon_code_msg(name, host)
        if input("请输入是否有领取码状态返回：(是/否)。") == "是":
            # 11.查看原始码领取状态
            coupon_code_used(name, host)
            print("测试结束！")
        else:
            print("测试结束！")
    return


if __name__ == '__main__':
    equities_test()
    "集群车宝: jqcb_coupon ,第三方权益：1|73549|0.01,13763910426"
    "卓悦加油:zhuo_yue, 第三方商品标识:RY_RY3YCSQ"
    "科拓优惠券:kt_coupon,第三方商品标识:MONTHLY_PERCENT_15_CUT,phone:13763910426"


