#/Code/python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/28 16:58 
# @Author : ye
# @Site :  
# @File : 
# @Software: VS

import sys
import re


def car_ctlMatch(xfyunword):
    #名词词性
    Nounlist = ['尾箱','门','全','所有'] 
    #方向词性
    Dirlist = ['前','后','左','右']
    #动作词性
    Verlist = ['开','关']
    cthing = '无'
    ccmd = '无'
    #word = '开一下'
    word = xfyunword
    for keyn in Nounlist:
        pattern = '.*' + keyn + '.*'
        obj = re.findall(pattern, word)#正则模糊提取
        if len(obj)>0:
            cthing = keyn
    
    for keyd in Dirlist:
        pattern = '.*' + keyd + '.*'
        obj = re.findall(pattern, word)#正则模糊提取
        if len(obj)>0:
            cthing = keyd + cthing

    for keyv in Verlist:
        pattern = '.*' + keyv + '.*'
        obj = re.findall(pattern, word)#正则模糊提取
        if len(obj)>0:
            ccmd = keyv

    #print('cthing',cthing)
    #print('ccmd',ccmd)
    return(cthing,ccmd)#返回动作ccmd和控制设备cthing

'''
if __name__ == '__main__':
	fuzzyMatch('a')
'''