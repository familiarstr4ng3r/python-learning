import mouse
from time import sleep

isPressed = False

print("Start")
#3.6.53
while True:
	#if mouse.is_pressed(button = 'right'):
	#	print("Executed")
	#	while True:
	#		sleep(0.1)
	#		mouse.double_click(button = 'left')
	
	if (mouse.is_pressed(button = 'middle')):
		#isPressed = not isPressed
		#print(isPressed)
		mouse.click(button = 'left')
		sleep(0.05)
		
	#if (mouse.is_pressed(button = 'middle')):
	#	print("Stop")
	#	break
	
	#if (isPressed):
	#	sleep(0.5)
	#	print("Clicked")
	
	#if mouse.is_pressed(button = 'right'):
		#isPressed = True