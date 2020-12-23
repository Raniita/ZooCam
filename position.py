import pyautogui

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen.
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
print(f"Screen size: {screenWidth}x{screenHeight}") # T440p => 1366x768

pyautogui.confirm("Prepare your position reference")

position_bar = pyautogui.position()
print(f"position: {position_bar}")