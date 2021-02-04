import cv2
import numpy as np
from PIL import ImageGrab
import win32con
import win32gui

# http://timgolden.me.uk/pywin32-docs/win32gui.html
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow
# https://docs.opencv.org/3.4/d7/dfc/group__highgui.html

# https://stackoverflow.com/questions/29458775/tkinter-see-through-window-not-affected-by-mouse-clicks


def update_style(hwnd):
  lExStyle = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
  lExStyle |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
  win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE , lExStyle)

def cv_main():
  window_name = "Overlay Window"
  cv2.namedWindow(window_name)
  cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, cv2.WINDOW_FULLSCREEN)

  hwnd = win32gui.FindWindow(None, window_name)

  #update_style(hwnd)
  capture_screen(window_name)

def capture_screen(window_name):
  rect = (0, 0, 300, 200)

  while True:
    screen = np.array(ImageGrab.grab(rect))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
    cv2.imshow(window_name, screen)

    key = cv2.waitKey(20)
    if key == ord("q"):
      break
    elif key == ord("w"):
      #win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
      #win32gui.CloseWindow(hwnd)
      print("closed")

  cv2.destroyAllWindows()
  
if __name__ == "__main__":
  cv_main()