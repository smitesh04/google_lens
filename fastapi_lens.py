import time
from fastapi import FastAPI, Query
from DrissionPage import ChromiumPage
import pyautogui
import re
from urllib.parse import unquote
import html

app = FastAPI()

@app.get("/google-lens-search")
def google_lens_search_by_image(image_url: str = Query(..., description="URL of the image to search with Google Lens")):

    # Set up browser options
    page = ChromiumPage()

    # Navigate to the website
    page.get(image_url)

    # Wait for the page to load completely
    time.sleep(2)

    # To right-click on the window
    pyautogui.moveTo(x=400, y=400, duration=1)
    pyautogui.rightClick()

    # To click on "Search With Google Lens"
    pyautogui.moveTo(x=461, y=725, duration=1)
    pyautogui.click()

    time.sleep(1)

    # Drag the image for Google Lens search
    pyautogui.moveTo(x=484, y=152, duration=1)
    pyautogui.mouseDown()
    pyautogui.moveTo(x=1116, y=953, duration=1.5)
    pyautogui.mouseUp()

    # Click on the search input of the Google Lens window
    pyautogui.moveTo(x=1316, y=258, duration=1.5)
    pyautogui.click()

    # Enter the search term into the search input
    text_to_type = "Shopsy"
    pyautogui.typewrite(text_to_type, interval=0.1)
    pyautogui.moveTo(x=1282, y=334, duration=1.5)
    pyautogui.click()

    # Find and extract links from the Google Lens window
    snu_links = []
    all_tabs = page.tab_ids
    for t in all_tabs:
        try:
            element = page.get_tab(t).ele('tag:lens-side-panel-app').sr.ele('tag:iframe')
            if element:
                texttt = page.get_tab(t).ele('tag:lens-side-panel-app').sr.ele('tag:iframe').html
                links = set(re.findall(r'(https://www.shopsy.*?)"', texttt))
                for link in links:
                    if 'SNU' in link:
                        link = link.encode('utf-8').decode('unicode_escape')
                        link = unquote(link)
                        link = html.unescape(link)
                        link = re.findall(r'(https.*?pid.*?)&', link)[0]
                        if link not in snu_links:
                            snu_links.append(link)
                break
        except Exception as e:
            print(e)
            continue

    # Close the browser
    page.close()

    # Return the list of links as a JSON response
    # return {"links": snu_links}
    return snu_links

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
