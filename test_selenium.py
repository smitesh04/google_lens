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

    # time.sleep(5)

    # pyautogui.moveTo(x=1625, y=767, duration=1.5)
    # pyautogui.click()
    # # action_chains.context_click().perform()

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

            # Wait for the lens-side-panel-app to be present
            wait = WebDriverWait(driver, 10)

            # Get the shadow host element (lens-side-panel-app)
            shadow_host = driver.find_element(By.CSS_SELECTOR, "lens-side-panel-app")

            shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
            time.sleep(2)

            # actions = ActionChains(driver)
            #
            # # pyautogui.moveTo(x=1534, y=538, duration=1.5)
            # # action_chains.move_by_offset(1534, 538)  # Coordinates from the top-left corner (100, 100 as an example)
            #
            # # pyautogui.click()
            # actions.context_click(shadow_root).perform()
            action_chains = ActionChains(driver)
            action_chains.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(2)
            action_chains.move_by_offset(100, 100)  # Coordinates from the top-left corner (100, 100 as an example)
            action_chains.context_click().perform()
            pyautogui.moveTo(x=1575, y=727, duration=1)
            pyautogui.click()
            time.sleep(3)

            pyautogui.moveTo(x=208, y=353, duration=1)
            pyautogui.click()
            pyautogui.moveTo(x=228, y=380, duration=1)
            pyautogui.click()

            time.sleep(60)

            # Access the shadow DOM

            # Example of finding elements inside the shadow DOM (adjust the selector as needed)
            # For instance, locating all links or product containers
            product_links = shadow_root.find_elements(By.CSS_SELECTOR, "a.LBcIee")

            # Extract and print links
            for product in product_links:
                link = product.get_attribute('href')  # Assuming they are anchor tags with href attributes
                print(link)
        except:
            # If not found, continue
            continue


except Exception as e:
    print(e)

print()