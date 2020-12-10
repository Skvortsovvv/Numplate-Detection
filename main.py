
import cv2
from imutils import contours
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user-pc\AppData\Local\Tesseract-OCR\tesseract.exe'



results = []
image = cv2.imread('1.jpg')
height, width, _ = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts, _ = contours.sort_contours(cnts[0])
for c in cnts:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    if area > 3000:
        img = image[y:y + h, x:x + w]
        result = pytesseract.image_to_string(img, lang='rus+eng', config='--psm 6')
        if len(result) > 7:
            print(result)
            #results.append(result)
#return results