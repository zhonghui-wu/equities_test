import json

# c = {"code":200,"success":"true","data":{"records":[{"id":"1651783748487254018","goodCode":"SG2304000000000028","goodName":"洗车助手优惠券测试","thirdGoodCode":"EJ202304258248","goodDescription":"测试测试","goodType":"虚拟类","goodSubType":"其他","goodRating":"五星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"1.00","marketPrice":"1.00","paperAmount":"1.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000005","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"洗车助手优惠券","sourceStore":"洗车助手优惠券","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-04-28 11:01:49","creatorCode":"1638440307854475265","creatorName":"吴中卉","modifyTime":"2023-04-28 11:01:49","modifierCode":"1638440307854475265","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"中卉供方","goodStoreMappingCount":1,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1651748717467308033","goodCode":"SG2304000000000027","goodName":"洗车助手优惠券","thirdGoodCode":"EJ202304258248","goodDescription":"洗车助手测试","goodType":"服务类","goodSubType":"洗车","goodRating":"五星","ruleDescription":"","goodSpec":"服务","goodSpecCode":"null","goodSubSpec":"优惠券","costPrice":"1.00","marketPrice":"1.00","paperAmount":"1.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2304000000000003","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"洗车助手优惠券","sourceStore":"洗车助手","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-04-28 08:42:37","creatorCode":"1612271338407919617","creatorName":"李昌俊","modifyTime":"2023-04-28 09:52:01","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"洗车助手科技公司","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638074808108920834","goodCode":"SG2303000000000010","goodName":"鼎聚代驾券（使用）","thirdGoodCode":"dj0050","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000002","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"鼎聚代驾券","sourceStore":"鼎聚代驾券","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-21 15:07:23","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-04-26 15:19:52","modifierCode":"1638440307854475265","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"2","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"使用供方","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1646772622359916545","goodCode":"SG2304000000000026","goodName":"车仆汽油添加剂燃油宝6瓶","thirdGoodCode":"222","goodDescription":"车仆汽油添加剂燃油宝6瓶1","goodType":"实物类","goodSubType":"其他","goodRating":"一星","ruleDescription":"11","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2304000000000002","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"测试20221115","sourceStore":"11","listPicUrl":"","rate":"0","tenantId":"null","createTime":"2023-04-14 15:09:23","creatorCode":"1123598821738675201","creatorName":"admin","modifyTime":"2023-04-20 11:43:45","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"睿途","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1646721070039429121","goodCode":"SG2304000000000025","goodName":"加厚双面珊瑚绒洗车毛巾3条","thirdGoodCode":"11","goodDescription":"加厚双面珊瑚绒洗车毛巾3条","goodType":"实物类","goodSubType":"其他","goodRating":"一星","ruleDescription":"11","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000015","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"测试20221115","sourceStore":"11","listPicUrl":"https://yf-rayoright.oss-cn-guangzhou.aliyuncs.com/upload/20230414/614e6136b7ba96cd0d7329016c1e9c2d.jpg","rate":"0","tenantId":"null","createTime":"2023-04-14 11:44:32","creatorCode":"1123598821738675201","creatorName":"admin","modifyTime":"2023-04-14 11:46:08","modifierCode":"1123598821738675201","modifierName":"admin","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"测试供方20221115","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1592500309644353537","goodCode":"SG2022110000000021","goodName":"蛋黄酥","thirdGoodCode":"11","goodDescription":"11","goodType":"实物类","goodSubType":"其他","goodRating":"一星","ruleDescription":"11","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000015","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"测试20221115","sourceStore":"11","listPicUrl":"https://yf-rayoright.oss-cn-guangzhou.aliyuncs.com/upload/20230412/ee830e1a5b0107b57e88b9f7ab04c598.jpg","rate":"0","tenantId":"null","createTime":"2022-11-15 20:50:36","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-04-12 15:33:42","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"测试供方20221115","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1645994085885538306","goodCode":"SG2304000000000024","goodName":"阿芷商品2","thirdGoodCode":"1128","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"null","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"true","supplierCode":"SUP2022100000000001","codeGetType":"导入","codeTradeType":"导入","goodInterfaceSign":"麦当劳券接口","sourceStore":"来源方","listPicUrl":"null","rate":"0","tenantId":"null","createTime":"2023-04-12 11:35:46","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-04-12 11:36:06","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"excel导入供方商品","settlementType":"null","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"是","supplierName":"阿芷","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1645989412340363265","goodCode":"SG2304000000000022","goodName":"1122","thirdGoodCode":"22","goodDescription":"1122","goodType":"服务类","goodSubType":"充值中心","goodRating":"二星","ruleDescription":"1122","goodSpec":"素材","goodSpecCode":"null","goodSubSpec":"直充","costPrice":"22.00","marketPrice":"22.00","paperAmount":"22.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"false","hasMultiInOrder":"false","supplierCode":"SUP2022060000000001","codeGetType":"导入","codeTradeType":"null","goodInterfaceSign":"京东E卡手动导入","sourceStore":"22","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-04-12 11:17:12","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-04-12 11:19:18","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"否","hasMultiInOrderCn":"否","supplierName":"金拱门麦当劳","goodStoreMappingCount":25,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1645724584606560257","goodCode":"SG2304000000000021","goodName":"微能测试","thirdGoodCode":"SYW2203020001","goodDescription":"测试测试","goodType":"虚拟类","goodSubType":"其他","goodRating":"五星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"1.00","marketPrice":"1.00","paperAmount":"1.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000005","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"微能","sourceStore":"微能","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-04-11 17:44:52","creatorCode":"1638440307854475265","creatorName":"吴中卉","modifyTime":"2023-04-11 17:44:52","modifierCode":"1638440307854475265","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"中卉供方","goodStoreMappingCount":1,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1643169599985324033","goodCode":"SG2304000000000004","goodName":"新的测试商品","thirdGoodCode":"SYW2203020006","goodDescription":"100","goodType":"服务类","goodSubType":"其他","goodRating":"五星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"1.00","marketPrice":"1.00","paperAmount":"1.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000005","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"微能","sourceStore":"微能","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-04-04 16:32:16","creatorCode":"1638440307854475265","creatorName":"吴中卉","modifyTime":"2023-04-04 17:31:34","modifierCode":"1638440307854475265","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"中卉供方","goodStoreMappingCount":1,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1631494178420133890","goodCode":"SG2023030000000004","goodName":"Q币","thirdGoodCode":"gzrysz_ry6ypcsq","goodDescription":"Q币","goodType":"虚拟类","goodSubType":"充值中心","goodRating":"五星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"直充","costPrice":"0.50","marketPrice":"0.50","paperAmount":"0.50","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022060000000007","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"如约中石油","sourceStore":"如约中石油","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-03 11:18:18","creatorCode":"1627853185430913025","creatorName":"吴中卉","modifyTime":"2023-04-01 16:06:45","modifierCode":"1638440307854475265","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"企鹅","goodStoreMappingCount":3,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1641297326093496322","goodCode":"SG2303000000000022","goodName":"大融城门店测试","thirdGoodCode":"SYW2204070001","goodDescription":"100","goodType":"其他","goodSubType":"其他","goodRating":"五星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"10.00","marketPrice":"10.00","paperAmount":"10.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000006","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"微能","sourceStore":"微能","listPicUrl":"","rate":"0","tenantId":"null","createTime":"2023-03-30 12:32:31","creatorCode":"1123598821738675201","creatorName":"admin","modifyTime":"2023-03-30 12:34:46","modifierCode":"1123598821738675201","modifierName":"admin","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"大融城测试","goodStoreMappingCount":3,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638444096476946434","goodCode":"SG2303000000000021","goodName":"微能测试","thirdGoodCode":"SYW2204070001","goodDescription":"100","goodType":"其他","goodSubType":"其他","goodRating":"五星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"10.00","marketPrice":"10.00","paperAmount":"10.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000005","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"微能","sourceStore":"微能","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-22 15:34:48","creatorCode":"1638440307854475265","creatorName":"吴中卉","modifyTime":"2023-03-22 17:37:35","modifierCode":"1638440307854475265","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"中卉供方","goodStoreMappingCount":24,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638442545561739265","goodCode":"SG2303000000000020","goodName":"322","thirdGoodCode":"11","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"二星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022060000000001","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"微能","sourceStore":"111","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-22 15:28:38","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-22 15:28:42","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"金拱门麦当劳","goodStoreMappingCount":24,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638380482764288001","goodCode":"SG2303000000000013","goodName":"银讯无门店无核销","thirdGoodCode":"11","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"11","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000004","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"银讯无门店无核销","sourceStore":"银讯无门店无核销","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-22 11:22:01","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-22 11:26:24","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"2","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"银讯测试","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638381052728258561","goodCode":"SG2303000000000014","goodName":"银讯无门店有核销","thirdGoodCode":"11","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"二星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000004","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"银讯无门店有核销","sourceStore":"银讯无门店有核销","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-22 11:24:17","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-22 11:26:19","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"2","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"银讯测试","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638381511211823106","goodCode":"SG2303000000000015","goodName":"银讯中石化自助洗车","thirdGoodCode":"11","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"11","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000004","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"银讯中石化自助洗车","sourceStore":"银讯中石化自助洗车","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-22 11:26:07","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-22 11:26:16","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"2","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"银讯测试","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638074875498803202","goodCode":"SG2303000000000011","goodName":"鼎聚代驾券（无需）","thirdGoodCode":"djry20","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000003","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"鼎聚中石化洗车","sourceStore":"鼎聚代驾券","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-21 15:07:39","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-21 16:36:28","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"3","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"无需供方","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638079305111646210","goodCode":"SG2303000000000012","goodName":"鼎聚代驾券（发放）","thirdGoodCode":"djry20","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2303000000000001","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"鼎聚中石化洗车","sourceStore":"鼎聚代驾券","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-21 15:25:15","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-21 15:25:20","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"发放供方","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1632638540134834178","goodCode":"SG2303000000000002","goodName":"鼎聚代驾券","thirdGoodCode":"djry20","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022100000000001","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"鼎聚中石化洗车","sourceStore":"鼎聚代驾券","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-06 15:05:36","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-21 15:24:54","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"阿芷","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1637747382057250817","goodCode":"SG2303000000000008","goodName":"一点停城市运营券","thirdGoodCode":"11","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022100000000001","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"一点停城市运营券","sourceStore":"11","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-20 17:26:18","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-21 15:08:54","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"3","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"阿芷","goodStoreMappingCount":6,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1638002482302496769","goodCode":"SG2303000000000009","goodName":"银讯中石化","thirdGoodCode":"11","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022100000000001","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"银讯中石化洗车","sourceStore":"11","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-21 10:19:59","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-21 15:08:39","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"2","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"阿芷","goodStoreMappingCount":6,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1597870247343058945","goodCode":"SG2022110000000038","goodName":"一点科技10元停车券","thirdGoodCode":"638721f083fa047c4dd646bb12673","goodDescription":"一点科技","goodType":"虚拟类","goodSubType":"汽车·用品","goodRating":"五星","ruleDescription":"一点科技","goodSpec":"服务","goodSpecCode":"null","goodSubSpec":"优惠券","costPrice":"10.00","marketPrice":"10.00","paperAmount":"10.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022070000000017","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"一点科技发券","sourceStore":"一点科技","listPicUrl":"","rate":"0","tenantId":"null","createTime":"2022-11-30 16:28:49","creatorCode":"1520035166396538882","creatorName":"郭晶","modifyTime":"2023-03-21 10:12:28","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"2","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"广州荣焰科技有限公司","goodStoreMappingCount":1669,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1637742720545533954","goodCode":"SG2303000000000007","goodName":"河南","thirdGoodCode":"0123456789000015","goodDescription":"11","goodType":"其他","goodSubType":"充值中心","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000020","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"河南中石油","sourceStore":"河南","listPicUrl":"","rate":"11","tenantId":"null","createTime":"2023-03-20 17:07:47","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-20 17:17:10","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"3","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"河南中石化","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1637741029616070657","goodCode":"SG2303000000000006","goodName":"河南中石化商品（副本）","thirdGoodCode":"0123456789000015","goodDescription":" 只能为汉字","goodType":"其他","goodSubType":"充值中心","goodRating":"二星","ruleDescription":" 只能为汉字","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"优惠券","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000020","codeGetType":"API","codeTradeType":"导入","goodInterfaceSign":"河南中石油","sourceStore":"石油","listPicUrl":"","rate":"0","tenantId":"null","createTime":"2023-03-20 17:01:04","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-20 17:01:24","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"excel导入供方商品","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"河南中石化","goodStoreMappingCount":1,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1544617505392951297","goodCode":"SG2022070000000001","goodName":"河南中石化商品","thirdGoodCode":"0123456789000015","goodDescription":" 只能为汉字","goodType":"其他","goodSubType":"充值中心","goodRating":"二星","ruleDescription":" 只能为汉字","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"优惠券","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000020","codeGetType":"API","codeTradeType":"导入","goodInterfaceSign":"河南中石油","sourceStore":"石油","listPicUrl":"","rate":"0","tenantId":"null","createTime":"2022-07-06 17:41:26","creatorCode":"1520035166396538882","creatorName":"郭晶","modifyTime":"2023-03-20 15:30:04","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"excel导入供方商品","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"河南中石化","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1633292577951780866","goodCode":"SG2023030000000006","goodName":"如约发放结算","thirdGoodCode":"gzrysz_ry6ypcsq","goodDescription":"11","goodType":"其他","goodSubType":"其他","goodRating":"一星","ruleDescription":"11","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"兑换码","costPrice":"11.00","marketPrice":"11.00","paperAmount":"11.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2023020000000001","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"如约中石油","sourceStore":"如约中石油","listPicUrl":"","rate":"1","tenantId":"null","createTime":"2023-03-08 10:24:30","creatorCode":"1567355933251457026","creatorName":"阿芷","modifyTime":"2023-03-20 10:00:38","modifierCode":"1567355933251457026","modifierName":"阿芷","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"如约科技","goodStoreMappingCount":605,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1636188895388979202","goodCode":"SG2023030000000011","goodName":"银联券0.02-0.01","thirdGoodCode":"200780","goodDescription":"银联券0.02-0.01","goodType":"虚拟类","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"1.00","marketPrice":"1.00","paperAmount":"1.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000015","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"银讯无门店无核销","sourceStore":"银联","listPicUrl":"http://fenle.oss-cn-beijing.aliyuncs.com/upload/20221026/bfae4274ab1e4fa79aadae2c8374987b.png","rate":"0","tenantId":"null","createTime":"2023-03-16 10:13:26","creatorCode":"1123598821738675201","creatorName":"admin","modifyTime":"2023-03-16 10:13:30","modifierCode":"1123598821738675201","modifierName":"admin","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"测试供方20221115","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1636187214819446786","goodCode":"SG2023030000000010","goodName":"银联券0.02-0.01","thirdGoodCode":"200780","goodDescription":"银联券0.02-0.01","goodType":"虚拟类","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"直充","costPrice":"1.00","marketPrice":"1.00","paperAmount":"1.00","hasOnShelf":"false","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2302000000000002","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"银讯无门店无核销","sourceStore":"银迅","listPicUrl":"","rate":"0","tenantId":"null","createTime":"2023-03-16 10:06:46","creatorCode":"1123598821738675201","creatorName":"admin","modifyTime":"2023-03-16 10:06:46","modifierCode":"1123598821738675201","modifierName":"admin","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"下架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"中卉测试供方","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"},{"id":"1607208649351782402","goodCode":"SG2022120000000042","goodName":"新疆哈密瓜","thirdGoodCode":"","goodDescription":"00","goodType":"实物类","goodSubType":"其他","goodRating":"一星","ruleDescription":"","goodSpec":"其他","goodSpecCode":"null","goodSubSpec":"其他","costPrice":"10.00","marketPrice":"10.00","paperAmount":"10.00","hasOnShelf":"true","hasForCommonStore":"true","hasInUserAccount":"true","hasMultiInOrder":"false","supplierCode":"SUP2022110000000015","codeGetType":"API","codeTradeType":"null","goodInterfaceSign":"测试20221115","sourceStore":"00","listPicUrl":"https://fenle.oss-cn-beijing.aliyuncs.com/upload/20221226/fe482c8b28f694bcb4e23ceea3b56d3c.jpg","rate":"0","tenantId":"null","createTime":"2022-12-26 10:56:17","creatorCode":"1587370429281832961","creatorName":"甘学俊","modifyTime":"2023-03-13 16:18:50","modifierCode":"1627853185430913025","modifierName":"吴中卉","hasDelete":"false","deleteTime":"null","remark":"null","settlementType":"1","hasOnShelfCn":"上架","hasForCommonStoreCn":"是","hasInUserAccountCn":"是","hasMultiInOrderCn":"否","supplierName":"测试供方20221115","goodStoreMappingCount":0,"thirdGoodLastUpdateTime":"null","listSupplierGoodStoreMapping":"null","listPsSupplierGoodMainPicOneToOne":"null","listPsSupplierGoodMainPicSixteenToNine":"null","listPsSupplierGoodDetailPic":"null","listPsSupplierGoodVideo":"null","listSupLicPic":"null"}],"total":227,"size":30,"current":1,"orders":[],"optimizeCountSql":"true","searchCount":"true","countId":"null","maxLimit":"null","pages":8},"msg":"操作成功"}
# # print(c['data']['records'])
# for i in c['data']['records']:
#      print(i['thirdGoodCode'])


def a():
     b = 1
     c = 2
     return b,c

print(a()[0])

