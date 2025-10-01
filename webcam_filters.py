import cv2
import numpy as np


def apply_filter(image, filter_type):
    '''Apply selected filter or edge detection'''
    filtered_image = image.copy()

    if filter_type == 'red_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'gray':
        filtered_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'canny':
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
        edges = cv2.Canny(blurred, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'sobel':
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=5)
        combined = cv2.magnitude(sobelx, sobely)
        combined = np.uint8(np.clip(combined, 0, 255))
        filtered_image = cv2.cvtColor(combined, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'orignal':
        filtered_image = image.copy()

    return filtered_image


# Capture photo from webcam
cap = cv2.VideoCapture(0)
print('Print SPACE to take a picture or ESC to quit')
captured_image = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to access camera")
        break

    cv2.imshow("Webcam - Press SPACE to capture image", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:    # ESC key
        print("Exiting without capturing")
        cap.release()
        cv2.destroyAllWindows()
        exit()
    elif key == 32:    # SPACE key
        captured_image = frame.copy()
        print("Image captured!")
        break

cap.release()
cv2.destroyAllWindows()

# Apply filters on captured photo
if captured_image is None:
    print("No Picture taken")
    exit()

filter_type = "orignal"
print("Now apply filters. Options:-")
print("r - Red tint")
print("g - Green tint")
print("b - Blue tint")
print("y - Gray")
print("s - Sobel Edge Detector")
print("c - Canny Edge Detector")
print("o - Orignal")
print("q - Quit")

while True:
    filtered_image = apply_filter(captured_image, filter_type)
    cv2.imshow("Filtered Image", filtered_image)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('r'):
        filter_type == 'red_tint'
    elif key == ord('g'):
        filter_type == 'green_tint'
    elif key == ord('b'):
        filter_type == 'blue_tint'
    elif key == ord('y'):
        filter_type == 'gray'
    elif key == ord('s'):
        filter_type == 'sobel'
    elif key == ord('c'):
        filter_type == 'canny'
    elif key == ord('o'):
        filter_type == 'orignal'
    elif key == ord('q'):
        break

print("Exiting...Thanks for using the filter")
cv2.destroyAllWindows()

