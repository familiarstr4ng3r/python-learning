import time
import mouse
import keyboard

# ! http://cpstest.org/5-seconds.php

keys = ["q", "w"]

cps = 30
user = input(f"Enter click per seconds (default is {cps}): ")

if user: cps = int(user)

delay = 1 / cps

print(f"App is running: {cps}")

while True:
  isPressed = False

  for k in keys:
    if keyboard.is_pressed(k):
      isPressed = True
      break

  if isPressed:
    mouse.click("left")
    time.sleep(delay)
  else:
    time.sleep(0.1)


input("Smth:")
  