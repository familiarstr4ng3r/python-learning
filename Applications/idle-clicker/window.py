import win32gui
import win32con
import mouse

class Window:
  def __init__(self, name):
    self.name = name

  def is_active(self):
    hwnd = win32gui.FindWindow(None, self.name)

    if hwnd > 0: return True, hwnd
    else: return False, None
  
  # x, y - relitive position to window
  def get_absolute_position(self, x, y):
    success, hwnd = self.is_active()
    if success:
      rect = win32gui.GetWindowRect(hwnd)
      rx, ry, rw, rh = rect
      
      abs_x = rx + x
      abs_y = ry + y
      return True, (abs_x, abs_y)
    else:
      return False, None

  # x, y - absolute position on screen
  def get_relative_position(self, x, y):
    success, hwnd = self.is_active()
    if success:
      rect = win32gui.GetWindowRect(hwnd)
      rx, ry, rw, rh = rect
      
      rel_x = x - rx
      rel_y = y - ry
      return True, (rel_x, rel_y)
    else:
      return False, None

  def click_at_relative(self, x, y):
    success, (x, y) = self.get_absolute_position(x, y)
    
    if success: 
      mouse.move(x, y)
      mouse.click("left")

  # x, y - absolute position on screen
  def set_position(self, x, y):
    success, hwnd = self.is_active()
    if success:
      flags = win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW
      win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, 0, 0, flags)

  def activate(self):
    success, hwnd = self.is_active()
    if success:
      result = win32gui.BringWindowToTop(hwnd)
      #result = win32gui.ShowWindow(hwnd, win32con.SW_SHOWDEFAULT)
      print(result)

      # win32gui.SetActiveWindow(hwnd)
      # result = win32gui.ShowWindow(hwnd, True)
      # print(result)

      # ! win32gui.SetFocus(hwnd)
      #win32gui.SetForegroundWindow(hwnd)
