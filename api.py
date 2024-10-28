import time
from DrissionPage import ChromiumPage
from fake_useragent import UserAgent
import pyautogui
import re
from urllib.parse import unquote
import html
import pytesseract
from PIL import ImageGrab
from corners import corners_fun, crop_window_excluding_ui


def google_lens_search_by_image(image_link):
    # Generate a random user agent
    ua = UserAgent()

    # Set up browser options
    page = ChromiumPage()

    # Navigate to the website
    # url = 'https://images.meesho.com/images/products/303431895/4e68v_512.jpg'
    page.get(image_link)
    page.set.window.max()

    # Wait for the page to load completely
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    screenshot_main = ImageGrab.grab()

    # Save the screenshot (optional, for debugging)
    screenshot_main.save("screenshot_main.png")
    cropped = crop_window_excluding_ui('screenshot_main.png')

    # To right click on the window
    pyautogui.moveTo(x=400, y=400, duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
    pyautogui.rightClick()


    ###
    # pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Actowiz/Desktop/Smitesh_Docs/tesseract-ocr-w64-setup-5.4.0.20240606.exe'
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Capture the screen (can be the full screen or a region where the context menu is)
    screenshot = ImageGrab.grab()

    # Save the screenshot (optional, for debugging)
    screenshot.save("screenshot.png")

    # Use pytesseract to perform OCR on the screenshot
    text_and_boxes = pytesseract.image_to_data(screenshot, output_type=pytesseract.Output.DICT)

    # Search for the word "Search with Google Lens" in the detected text
    for i, word in enumerate(text_and_boxes['text']):
        # if "Search with Google Lens" in word:
        if "Lens" in word:
            x = text_and_boxes['left'][i]
            y = text_and_boxes['top'][i]
            width = text_and_boxes['width'][i]
            height = text_and_boxes['height'][i]

            # Calculate the center of the text box
            center_x = x + width // 2
            center_y = y + height // 2

            # Print the coordinates for debugging
            print(f"Found 'Search with Google Lens' at ({center_x}, {center_y})")

            # Click the center of the found text
            pyautogui.click(center_x, center_y)
            break
    else:
        print("Could not find 'Search with Google Lens' in the screenshot.")
    ###




    corners = corners_fun('screenshot_main.png')

    # To click on Search With Google Lens
    pyautogui.moveTo(x=461, y=725, duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
    pyautogui.click()

    time.sleep(1)

    # # todo - If there's any pop-up on screen before image drag option then uncomment this code.
    # pyautogui.moveTo(x=959, y=627,
    #                      duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
    # pyautogui.click()

    # Click and hold the mouse button from top left of image
    pyautogui.moveTo(x=484, y=152, duration=1)
    pyautogui.mouseDown()
    # Drag the mouse to the bottom-right of the image (simulate dragging)
    pyautogui.moveTo(x=1116, y=953, duration=1.5)  # Set end_x and end_y to the bottom-right coordinates
    # Release the mouse button to finish the drag
    pyautogui.mouseUp()

    # Click on search input of google lens window
    pyautogui.moveTo(x=1316, y=258, duration=1.5)
    pyautogui.click()

    # Enter the text into the search input
    text_to_type = "Shopsy"
    pyautogui.typewrite(text_to_type, interval=0.1)
    pyautogui.moveTo(x=1282, y=334, duration=1.5)
    pyautogui.click()

    all_tabs = page.tab_ids
    for t in all_tabs:
        try:
            element = page.get_tab(t).ele('tag:lens-side-panel-app').sr.ele('tag:iframe')
            if element:
                print()
                texttt = page.get_tab(t).ele('tag:lens-side-panel-app').sr.ele('tag:iframe').html
                links = set(re.findall('(https://www.shopsy.*?)"', texttt))
                snu_links = list()
                for link in links:
                    # if 'SNU' in link:
                    link = link.encode('utf-8').decode('unicode_escape')
                    link = unquote(link)
                    link = html.unescape(link)
                    try:
                        link = re.findall('(https.*?pid.*?)&', link)[0]
                        if link not in snu_links:
                            snu_links.append(link)
                    except:pass

                print(len(snu_links))
                print(snu_links)
                break
        except Exception as e:print(e)

    # Close the browser
    page.close()


if __name__ == '__main__':

    url = 'https://images.meesho.com/images/products/41815313/ydyt9_512.jpg'
    google_lens_search_by_image(url)