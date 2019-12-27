#/Code/python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/28 16:58 
# @Author : ye
# @Site :  
# @File : 
# @Software: VS
import pyaudio 
import wave
import os
import sys
in_path = "/home/pi/mywork/test7/car/Source" # 存放录音的路径

def get_audio(filepath):
    
    aa = str(input("请按y开始控制车辆？   （y/n）"))
    if aa == str("y") :
        #os.close(sys.stderr.fileno())
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 5          # 录音时间
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*5, "recording...", "*"*5)
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("getting result from xfyun ...")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    else:
        print("语音录入失败，请重新开始")
        get_audio(in_path)
