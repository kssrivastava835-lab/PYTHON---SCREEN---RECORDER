import cv2  # it is used in video making , window show
import numpy as np # to convert image to array
import pyautogui # to take screenshot
import time # to make name of file
import os # to create folder or to check
import win32gui # Windows specific libraries
import win32con # windows ko minimize karne le liye use ho rahi hai
# create recordings folder
if not os.path.exists("recordings"):
    os.makedirs("recordings") # if folder named recordings is not their then create a new folder
def minimize_window():
    window = win32gui.FindWindow(None, "Screen recorder") # to find screen recorder named window
    if window:
        win32gui.ShowWindow(window, win32con.SW_MINIMIZE) # if window is finded then minimize taskbar
# auto-detect screen size
SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID") # codec format of video is decided , XVID is a common video format
output = cv2.VideoWriter( # video file is creating
    f"recordings/ScreenRecording_{time.strftime('%H-%M-%S_%d-%m-%y')}.mp4", # current time and data automatically is adding
    fourcc,
    20.0,
    SCREEN_SIZE # FPS = 20 frames per second , video size = screen size
)
print("Recording started....")
print("Window minimized in taskbar.")
print("Press q to exit.")
window_minimized = False # window will be minimized once
while True: # unless q is not pressed , loop will work till then
    img = pyautogui.screenshot() # Screen shot of current screen
    frame = np.array(img) # to convert screesnhot to numpy
    # RGB → BGR (correct conversion)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Screen recorder", frame) # Screen recording showing live on window
    if not window_minimized: # if window is not minimized
        minimize_window() # then minimize it 
        window_minimized = True
    output.write(frame) # to write current frame in video file
    if cv2.waitKey(1) & 0xFF == ord("q"): # if user pressed q
        print("Recording Finished.")
        break # then recording is pressed
output.release() # to convert video file properly
cv2.destroyAllWindows() # to close open cv windows
