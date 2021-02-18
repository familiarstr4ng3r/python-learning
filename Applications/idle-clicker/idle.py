import time
import os
import win32gui
import keyboard
import mouse

from window import Window

def loop_action(window):
  shop = (125, 50)
  library = (250, 50)

  e1 = (100, 140)
  e2 = (100, 200)
  close = (600, 60)

  if keyboard.is_pressed("q"): window.click_at_relative(*e1)
  elif keyboard.is_pressed("w"): window.click_at_relative(*e2)
  elif keyboard.is_pressed("e"): window.click_at_relative(*close)
  elif keyboard.is_pressed("r"): window.set_position(100, 100)
  elif keyboard.is_pressed("t"): window.set_position(500, 500)
  elif keyboard.is_pressed("y"): window.activate()
  elif keyboard.is_pressed("m"):
    s, p = window.get_relative_position(*mouse.get_position())
    if s: print(p)
  elif keyboard.is_pressed("o"):
    hwnd = win32gui.GetForegroundWindow()
    print(hwnd, win32gui.GetWindowText(hwnd))

WINDOW_NAME = ""

def main():
  if not WINDOW_NAME:
    input("WINDOW_NAME is empty, please enter valid name! Press enter to exit")
    exit()
	
  window = Window(WINDOW_NAME)

  while True:
    #os.system("cls")
    loop_action(window)
    # r q e
    time.sleep(0.1)

main()
