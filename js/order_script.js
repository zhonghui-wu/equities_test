// 获取环境变量
const env = pm.environment;
// 获取全局变量
const globalVar = pm.globals;
// 获取临时变量
const temp = pm.variables;
// 引用内置js库
const cryptoJs = require("crypto-js");

/**
 * 订单下单
 */
function saveOrder() {

    // 1.初始化必填参数
    const initObj = initParam();
    // 2.校验参数
    validParams(initObj);
    // 3.定义访问token的url
    const subUrl = '/get-token';
    // 4.生成获取token的请求体
    const bodyStr = JSON.stringify({ "appKey": initObj.appKey });
    // 5.生成sign
    const tokenSign = genSign(initObj, bodyStr);
    // 6.设置获取token的请求头
    let header = {
        "Authorization": initObj.authorization,
        "clientId": initObj.clientId,
        "appKey": initObj.appKey,
        "timeStamp": initObj.timeStamp,
        "sign": tokenSign
    }
    // 7.构造token请求数据
    const requestParam = genPostRequestParam(subUrl, header, bodyStr);
    console.log("获取token请求体数据: " + JSON.stringify(requestParam));

    // 8.异步发送请求获取token
    pm.sendRequest(requestParam, function (err, resp) {
        if (err) {
            throw new Error("获取token发生异常" + JSON.stringify(err));
        }
        if (resp) {
            if (resp.json().status === 1) {
                console.log("获取token成功: " + JSON.stringify(resp.json()));
                let token = resp.json().data.accessToken;
                setSaveOrderRequestParams(initObj, token);
                // setSaveOrderRequestParams2(initObj, token);
            } else {
                throw new Error("获取token失败: " + JSON.stringify(resp.json()));
            }
        }
    });

};

/**
* 设置下单请求数据
* 包括请求头、请求体
*/
function setSaveOrderRequestParams(initObj, accessToken) {
    // 1.获取请求体内容
    let bodyStr = pm.request.body.raw;
    let body = JSON.parse(bodyStr);
    body.accessToken = accessToken;
    body.orderMobile = aesEncry(body.orderMobile);
    body.orderPersonName = aesEncry(body.orderPersonName);
    body.thirdOrderCode = "TEST".concat(dateFormat(new Date())).concat(Math.round(Math.random() * 10000));
    bodyStr = JSON.stringify(body);
    console.log("下单请求体数据: " + bodyStr);
    // 2.更新请求体
    setBody(bodyStr);
    // 3.生成sign
    const sign = genSign(initObj, bodyStr);
    // 4.设置请求头
    setHeaders(initObj, sign);
}

function dateFormat (date) {
    let y = date.getFullYear();
    let m = date.getMonth() + 1;
    m = m < 10 ? ('0' + m) : m;
    let d = date.getDate();
    d = d < 10 ? ('0' + d) : d;
    let h = date.getHours();
    h = h < 10 ? ('0' + h) : h;
    let minute = date.getMinutes();
    minute = minute < 10 ? ('0' + minute) : minute;
    let second = date.getSeconds();
    second = second < 10 ? ('0' + second) : second;

    return new String(y).concat(m).concat(d).concat(h).concat(minute).concat(second);
}

/**
 * 提供测试使用
 */
function setSaveOrderRequestParams2(initObj, accessToken) {
    // 1.获取请求体内容
    let bodyStr = pm.request.body.raw;
    let body = JSON.parse(bodyStr);
    body.accessToken = accessToken;
    body.orderMobile = aesEncry(body.orderMobile);
    body.orderPersonName = aesEncry(body.orderPersonName);
    body.thirdOrderCode = pm.variables.get("thirdOrderCode");
    console.log("第三方订单号:", body.thirdOrderCode);
    bodyStr = JSON.stringify(body);
    console.log("下单请求体数据: " + bodyStr);
    // 2.更新请求体
    setBody(bodyStr);
    // 3.生成sign
    const sign = genSign(initObj, bodyStr);
    // 4.设置请求头
    setHeaders(initObj, sign);
}

/**
 * 生成post提交的访问数据
 * (包括请求头地址、请求头、请求体)
 */
const genPostRequestParam = (subUrl, header, bodyStr) => {
    const url = env.get('BASE_URL') + subUrl;
    console.log("获取token请求url: " + url);
    header["Content-Type"] = "application/json";

    // 可以设置根据当前请求类型使用动态数据格式封装
    let reuestParams = {
        url: url,
        method: 'POST',
        header: header,
        body: {
            mode: 'raw',
            raw: bodyStr
        }
    };

    return reuestParams;
}

/**
 * 设置请求体数据
 */
function setBody(bodyStr) {
    pm.request.body.update(bodyStr);
}

/**
 * 设置请求头
 */
function setHeaders(initObj, sign) {

    pm.request.headers.upsert({
        key: "Authorization",
        value: initObj.authorization
    });

    pm.request.headers.upsert({
        key: "clientId",
        value: initObj.clientId
    });

    pm.request.headers.upsert({
        key: "appKey",
        value: initObj.appKey
    });

    pm.request.headers.upsert({
        key: "timeStamp",
        value: initObj.timeStamp
    });

    pm.request.headers.upsert({
        key: "sign",
        value: sign
    });
}

/**
 * 生成sign
 */
function genSign(initObj, bodyStr) {

    const splChar = ":";
    const arr = [initObj.clientId, initObj.appKey, bodyStr, initObj.timeStamp, initObj.appSecret];
    let preSign = arr.join(splChar);
    console.log("加密前sign字符串: " + preSign);
    const sufSign = cryptoJs.MD5(preSign).toString();
    console.log("加密后sign字符串: " + sufSign);
    return sufSign;
}

/**
 * 校验必要参数
 */
function validParams(initObj) {

    const active = getActive();
    const acEnum = activeEnum.getByCode(active);

    if (isNullOrUndefined(initObj)) {
        throw new Error("请在[" + acEnum.desc + "]环境中设置: Authorization、clientId、appKey、appSecret变量");
    }

    if (isNullOrUndefined(initObj.authorization)) {
        throw new Error("请在" + acEnum.desc + "环境设置Authorization变量");
    }

    if (isNullOrUndefined(initObj.clientId)) {
        throw new Error("请在" + acEnum.desc + "环境设置clientId变量");
    }

    if (isNullOrUndefined(initObj.appKey)) {
        throw new Error("请在" + acEnum.desc + "环境设置appKey变量");
    }

    if (isNullOrUndefined(initObj.appSecret)) {
        throw new Error("请在" + acEnum.desc + "环境设置appSecret变量");
    }

    if (isNullOrUndefined(initObj.timeStamp)) {
        throw new Error("脚本无法获取tiemStamp当前时间戳变量");
    }

    console.log("校验必填参数成功");
}

/**
 * 初始化必填参数
 */
function initParam() {

    // 必填参数对象
    let initObj = {};
    // 获取参数的环境
    let getParamActive;
    // 获取当前变量环境
    let paramActive = getActive();
    // 默认环境请求头

    if (isNullOrUndefined(paramActive)) {
        // throw new Error("请在全局变量添加键名为active,值为header、local、global");
        paramActive = 'header';
    }

    switch (paramActive.toLowerCase()) {
        case 'header':
            getParamActive = pm.request.headers;
            break;
        case 'local':
            getParamActive = pm.environment;
            break;
        case 'global':
            getParamActive = pm.globals;
            break;
        default:
            console.log("全局变量active设置了非法参数");
            throw new Error("全局变量active设置了非法参数");
    }

    initObj.authorization = getParamActive.get("Authorization");
    initObj.clientId = getParamActive.get("clientId");
    initObj.appKey = getParamActive.get("appKey");
    initObj.appSecret = getParamActive.get("appSecret");
    initObj.timeStamp = String(Date.now());

    return initObj;
}

/**
 * 判断变量是否为空
 */
function isNullOrUndefined(obj) {
    return obj === null || obj === undefined || obj === 'undefined' || obj === '';
}

/**
 * 获取当前变量存放的环境
 */
function getActive() {
    return String(globalVar.get("active"));
}

/**
 * 定义环境枚举变量
 */
let activeEnum = {

    UN_KNOW: { code: 'unknow', desc: '未设置环境' },
    HEADER: { code: 'header', desc: '请求头' },
    LOCAL: { code: 'local', desc: '环境变量' },
    GLOBAL: { code: 'global', desc: '全局变量' },

    getByCode: function (code) {
        for (let key in activeEnum) {
            if (code == activeEnum[key].code) {
                return activeEnum[key];
            }
        }
        return activeEnum.UN_KNOW;
    }
}

/**
 * AES加密
 */
function aesEncry(words) {

    // 开放平台加密key
    const secret = "h2wGC4pNGzWYgiEW";

    if (isNullOrUndefined(words)) {
        return;
    }
    const key = cryptoJs.enc.Utf8.parse(secret);
    const srcs = cryptoJs.enc.Utf8.parse(words);
    const encrypted = cryptoJs.AES.encrypt(srcs, key, { mode: cryptoJs.mode.ECB, padding: cryptoJs.pad.Pkcs7 });
    return encrypted.toString();
}

// 调用下单方法
saveOrder();