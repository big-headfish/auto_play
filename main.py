# -*- coding: utf-8 -*-
##########################
####    程序入口      ####
##########################


from typing import Tuple
import util
import constant as c
import time
import auto
import os
import argparse


# _*_ coding:UTF-8 _*_  
import win32con
import ctypes
import ctypes.wintypes
import threading


RUN=False #用来传递运行一次的参数
EXIT = False #用来传递退出的参数
user32 = ctypes.windll.user32  #加载user32.dll
id1=105 #注册热键的唯一id，用来区分热键
id2=106
id3=107

### 脚本运行标识
PLAY=False

class Hotkey(threading.Thread):  #创建一个Thread.threading的扩展类  

    def run(self):  
        global EXIT  #定义全局变量，这个可以在不同线程间共用。
        global RUN  #定义全局变量，这个可以在不同线程间共用。

        if not user32.RegisterHotKey(None, id1, 0, win32con.VK_F9):   # 注册快捷键F9并判断是否成功，该热键用于执行一次需要执行的内容。  
            print ("Unable to register id"), id1 # 返回一个错误信息

        if not user32.RegisterHotKey(None, id2, 0, win32con.VK_F10):   # 注册快捷键F10并判断是否成功，该热键用于暫停程序，且最好这么结束，否则影响下一次注册热键。  
            print ("Unable to register id"), id2
        if not user32.RegisterHotKey(None, id3, 0, win32con.VK_F11):   # 注册快捷键F10并判断是否成功，该热键用于结束程序，且最好这么结束，否则影响下一次注册热键。  
            print ("Unable to register id"), id3    

        #以下为检测热键是否被按下，并在最后释放快捷键  
        try:  
            msg = ctypes.wintypes.MSG()  

            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:

                    if msg.message == win32con.WM_HOTKEY:  
                        if msg.wParam == id1:
                            print('运行')
                            RUN = True
                            EXIT=False
                        elif msg.wParam == id2:
                            print('暂停')
                            RUN=False
                        elif msg.wParam == id3:
                            print('退出')
                            EXIT=True
                            return    


                    user32.TranslateMessage(ctypes.byref(msg))  
                    user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            user32.UnregisterHotKey(None, id1)#必须得释放热键，否则下次就会注册失败，所以当程序异常退出，没有释放热键，
                                              #那么下次很可能就没办法注册成功了，这时可以换一个热键测试
            user32.UnregisterHotKey(None, id2)
            user32.UnregisterHotKey(None, id3)


hotkey = Hotkey()  
hotkey.start()  




### 测试用
def test():
    util.log_h1(f'测试')
    auto.open_driver()
    while(True):
        auto.move_to(500,500)
        auto.test_left_mouse()
        time.sleep(3)
        

### 连点器
def liandian():
    while(True):
        auto.test_left_mouse() 
        time.sleep(0.02)


### 循环脚本
def auto_play():
    global PLAY
    global RUN
    global EXIT
    print("运行1")
    auto.open_driver()
    time.sleep(2)
    i = 0
    auto.default_key()
    while(True):
        if EXIT==True:
            return
        play_time = '运行第' + str(i) + '次'
        print(play_time)
        time.sleep(1)
        if(int(i)%2 == 0):
            if EXIT==True:
                return
            if(i%12 == 0):
                auto.auto_buff()  
            if(i%4 == 0):
                auto.auto_60()
            print('向右')
            for j in range(10):
                auto.auto_right()
                if EXIT==True:
                    return
        else:
            if EXIT==True:
                return
            print('向左')
            for j in range(10):
                auto.auto_left()
                if EXIT==True:
                    return
        i = i + 1


### 热键启动
def hot_run():
    print("F9启动,F10暂停")
    global RUN
    global EXIT
    global PLAY
    while(True):
        time.sleep(1)
        if RUN==True:
            auto_play()
        elif EXIT==True:
            #这里是用于退出循环的
            return      


### 龙神
def longshen_run():
    global RUN
    global EXIT
    global PLAY
    print("运行1")
    auto.open_driver()
    time.sleep(2)
    i = 0
    auto.default_key()
    print("F9启动,F10暂停")
    while(True):
        time.sleep(1)
        if RUN==True:
            play_time = '运行第' + str(i) + '次'
            print(play_time)
            auto.auto_q_s()
            time.sleep(1)
            i = i + 1
        elif EXIT==True:
            #这里是用于退出循环的
            return


parser = argparse.ArgumentParser()

parser.add_argument("--click", help="Auto Click", type=int)
parser.add_argument("--learn", help="Lean Clean", type=int)

args = parser.parse_args()

# if args.click:
#     auto_click()

# if args.learn:
#     move_learn()


# if __name__ == '__main__':
#     print('Bye~')
## 运行
# auto_click()
## 训练
# dm.base()
# liandian()
# auto_play()
# hot_run()
longshen_run()