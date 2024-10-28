import cv2
import numpy as np


def corners_fun(image_path):
    # Load the image
    # image_path = "/mnt/data/image.png"
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    # edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)
    edges = cv2.Canny(gray_image, threshold1=150, threshold2=200)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours to find the bounding box of the largest detected area
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(max_contour)

    # Draw a rectangle around the detected boundary
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the result image
    cv2.imwrite("detected_boundary.png", image)

    # Print the coordinates of the top-left and bottom-right corners
    print(f"Top-left corner: ({x}, {y})")
    print(f"Bottom-right corner: ({x + w}, {y + h})")

    # Optionally display the image with drawn rectangle (remove if running in headless mode)
    cv2.imshow("Detected Boundary", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    corners = {
        'top_left_x':x,
        'top_left_y':y,
        'bottom_right_x':x+w,
        'bottom_right_y':x+h
    }

    return corners



from PIL import ImageGrab

def crop_window_excluding_ui(image_path):
    # Capture the entire screen
    screenshot_main = ImageGrab.grab()

    # Define the crop box (left, upper, right, lower)
    # These values should be adjusted based on your screen resolution and the position of the window
    left = 100    # Adjust based on your screen (e.g., starting x-coordinate)
    upper = 150   # Adjust based on your screen (e.g., starting y-coordinate)
    right = 1800  # Adjust based on your screen (e.g., ending x-coordinate)
    lower = 1000  # Adjust based on your screen (e.g., ending y-coordinate)

    # Create a crop box
    crop_box = (left, upper, right, lower)

    # Crop the image using the defined box
    cropped_image = screenshot_main.crop(crop_box)

    # Save the cropped image
    cropped_image.save(image_path)  # Save the result image

    # Optionally display the cropped image
    cropped_image.show()


