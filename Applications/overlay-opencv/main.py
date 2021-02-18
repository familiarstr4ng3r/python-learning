import keyboard
import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
import googletrans
import win32ui
import win32gui
import win32con

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
translator = googletrans.Translator()

red = (0, 0, 255)
window_name = "Overlay"
rect = (0, 0, 1300, 700)

screen = None
down_pos = None
up_pos = None

def mouse_event(event, x, y, flags, param):
  global screen, down_pos, up_pos

  if event == cv2.EVENT_LBUTTONDOWN:
    #print("L_DOWN", x, y)
    down_pos = (x, y)
  elif event == cv2.EVENT_LBUTTONUP:
    #print("L_UP", x, y)
    up_pos = (x, y)
    #size = tuple(np.subtract(down_pos, up_pos))
    #size = tuple([abs(value) for value in size])
    
    top_left = (min(down_pos[0], up_pos[0]), min(down_pos[1], up_pos[1]))
    bottom_right = (max(down_pos[0], up_pos[0]), max(down_pos[1], up_pos[1]))

    def clamp(v):
      return 0 if v < 0 else v

    top_left = tuple([clamp(value) for value in top_left])
    x, y = top_left
    
    size = tuple(np.subtract(top_left, bottom_right))
    size = tuple([abs(value) for value in size])

    w, h = size
    roi = screen[y:y+h, x:x+w]
    try:
      #cv2.imshow("window_name", roi)
      text = pytesseract.image_to_string(roi, lang="eng")
      text = text.strip()
      success = len(text) > 0
	  
      confirm = win32ui.MessageBox(text, "Press OK to translate", win32con.MB_YESNO)
      
      if confirm == win32con.IDYES:
        if not success: text = "Undefined"
        else: text = translator.translate(text, dest="ru").text

        #print(text)
        win32ui.MessageBox(text, "Cucumber")

      # ! https://www.youtube.com/watch?v=2WR3wMt6V2k
      #cv2.displayOverlay(window_name, text, 3000)
      #cv2.displayStatusBar(window_name, text, 3000)

      # ! OpenCV(4.4.0) C:\Users\appveyor\AppData\Local\Temp\1\pip-req-build-cff9bdsm\opencv\modules\highgui\src\window.cpp:567: error: (-213:The function/feature is not implemented) The library is compiled without QT support in function 'cv::displayStatusBar'

    except Exception as e:
      print(e)

  elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
    #print("L_MOVE")
    up_pos = (x, y)
    clone = screen.copy()
    cv2.rectangle(clone, down_pos, up_pos, red, 1)
    cv2.imshow(window_name, clone)

def update_style(hwnd):
  # ! https://answers.opencv.org/question/33681/to-remove-opencv-title-bar/
  style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
  style &= ~win32con.WS_OVERLAPPEDWINDOW
  style |= win32con.WS_POPUP
  win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE , style)
  win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, rect[2], rect[3], 0)

def show_window():

  global screen
  screen = np.array(ImageGrab.grab(rect))
  #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
  cv2.imshow(window_name, screen)
  #cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, cv2.WINDOW_FULLSCREEN)
  #cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, cv2.WINDOW_NORMAL)
  cv2.setMouseCallback(window_name, mouse_event)

  # ! http://www.noah.org/wiki/OpenCV_display_window_on_top_with_focus
  #cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
  #cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

  hwnd = win32gui.FindWindow(None, window_name)
  update_style(hwnd)
  #win32gui.ShowWindow(hwnd, 5)
  #win32gui.SetForegroundWindow(hwnd)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

def loop_action():
  while True:
    if keyboard.is_pressed("p"):
      #cv2.destroyAllWindows()
      show_window()

def main():
  try:
    #show_window()
    #keyboard.add_hotkey("ctrl+shift+u", show_window)
    loop_action()
  except KeyboardInterrupt as e:
    print("Type:", type(e))

main()
