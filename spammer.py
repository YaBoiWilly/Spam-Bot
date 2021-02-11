import pyautogui
import time

msg = open("shrek-script.txt", 'r')
text = []
for word in msg:
    text.append(word)

for line in text:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    text.remove(line)