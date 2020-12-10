
REGS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
        30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
        84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
        102, 113, 116, 121, 122, 123, 124, 125, 126, 134, 136, 138, 142, 147, 150, 152, 154, 156, 159, 161, 163,
        164, 173, 174, 177, 178, 186, 190, 193, 196, 197, 198, 199, 702, 750, 716, 761, 763, 774, 777, 790, 797,
        799]

CHARS = ['A', 'B', 'E', 'K', 'M', 'H', 'O', 'P', 'C', 'T', 'Y', 'X',
         'А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']

def NumPlateParser(NumPlate):
    char_1 = ""
    char_2 = ""
    char_3 = ""
    numbers = ""
    region = ""
    temp = ""
    for i in range(7, len(NumPlate)):
        temp += NumPlate[i].upper()
    print(temp)
    if len(temp) >= 8:
        print('1')
        if len(temp) <= 9:
            print('2')
            if temp[0].isalpha(): # A
                print('3')
                char_1 = temp[0]
                if temp[1].isdigit(): # 1
                    print('4')
                    numbers += temp[1]
                    if temp[2].isdigit(): # 1
                        print('5')
                        numbers += temp[2]
                        if temp[3].isdigit(): # 1
                            print('6')
                            numbers += temp[3]
                            if temp[4].isalpha(): # A
                                print('7')
                                char_2 = temp[4]
                                if temp[5].isalpha(): # A
                                    print('8')
                                    char_3 = temp[0]
                                    if temp[6].isdigit(): # 1
                                        print('9')
                                        region += temp[6]
                                        if temp[7].isdigit(): # 1
                                            print('10')
                                            region += temp[7]
                                            if len(temp) == 9:
                                                if temp[8].isdigit(): # 1
                                                    print('11')
                                                    region += temp[8]
        else:
            return ""
    else:
        return ""

    if char_1 in CHARS:
        if char_2 in CHARS:
            if char_3 in CHARS:
                if int(numbers) != 000:
                    if len(region) == 3:
                        if region[0] != '0':
                            if int(region) in REGS:
                                print("Numplate ", temp)
                                return temp
                            else:
                                return "Sorry, but there is no such region"
                    elif int(region) in REGS:
                        print("Numplate ", temp)
                        return temp
                    else:
                        return "Sorry, but there is no such region"
                else:
                    return "Sorry, but numbers cant be 000"
            else:
                return "Sorry, but character " + '"' + temp[5] + '"' + " cant be here"
        else:
            return "Sorry, but character " + '"' + temp[4] + '"' + " cant be here"
    else:
        return "Sorry, but character " + '"' + temp[0] + '"' + " cant be here"
