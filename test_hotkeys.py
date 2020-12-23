from time import sleep
import pyautogui        # DOC: https://pypi.org/project/PyAutoGUI/

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen.
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
print(f"Screen size: {screenWidth}x{screenHeight}") # T440p => 1366x768

# Waiting to user confirm start
text_confim = pyautogui.confirm("Start proces? \n 1. Connect to WiFi Camera. \n 2. Prepare RisingView \n 3. Select Camera on RisingView")
if text_confim == 'Cancel':
    print("User cancel the procesing")
    exit(0)

# Open Rising Software
#position_bar = pyautogui.position()
#print(f"position: {position_bar}")
pyautogui.click(319,746)

# Test photo and save
print("Capturing image")
pyautogui.press('f8')
# Move to center screen
pyautogui.move(672,504)

print("Saving image")
#pyautogui.hotkey('ctrl','s')
pyautogui.click(44,53)

# Textbox filename => 672,504
#sleep(0.1)
pyautogui.click(672,504)
sleep(0.2)
pyautogui.write('testAuto6.jpg', interval=0.05)
pyautogui.press('enter')
# Move to Active video
pyautogui.press('f6')

# Middle focus
pyautogui.click(820,382)

#position_bar = pyautogui.position()
#print(f"position: {position_bar}")


#print("moving")
#pyautogui.moveTo(100, 150)

#print("test message boxes")
#text_confirm = pyautogui.confirm("hi")
#print(f"textbox: {text_confirm}")