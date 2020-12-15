
REGS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
        102, 113, 116, 121, 122, 123, 124, 125, 126, 134, 136, 138, 142, 147, 150, 152, 154, 156, 159, 161, 163,
        164, 173, 174, 177, 178, 186, 190, 193, 196, 197, 198, 199, 702, 750, 716, 761, 763, 774, 777, 790, 797,
        799]

CHARS = ['A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X',
         'А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']

def NumPlateParser(Numplate):
    Number = ""
    Region = ""
    temp = ""
    for i in range(0, len(Numplate)):
        temp += Numplate[i].upper()
    index = 0
    if len(temp) >= 8:
        if len(temp) <= 9:
            if temp[index] in CHARS: # A
                index += 1
                if temp[index].isdigit(): # 1
                    Number += temp[index]
                    index += 1
                    if temp[index].isdigit():  # 1
                        Number += temp[index]
                        index += 1
                        if temp[index].isdigit():  # 1
                            Number += temp[index]
                            index += 1
                            if temp[index] in CHARS:  # A
                                index += 1
                                if temp[index] in CHARS:  # A
                                    index += 1
                                    if temp[index].isdigit():  # 1
                                        Region += temp[index]
                                        index += 1
                                        if temp[index].isdigit():  # 1
                                            Region += temp[index]
                                            if len(temp) == 9:
                                                index += 1
                                                if temp[index].isdigit():  # 1
                                                    Region += temp[index]
                                            if Number != "000":
                                                if int(Region) in REGS:
                                                    return temp
                                                else:
                                                    print(Region)
                                                    index = -1
                                            else:
                                                index = -2
    if index == 0:
        return ""
    elif index == -1:
        return "Sorry, but there is no such region"
    elif index == -2:
        return "Sorry, but numbers cant be 000"
    else:
        return "Sorry, but character " + '"' + temp[index] + '"' + " cant be here"

def TessNumplateParser(numplate):
    temp1 = ""
    temp2 = ""
    for ch in numplate:
        temp1 += ch.upper()
    for ch in temp1:
        if ch.isalpha():
            if ch in CHARS:
                temp2 += ch
        else:
            temp2 += ch
    return temp2
