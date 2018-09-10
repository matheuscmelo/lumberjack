import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from time import sleep
from gi.repository import Gdk
from pynput.keyboard import Key, Controller
import time

def screenshot():
    window = Gdk.get_default_root_window()
    x, y, width, height = window.get_geometry()
    pb = Gdk.pixbuf_get_from_window(window, 820, 180, 280, 520)
    pb.savev("screenshot.png", "png", (), ())

def get_right():
    screenshot()
    f = misc.imread('screenshot.png')
    return [x[170:270] for x in f[350:480]]

def get_left():
    f = misc.imread('screenshot.png')
    return [x[10:110] for x in f[350:480]]

def read_right():
    f = misc.imread('right.png')
    return f

def read_right_2():
    f = misc.imread('right_2.png')
    return f

def read_left_1():
    f = misc.imread('left_1.png')
    return f

def read_left_2():
    f = misc.imread('left_2.png')
    return f

def read_left_3():
    f = misc.imread('left.png')
    return f

def read_right_3():
    f = misc.imread('right_3.png')
    return f

def read_right_4():
    f = misc.imread('right_4.png')
    return f

def read_can_left_2():
    f = misc.imread('can_left_2.png')
    return f



keyboard = Controller()

# a = get_left()

# plt.imshow(a)
# plt.show()
# misc.imsave('can_left_2.png', a)

right = read_right()
right_2 = read_right_2()
right_3 = read_right_3()
right_4 = read_right_4()

left_1 = read_left_1()
left_2 = read_left_2()
left_3 = read_left_3()
left_4 = read_can_left_2()

sleep(5)
current_milli_time = lambda: int(round(time.time() * 1000))
while True:
    sleep_time = 0.08

    actual_right = get_right()
    actual_left = get_left()
    can_right = np.array_equal(right, actual_right)
    can_right_2 = np.array_equal(right_2, actual_right)
    cannot_left_1 = np.array_equal(left_1, actual_left)
    cannot_left_2 = np.array_equal(left_2, actual_left)
    can_left = np.array_equal(left_3, actual_left)
    cannot_right_1 = np.array_equal(right_3, actual_right)
    cannot_right_2 = np.array_equal(right_4, actual_right)
    can_left_2 = np.array_equal(left_4, actual_left)
    # if can_left or can_left_2:
    #     keyboard.press(Key.left)
    #     keyboard.release(Key.left)
    # else:
    #     keyboard.press(Key.right)
    #     keyboard.release(Key.right)
    # sleep(0.2)

    if (cannot_left_1 or cannot_left_2 or can_right or can_right_2) and not (cannot_right_1 or cannot_right_2):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    else:
        if can_left or can_left_2:
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        else:
            sleep_time = 0
        
    sleep(sleep_time)