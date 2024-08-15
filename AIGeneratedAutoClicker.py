# Import necessary modules
import keyboard
import time
import pyautogui

# Set the key to enable/disable the autoclicker
ENABLE_KEY = '+'

# Set the delay between clicks (in seconds)
CLICK_DELAY = 0.5

# Flag to track whether the autoclicker is enabled or not
enabled = False

# Main loop
while True:
    # Check if the autoclicker is enabled
    if enabled:
        # Get the current mouse position
        pos = pyautogui.position()

        # Get the game window
        game_window = pyautogui.getWindowsWithTitle('Minecraft')[0]

        # Set the game window to be the active window
        pyautogui.getForegroundWindow(game_window)

        # Perform a mouse click at the current position
        pyautogui.click(pos.x, pos.y)

        # Sleep for the specified delay
        time.sleep(CLICK_DELAY)

    # Check if the enable key is being pressed
    if keyboard.is_pressed(ENABLE_KEY):
        # Toggle the autoclicker state
        enabled = not enabled