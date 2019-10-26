# coding: utf-8
# 获取token
import base64
import hmac
import json
import time

accessKey = "vt8x29atXIyGm8p0-sIgEekReiwO_ESQE3uRHM3w"
secretKey = "7G4LeXeBD5GwPMU1SLm7tZsasUs26Bc1wubcaWPx"

def get_token(bucket, filename=None, expires=3600):
    # 1、构建上次要素
    if filename:
        scope = "{}:{}".format(bucket, filename)
    else:
        scope = bucket
    # deadline = int(time.time()) + expires
    deadline = 1572076071

    policy = {
        "scope": scope,
        "deadline": deadline
    }
    # 2、转换为json字符串
    jsonPolicy = json.dumps(policy)
    # 3、对json字符串进行base64编码
    encodedPutPolicy = base64.urlsafe_b64encode(jsonPolicy.encode('utf-8'))
    # 4、使用HMAC-SHA1签名生成sign
    sign = hmac.new(secretKey.encode('utf-8'), encodedPutPolicy , 'sha1').digest()
    # 5、对签名进行base64编码
    encodedSign = base64.urlsafe_b64encode(sign)
    # 6、将accessKey，encodedSign，encodedPutPolicy 用英文符号:拼接起来
    token = "{}:{}:{}".format(accessKey, encodedSign .decode('utf-8'), encodedPutPolicy .decode('utf-8'))
    return token

def put_file():
    pass


if __name__ == "__main__":
    token = get_token('xcf_upload')
    print(token)