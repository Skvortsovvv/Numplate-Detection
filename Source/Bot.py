import telebot
import time
import Yolo
import Tess
import ParseNumplate
import Prediction
import config
bot_token = config.token

bot = telebot.TeleBot(token=bot_token)


def ItPredictedNumplate(chatID):
    read_number = Tess.Reading("image")
    read_number = ParseNumplate.TessNumplateParser(read_number)
    flag = Tess.IsNumbersHere(read_number)  # Check how good Tesseract read a numplate
    print("Flag ", flag)
    if len(read_number) == 0:
        bot.send_message(chatID, "Sorry, I could not read this number :`(")
    elif flag:
        bot.send_message(chatID, "Text on numplate: " + read_number)
    return flag


def DoingYOLOThings(chatID):
    result = Yolo.detection("image")
    if result == -1:
        bot.send_message(chatID, "Sorry, but image size is low")
    elif result == -2:
        bot.send_message(chatID, "Sorry, but here is no number plate")
    else:
        if result >= 2:
            indexes = Prediction.checkcropedimages(result)
            print("Numplates count: ", len(indexes))
            if len(indexes) == 1:
                bot.send_message(chatID, "Here is a number plate!")
            elif len(indexes) > 1:
                bot.send_message(chatID, "Here is a number plates!")
            else:
                bot.send_message(chatID, "Sorry, but here is no number plate")
            if len(indexes) > 0:
                for i in indexes:
                    bot.send_photo(chatID, photo=open(str(i) + '.jpg', 'rb'))
                    read_num = Tess.Reading(i)
                    read_num = ParseNumplate.TessNumplateParser(read_num)
                    if len(read_num) == 0:
                        bot.send_message(chatID, "Sorry, I could not read this number :`(")
                    else:
                        bot.send_message(chatID, "Text on numplate: " + read_num)


def DoEverything(message):
    fileID = message.photo[-1].file_id
    chatID = message.chat.id
    bot.send_message(chatID, 'Got a photo!')
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    prediction = Prediction.predicting("image.jpg")
    print("Prediction: ", prediction)
    flag = 1
    if prediction:
        flag = ItPredictedNumplate(chatID)
    if prediction != flag:
        DoingYOLOThings(chatID)


@bot.message_handler(commands=['start', 'about'])
def send_welcome(message):
    chatID = message.chat.id
    username = message.chat.username
    bot.send_message(chatID, 'Hi, ' + username + '! I can detect'
                                                ' a number plate on a photo,and read it (this function is in'
                                                ' alpha stage). You just need to send a command /check with'
                                                ' a photo attached. I can also find information about a car by it`s'
                                                ' registration number.'
                                                ' For more information type /help')

@bot.message_handler(commands=['help'])
def send_help(message):
    chatID = message.chat.id
    bot.send_message(chatID, 'For more accuracy of detection, please choose a photo'
                             ' with the most clearly visible license plate and good lighting. '
                             'To get information about a car by registration plate, use the command'
                             ' /checknum [your number plate]. Input format: А123ВС45.')

@bot.message_handler(commands=['checknum'])
def check_numplate(message):
    temp = ""
    for i in range(10, len(message.text)):
        temp += message.text[i]
    res = ParseNumplate.NumPlateParser(temp)
    if (len(res) > 7) & (len(res) < 10):
        bot.send_message(message.chat.id, "Here is some information!")
        bot.send_message(message.chat.id, 'https://vin.drom.ru/report/' + res + '/')
        bot.send_message(message.chat.id, 'https://avtocod.ru/proverkaavto/' + res + '?rd=GRZ')
    elif len(res) > 10:
        bot.send_message(message.chat.id, res)
    elif res == "":
        bot.send_message(message.chat.id, "Wrong format")

@bot.message_handler(content_types=["photo"])
def photo(message):
    if message.caption == "/check":
        DoEverything(message)


""""
while True:
    try:
        print('...')
        bot.polling()
    except:
        time.sleep(10)
"""
