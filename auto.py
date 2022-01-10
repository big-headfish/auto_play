# -*- coding: utf-8 -*-
##########################
####    键鼠包装   ####
##########################

# import pyautogui
import random
from util import log_title as t
import time
import keymouse as km

# pyautogui.PAUSE = random.random()/3
# pyautogui.FAILSAFE = False           # 启用自动防故障功能


def open_driver():
    km.load_driver()
    
def move_to_click(x,y):
    t('绝对移动 点击')
    move_to(x,y)
    time.sleep(random.random()/21)
    km._left_button_down()
    # time.sleep(random.random()/5)
    time.sleep(50)
    km._left_button_up()

def move_rel_click(x,y):
    t('相对移动 点击')
    move_rel(x,y)
    time.sleep(random.random()/20)
    km._left_button_down()
    time.sleep(random.random()/5)
    km._left_button_up()


def move_to(x,y):
    print(f'move to - > {(x,y)}')
    # pyautogui.moveTo(x,y,duration=random.random()/2)

def move_rel(x,y):
    print(f'move rel - > {(x,y)}')
    # pyautogui.moveRel(x,y,duration=random.random()/2)

## 测试
def test_left_mouse():
    km._left_button_down()
    time.sleep(random.random()/5)
    km._left_button_up()

## 自动秒
def alt_q():
    km._key_down("alt")
    km._key_down("q")
    time.sleep(0.05 + random.random()/ 1000)
    km._key_down("a")
    km._key_up("q")
    km._key_up("a")
    km._key_up("alt")

### 产生随机数 秒数
def random_num(num):
    return num*random.random()


### 按键触发 防止第一次按下不响应
def default_key():
    print('按键测试')
    km._key_down("left_arrow")
    km._key_up("left_arrow")
    time.sleep(0.1)
    km._key_down('right_arrow')
    km._key_up("right_arrow")
    time.sleep(0.1)
    km._key_down("a")
    km._key_up("a")
    time.sleep(0.1)
    km._key_down("shift")
    km._key_up("shift")

### buff区
def auto_buff():
    km._key_down('v')
    km._key_up('v')
    time.sleep(3)


### 自定义按键
def auto_60():
    km._key_down('ins')
    km._key_up('ins')
    time.sleep(2)

### 自动刷图 向左
def auto_left():
    print('攻击')
    km._key_down("left_arrow")
    km._key_down("a")
    time.sleep(0.35 + random_num(0.05))
    km._key_up("a")
    km._key_down("shift")
    time.sleep(0.15 + random_num(0.05))
    km._key_up("shift")
    km._key_up("left_arrow")
    time.sleep(0.15 + random_num(0.05))

### 向右
def auto_right():
    print('攻击')
    km._key_down('right_arrow')
    km._key_down("a")
    time.sleep(0.35 + random_num(0.05))
    km._key_up("a")
    km._key_down("shift")
    time.sleep(0.15 + random_num(0.05))
    km._key_up("shift")
    km._key_up("right_arrow")
    time.sleep(0.15 + random_num(0.05))

### 自动刷图 pyautogui
# def auto_a2():
#     pyautogui.keyDown('a')
#     time.sleep(0.4)
#     pyautogui.keyUp('a')
#     pyautogui.keyDown('shift')
#     time.sleep(0.2)
#     pyautogui.keyUp('shift')

### 压下←  
def left_down():
    km._key_down('left_arrow')

### 抬起←
def left_up():
    km._key_up('left_arrow')

### 压下→
def right_down():
    km._key_down('right_arrow')

### 抬起→
def right_up():
    km._key_up('right_arrow')


    
	

if __name__ == '__main__':
    print('加载键盘')
    open_driver()
    # move_to_click(341,437)