import time
from DrissionPage import ChromiumPage
from fake_useragent import UserAgent
import pyautogui
import re
from urllib.parse import unquote
import html

def google_lens_search_by_image(image_link):
    # Generate a random user agent
    ua = UserAgent()

    # Set up browser options
    page = ChromiumPage()

    # Navigate to the website
    # url = 'https://images.meesho.com/images/products/303431895/4e68v_512.jpg'
    page.get(image_link)

    # Wait for the page to load completely
    time.sleep(2)

    # To right click on the window
    pyautogui.moveTo(x=400, y=400, duration=1)  # Set the x and y to the actual position of 'Search with Google Lens'
    pyautogui.rightClick()

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
                    if 'SNU' in link:
                        link = link.encode('utf-8').decode('unicode_escape')
                        link = unquote(link)
                        link = html.unescape(link)
                        link = re.findall('(https.*?pid.*?)&', link)[0]
                        if link not in snu_links:
                            snu_links.append(link)
                print(len(snu_links))
                print(snu_links)
                break
        except Exception as e:print(e)

    # Close the browser
    page.close()


if __name__ == '__main__':

    url = 'https://images.meesho.com/images/products/303431895/4e68v_512.jpg'
    google_lens_search_by_image(url)