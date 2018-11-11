# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:37:45 2018

@author: Administrator
"""

"""
方法功能：实现字符串反转
输入参数：ch:字符数组 front与end:待交换子字符串的首尾下标
"""
def reverseStr(ch,front,end):
    while  front<end:
        ch[front]=chr(ord(ch[front])^ord(ch[end]))
        ch[end]=chr(ord(ch[front])^ord(ch[end]))
        ch[front]=chr(ord(ch[front])^ord(ch[end]))
        front +=1
        end -=1

# 反转字符串中的单词 
def swapWords(str):
    # 对整个字符串进行字符反转操作
    lens=len(str)
    ch=list(str)
    reverseStr(ch, 0, lens - 1)
    begin = 0  
    # 对每个单词进行字符反转操作
    i=1
    while  i<lens:
        if  ch[i] == ' ':
            reverseStr(ch, begin, i - 1)  
            begin = i + 1 
        i +=1
    #reverse_str(ch, begin, lens - 1)  #修改
    reverseStr(ch, begin, lens - 1)  #修改
    return  ''.join(ch)

if  __name__=="__main__":
    str="how are you"
    print  "字符串"+str+"翻转后为：",
    print  swapWords(str)
