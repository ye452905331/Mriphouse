#/Code/python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/28 16:58 
# @Author : ye
# @Site :  
# @File : 
# @Software: VS
import websocket
import requests
import datetime
import hashlib
import base64
import hmac
import json
import os, sys
import re
from urllib.parse import urlencode
import logging
import time
import ssl
import wave
from jsonpath_rw import jsonpath,parse
from jsonpath_rw_ext import parser
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
from pyaudio import PyAudio,paInt16
from audio_input import get_audio # 导入录音.py文件

input_filename = "input.wav"               # 麦克风采集的语音输入
input_filepath = "./audios/"              # 输入文件的path
in_path = input_filepath + input_filename

type = sys.getfilesystemencoding()

path_pwd = os.path.split(os.path.realpath(__file__))[0]
os.chdir(path_pwd)

try:
    import thread
except ImportError:
    import _thread as thread

logging.basicConfig()

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识

framerate = 8000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 2

myappid = '5dfb1838'
myappsecret = '429a0fff6ba84729d072cf927f23016b'
myappkey ='152f4464c3cfbba4dcc65fd213e903c3'
myresult = ''

class Ws_Param(object):
    # 初始化
    def __init__(self, host):
        self.Host = host
        self.HttpProto = "HTTP/1.1"
        self.HttpMethod = "GET"
        self.RequestUri = "/v2/iat"
        self.APPID = myappid # 在控制台-我的应用-语音听写（流式版）获取APPID
        self.Algorithm = "hmac-sha256"
        self.url = "wss://" + self.Host + self.RequestUri



        # 设置测试音频文件，流式听写一次最多支持60s，超过60s会引起超时等错误。
        self.AudioFile = r"/home/pi/mywork/test7/car/Source/input.wav"

        self.CommonArgs = {"app_id": self.APPID}
        self.BusinessArgs = {"domain":"iat", "language": "zh_cn","accent":"mandarin"}

    def create_url(self):
        url = 'wss://ws-api.xfyun.cn/v2/iat'
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        APIKey = myappkey # 在控制台-我的应用-语音听写（流式版）获取APIKey
        APISecret = myappsecret # 在控制台-我的应用-语音听写（流式版）获取APISecret

        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/iat " + "HTTP/1.1"
        signature_sha = hmac.new(APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        url = url + '?' + urlencode(v)
        return url
wsParam = Ws_Param("ws-api.xfyun.cn") #流式听写 域名
# 收到websocket消息的处理 这里我对json解析进行了一些更改 打印简短的一些信息
def on_message(ws, message):
    msg = json.loads(message) # 将json对象转换为python对象 json格式转换为字典格式
    global myresult
    try:
        code = msg["code"]
        sid = msg["sid"]

        if code != 0:
            errMsg = msg["message"]
            print("sid:%s call error:%s code is:%s\n" % (sid, errMsg, code))
        else:
            result = msg["data"]["result"]["ws"][0]
            
            #msg_json = json.dumps(result)
            print('jsonpath',msg)
            s = parse("$..w").find(msg)
            s = [match.value for match in s]
            #myresult = myresult + i
            for i in s:
                myresult = myresult + i
            #print('wod:',myresult) 
            #return(myresult)

    except Exception as e:
        print("receive msg,but parse exception:", e)

# 收到websocket错误的处理
def on_error(ws, error):
    print("### error:", error)

# 收到websocket关闭的处理
def on_close(ws):
    print("")

# 收到websocket连接建立的处理
def on_open(ws):
    def run(*args):
        frameSize = 1280  # 每一帧的音频大小
        intervel = 0.04  # 发送音频间隔(单位:s)
        status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧
        with open(wsParam.AudioFile, "rb") as fp:
            while True:
                buf = fp.read(frameSize)

                # 文件结束
                if not buf:
                    status = STATUS_LAST_FRAME
                # 第一帧处理
                # 发送第一帧音频，带business 参数
                # appid 必须带上，只需第一帧发送
                if status == STATUS_FIRST_FRAME:

                    d = {"common": wsParam.CommonArgs,
                         "business": wsParam.BusinessArgs,
                         "data": {"status": 0, "format": "audio/L16;rate=16000",
                                   "audio": str(base64.b64encode(buf),'utf-8'),
                                  "encoding": "raw"}}
                    d = json.dumps(d)
                    ws.send(d)
                    status = STATUS_CONTINUE_FRAME
                # 中间帧处理
                elif status == STATUS_CONTINUE_FRAME:
                    d = {"data": {"status": 1, "format": "audio/L16;rate=16000",
                                   "audio": str(base64.b64encode(buf),'utf-8'),
                                  "encoding": "raw"}}
                    ws.send(json.dumps(d))
                # 最后一帧处理
                elif status == STATUS_LAST_FRAME:
                    d = {"data": {"status": 2, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf),'utf-8'),
                                  "encoding": "raw"}}
                    ws.send(json.dumps(d))
                    time.sleep(1)
                    break
                # 模拟音频采样间隔
                time.sleep(intervel)
        ws.close()

    thread.start_new_thread(run, ())

def xfyu_audiohadle():
    # 采集音频 录音
    global myresult
    get_audio("input.wav")
    myresult = ''
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()#创建URL
    #合成PUSH的URL
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    return(myresult)#返回文本



    

