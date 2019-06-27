import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
from time import sleep
from gi.repository import Gdk
from pynput.keyboard import Key, Controller, Listener
from os import listdir
from os.path import isfile, join

TRAIN = False


can_left_images = []
can_right_images = []

def screenshot():
    window = Gdk.get_default_root_window()
    pb = Gdk.pixbuf_get_from_window(window, 820, 180, 280, 520)
    pb.savev("screenshot.png", "png", (), ())

def get_right():
    f = misc.imread('screenshot.png')
    return [x[170:270] for x in f[300:360]]

def get_left():
    f = misc.imread('screenshot.png')
    return [x[10:110] for x in f[300:360]]

def read_right():
    global can_right_images
    can_right_images = [misc.imread(join('./can_right', f)) for f in listdir('./can_right') if isfile(join('./can_right', f))]

def read_left():
    global can_left_images
    can_left_images = [misc.imread(join('./can_left', f)) for f in listdir('./can_left') if isfile(join('./can_left', f))]

def turn_left():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def turn_right():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

def can_left(actual):
    global can_left_images
    for image in can_left_images:
        if np.array_equal(actual, image):
            return True
    return False

def can_right(actual):
    global can_right_images
    for image in can_right_images:
        if np.array_equal(actual, image):
            return True
    return False

keyboard = Controller()


c = 0
def on_press(key):
    global c
    screenshot()
    c += 1
    if key == Key.left:
        misc.imsave('can_left/left{}.png'.format(c), get_left())
    elif key == Key.right:
        misc.imsave('can_right/right{}.png'.format(c), get_right())


if TRAIN:
    with Listener(on_press=on_press) as listener:
        listener.join()



read_left()
read_right()

sleep(5)

sleep_time = 0.16


rest_left = []
rest_right = []
while True:
    screenshot()
    actual_right = get_right()
    actual_left = get_left()

    if can_right(actual_right):
        turn_right()
        if rest_right:
            can_right_images += rest_right
            rest_left = []
            rest_right = []
    elif can_left(actual_left):
        turn_left()
        if rest_left:
            can_left_images += rest_left
            rest_left = []
            rest_right = []
    else:
        rest_left.append(actual_left)
        rest_right.append(actual_right)
        
    sleep(sleep_time)
