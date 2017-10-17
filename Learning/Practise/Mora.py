# -*- coding: UTF-8 -*-
'''
一个关于石头剪刀布的小游戏
'''
import random

while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "Stone"
    elif s == 2:
        ind = "Scissors"
    elif s == 3:
        ind = "Doth"
        
    m = raw_input('输入Stone、Scissors、Doth进行游戏,输入end结束游戏: ')
    blist = ["Stone", "Scissors", "Doth"]
    
    if (m not in blist) and (m != 'end'):
        print "输入错误，请重新输入！"
    elif (m not in blist) and (m == 'end'):
        print "\n游戏退出中..."
        break
    elif m == ind :
        print "电脑出了： " + ind + "，平局！"
    elif (m == 'Stone' and ind == 'Scissors') or (m == 'Scissors' and ind == 'Doth') or (m == 'Doth' and ind == 'Stone'):
        print "电脑出了： " + ind +"，你赢了！"
    elif (m == 'Stone' and ind == 'Doth') or (m == 'Scissors' and ind == 'Stone') or (m == 'Doth' and ind == 'Scissors'):
        print "电脑出了： " + ind +"，你输了！"
