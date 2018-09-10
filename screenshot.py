from gi.repository import Gdk
import time

def screenshot():
    window = Gdk.get_default_root_window()
    x, y, width, height = window.get_geometry()


    pb = Gdk.pixbuf_get_from_window(window, 820, 180, 280, 520)
    writing = True
    pb.savev("screenshot.png", "png", (), ())
    writing = False

if __name__ == "__main__":
    while True:
        current_milli_time = lambda: int(round(time.time() * 1000))
        a = current_milli_time()
        screenshot()
        b = current_milli_time()
        print (b - a)