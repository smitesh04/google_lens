import time
from DrissionPage import SessionOptions, ChromiumPage, SessionPage
from fake_useragent import UserAgent
import pyautogui

# Generate a random user agent
ua = UserAgent()

# Set up browser options
page = ChromiumPage()
# page = SessionPage()
# options.add_argument(f'user-agent={ua.random}')

# Initialize DrissionPage in Chromium mode
# page = Chromium(session_options=options)

# page.latest_tab


# Navigate to the website
url = 'https://images.meesho.com/images/products/303431895/4e68v_512.jpg'
page.get(url)
# screen_width, screen_height = pyautogui.size()
# page.driver.(screen_width, screen_height)

# Wait for the page to load completely
time.sleep(5)
pyautogui.moveTo(x=400, y=400,
                     duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
    # pyautogui.click()
pyautogui.rightClick()

pyautogui.moveTo(x=461, y=725,
                     duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
pyautogui.click()
time.sleep(1)

'''
# pyautogui.moveTo(x=959, y=627,
#                      duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
# pyautogui.click()
'''
pyautogui.moveTo(x=484, y=152, duration=1)

# Click and hold the mouse button
pyautogui.mouseDown()

# Drag the mouse to the bottom-right of the image (simulate dragging)
pyautogui.moveTo(x=1116, y=953, duration=1.5)  # Set end_x and end_y to the bottom-right coordinates

# Release the mouse button to finish the drag
pyautogui.mouseUp()
# Wait to see the result


pyautogui.moveTo(x=1316, y=258, duration=1.5)
pyautogui.click()

text_to_type = "Shopsy"

pyautogui.typewrite(text_to_type, interval=0.1)
pyautogui.moveTo(x=1282, y=334, duration=1.5)
pyautogui.click()

all_tabs = page.tab_ids
for t in all_tabs:

    response = page.get_tab(t).html

    page.activate_tab(int(t))
    element = page.ele('@src=side_panel_app.js')


time.sleep(5)

# Close the browser
page.close()
