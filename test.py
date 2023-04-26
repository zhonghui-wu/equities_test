import json
a = {"supplierCode":"SUP2303000000000005",
     "goodName":"需要取个名称",
     "goodType":"虚拟类",
     "goodSubType":"其他",
     "goodDescription":"测试测试",
     "settlementType":"1",
     "goodSpec":"其他",
     "goodSpecCode":"11508969352814634",
     "goodSubSpec":"其他",
     "costPrice":"1",
     "marketPrice":"1",
     "paperAmount":"1",
     "ruleDescription":"",
     "codeGetType":"API",
     "hasInUserAccount":"true",
     "thirdGoodCode":"测试",
     "sourceStore":"测试",
     "listPicUrl":"",
     "listSupLicPic":[],
     "listPsSupplierGoodMainPicOneToOne":[],
     "listPsSupplierGoodMainPicSixteenToNine":[],
     "listPsSupplierGoodDetailPic":[],
     "listPsSupplierGoodVideo":[],
     "listSupplierGoodStoreMapping":[],
     "removeApplicableStoreList":[],
     "applicableFormRequest":{},
     "goodRating":"五星",
     "rate":"1"}

data = {'goodInterfaceSign': 'qj_wn', 'description': '青桔微能', 'hasForCommonStore': True, 'hasInUserAccount': True, 'hasMultiInOrder': False, 'hasAutoImport': False, 'hasSupportUseStatus': 0, 'hasSupportResend': 1, 'hasSupportCancel': 0, 'hasSupportRefund': 0, 'hasSupportVerification': 0, 'hasCheckOffCode': 1, 'hasCoupon': 0, 'hasRedeemCode': 0, 'hasThirdBalance': 0, 'hasThirdGoodBalance': 0, 'hasStoreInterface': 0, 'hasQueryAvailableGood': 0, 'hasQueryGoodInfo': 1, 'hasQueryProductStock': 0, 'hasQueryStoreProduct': 0, 'hasProductInfoChangeNoti': 0, 'hasServiceInterface': 0, 'hasAccountCheckingInterface': 0, 'hasInvoiceInterface': 0}


newdate = dict(a, **data)
# print(json.dumps(newdate, ensure_ascii=False))
# print(newdate)

# 微能,qj_wn,SYW2203020001,13763910426

b = {'code': 200, 'success': True, 'data': {'records': [{'id': '1645708043634733057', 'goodOrderCode': 'SSO20230411163908036288893', 'firstGoodOrderCode': None, 'orderDate': '2023-04-11 16:39:08', 'orderStatus': 2, 'failureReason': None, 'thirdOrderCode': None, 'thirdOrderStatus': None, 'thirdFailureReason': None, 'supplierCode': 'SUP2303000000000005', 'supplierName': '中卉供方', 'storeCode': None, 'storeName': None, 'storeSignature': None, 'sourceStore': '微能', 'supplierTenanId': None, 'supplierTenanName': None, 'goodCode': 'SG2304000000000020', 'goodName': '微能测试', 'thirdGoodCode': 'SYW2203020001', 'goodDescription': '测试测试', 'hasInUserAccount': None, 'goodSpec': '其他', 'goodSpecCode': None, 'goodSubSpec': '其他', 'goodType': '虚拟类', 'goodSubType': '其他', 'goodInterfaceSign': 'qj_wn', 'settlementType': None, 'quantity': 1, 'costPrice': '1.00', 'marketPrice': '1.00', 'costAmount': '1.00', 'marketAmount': '1.00', 'actualAmount': '1.00', 'discountAmount': '0.00', 'benifitAmount': '0.00', 'codeGetType': 'API', 'codeTradeType': None, 'payStatus': None, 'payAmount': None, 'paySource': None, 'paySourceRemark': None, 'payMethod': None, 'payMethodRemark': None, 'payDiscountSource': None, 'payDiscountSourceRemark': None, 'payDiscountMethod': None, 'payDiscountMethodRemark': None, 'payMchCode': None, 'userPayCardCode': None, 'userPayCardCodeRemark': None, 'payPlatformOrderCode': None, 'payThirdOrderCode': None, 'payPostDataJson': None, 'payResultDataJson': None, 'userOrderClientCode': 'AC2022060000000017', 'userOrderClientName': 'Rayo接入', 'userOrderClientAppKey': 'SmCVbpHQTX9ZrUaYg6P3fZ3g0rJSp6JbSAhawQX4', 'userOrderClientAppName': 'Rayo应用', 'tenantId': '000000', 'tenantName': '分乐油站', 'orderUserId': None, 'orderUserCode': None, 'orderUserName': 't*********', 'orderUserPhone': '13763910426', 'userProductOrderCode': 'PTU20230411163907973196811', 'userProductOrderDate': '2023-04-11 16:39:07', 'userOrderProductCode': None, 'userOrderProductName': None, 'userProductOrderCostAmount': '1.00', 'userProductOrderMarketAmount': '1.00', 'userProductOrderActualAmount': '1.00', 'userProductOrderDiscountAmount': '0.00', 'hasErrorOrder': None, 'hasReturnOrder': None, 'hasReturn': None, 'productOrderVoucherCode': None, 'thirdOrderStatusRemark': None, 'paperAmount': '1.00', 'errorDesc': None, 'ruleDescription': '', 'returnDate': None, 'auditorCode': None, 'auditorName': None, 'auditTime': None, 'auditRemark': None, 'reissueManCode': None, 'reissueManName': None, 'reissueNewOrderCode': None, 'reissueTime': None, 'reissueRemark': None, 'hasResend': None, 'createTime': '2023-04-11 16:39:08', 'creatorCode': 'system', 'creatorName': '系统自动执行', 'modifyTime': '2023-04-11 16:39:08', 'modifierCode': 'system', 'modifierName': '系统自动执行', 'remark': None, 'listCouponCodeRecord': None, 'listCouponCodeUsedRecord': None, 'additionalParametersType': None, 'parameter1': None, 'parameter2': None, 'parameter3': None, 'parameter4': None, 'parameter5': None, 'parameter6': None, 'parameter7': None, 'parameter8': None, 'parameter9': None, 'settlementDate': None, 'isSettlement': False, 'importBatchCode': None, 'orderStatusCn': '处理中', 'hasErrorOrderCn': '否', 'hasInUserAccountCn': '否', 'hasReturnOrderCn': '否', 'hasReturnCn': None, 'thirdOrderStatusCn': '失败', 'goodStoreMappingCount': 1, 'designGoodStoreMapping': None, 'listPicUrl': '', 'goodInterfaceSignCn': '微能'}], 'total': 1, 'size': 30, 'current': 1, 'orders': [], 'optimizeCountSql': True, 'searchCount': True, 'countId': None, 'maxLimit': None, 'pages': 1}, 'msg': '操作成功'}
print(b['data']['records'][0]['failureReason'])
print(b['data']['records'][0])


