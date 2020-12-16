import cv2
from imutils import contours
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

def IsNumbersHere(num):
    counter = 0
    for ch in num:
        if ch.isdigit():
            counter += 1
    if counter > 3:
        return 1
    else:
       return 0

def Pars(num):
    temp = ""
    ind = 1
    if len(num) >= 9:
        while (num[len(num)-ind].isalpha()) & ((len(num) - ind) >= 9):
            ind += 1
        for index in range(len(num) - ind - 8, len(num) - ind +1):
            temp += num[index]
    else:
        print(num)
        return num
    print('3 ', temp)
    return temp

def FinalParsin(numplate):
    temp = ''
    for ch in numplate:
        if ch.isalpha():
            temp += ch.upper()
        elif ch.isdigit():
            temp += ch.upper()
    print('2', temp)
    return Pars(temp)

def parser(strings):
    max_d = 0
    max_ch = 0
    m_word = ""
    for el in strings:
        counter_d = 0
        counter_ch = 0
        for ch in el:
            if ch.isdigit():
                counter_d += 1
            elif ch.isalpha():
                counter_ch += 1
        if (counter_d >= 3) & (counter_d <= 8) & (counter_ch >= 2) & (counter_ch <= 6):
            if (counter_d >= max_d) & (counter_ch >= max_ch):
                max_d = counter_d
                max_ch = counter_ch
                m_word = el
    print("1 ", m_word)
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
                print("Suppositious numplate: ", result)
                results.append(result)
    return parser(results)
