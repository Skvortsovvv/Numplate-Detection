import cv2
from imutils import contours
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user-pc\AppData\Local\Tesseract-OCR\tesseract.exe'

def FinalParsin(numplate):
    temp = ''
    for ch in numplate:
        if ch.isalpha():
            temp += ch.upper()
        elif ch.isdigit():
            temp += ch.upper()
    return temp

def parser(strings):
    max_d = 0
    m_word = ""
    for el in strings:
        counter_d = 0
        for ch in el:
            if ch.isdigit():
                counter_d += 1
        if counter_d >= 3:
            if counter_d >= max_d:
                max_d = counter_d
                m_word = el

    return FinalParsin(m_word)

def Reading(ind):
    results = []
    image = cv2.imread(str(ind)+'.jpg')
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
            result = pytesseract.image_to_string(img, lang='eng+rus', config='--psm 6')
            if len(result) > 7:
                print(result)
                results.append(result)
    return parser(results)
