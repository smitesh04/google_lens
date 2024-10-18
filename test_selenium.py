import datetime
import math
import os.path
import random
import re
import sys
import time
import pyautogui
import pickle
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys

from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains

ua = UserAgent()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib


url = f'https://images.meesho.com/images/products/303431895/4e68v_512.jpg'

# chromedriver_path = r"C:\Users\Actowiz\Downloads\chromedriver-win64\chromedriver.exe"
# chrome_executable_path = r"C:\Users\Actowiz\Downloads\chrome-win64\chrome.exe"
# service = Service(executable_path=chromedriver_path)

# Set up undetected Chrome options
options = uc.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode (optional)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(f"user-agent={ua.random}")

# options.binary_location = chrome_executable_path

# driver = uc.Chrome(options=options, service=service)
driver = uc.Chrome(options=options)
# Navigate to the website
driver.get(url)
time.sleep(5)
print(pyautogui.position())
# Perform a right-click at a random location on the screen
action_chains = ActionChains(driver)
action_chains.move_by_offset(100, 100)  # Coordinates from the top-left corner (100, 100 as an example)
action_chains.context_click().perform()

try:
    # Wait a bit for the context menu to appear
    pyautogui.moveTo(x=346, y=611,
                     duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
    pyautogui.click()
    pyautogui.moveTo(x=1129, y=603,
                     duration=1)
    pyautogui.click()

    # Move to the start of the image (top-left corner)
    pyautogui.moveTo(x=624, y=152, duration=1)

    # Click and hold the mouse button
    pyautogui.mouseDown()

    # Drag the mouse to the bottom-right of the image (simulate dragging)
    pyautogui.moveTo(x=1338, y=1013, duration=1.5)  # Set end_x and end_y to the bottom-right coordinates

    # Release the mouse button to finish the drag
    pyautogui.mouseUp()

    pyautogui.moveTo(x=1632, y=277, duration=1.5)
    pyautogui.click()

    text_to_type = "Shopsy"

    # Simulate typing the text
    pyautogui.typewrite(text_to_type, interval=0.1)

    pyautogui.moveTo(x=1639, y=327, duration=1.5)
    pyautogui.click()

    time.sleep(5)

    # Get current window handle before interacting with the side panel
    main_window = driver.current_window_handle

    # List all available window handles (this will include the main window and the panel window)
    all_windows = driver.window_handles

    # Switch to each window and check for the Google Lens side panel
    for window in all_windows:
        driver.switch_to.window(window)

        # Now you can check if the window has the Google Lens side panel
        # Example: Check if the side panel contains a known element
        try:
            # Find the shadow host
            shadow_host = driver.find_element(By.CSS_SELECTOR, "lens-side-panel-app")

            # Use JavaScript to access the shadow root
            shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

            # Now you can interact with elements inside the shadow DOM
            # Example: Finding an element inside the shadow DOM
            inner_element = shadow_root.find_element(By.CSS_SELECTOR, "your-inner-element-selector")

            # Example: Clicking on an element inside the shadow DOM
            inner_element.click()
        except:
            # If not found, continue
            continue


except Exception as e:
    print(e)

print()