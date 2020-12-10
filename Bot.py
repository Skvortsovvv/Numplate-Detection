import telebot
from telebot import types
import time
import Yolo
import Tess
import ParseNumplate

bot_token = '1418824024:AAHup8u15EmL_xzRJO0AKsLd9M9FdKuESoY'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chatID = message.chat.id
    username = message.chat.username
    bot.send_message(chatID, 'Hi, ' + username + '! I can detect'
                                                ' a number plate on a photo,and read it (this function is in'
                                                ' alpha stage). You just need to send a photo with a'
                                                ' license plate. I can also find information about a car by its'
                                                ' registration number.'
                                                ' For more information write /help')

@bot.message_handler(commands=['help'])
def send_help(message):
    chatID = message.chat.id
    bot.send_message(chatID, 'For more accuracy of detection, please choose a photo'
                             ' with the most clearly visible license plate and good lighting. '
                             'To get information about a car by registration plate, use the command'
                             ' /check [your number plate]. Input format: А123ВС45')

@bot.message_handler(commands=['check'])
def check_numplate(message):
    res = ParseNumplate.NumPlateParser(message.text)
    if res:
        bot.send_message(message.chat.id, "Here is information!")
        bot.send_message(message.chat.id, 'https://vin.drom.ru/report/' + res + '/')
    else:
        bot.send_message(message.chat.id, "Wrong format")

@bot.message_handler(content_types=['text'])
def reply_to_message(message):
    msg = message.text
    msg = msg.lower()
    if msg == 'hi':
        bot.send_message(message.chat.id, "Hi " + message.chat.username + " !")
    elif msg == "hello":
        bot.send_message(message.chat.id, "Hello " + message.chat.username + " !")
    else:
        bot.send_message(message.chat.id, "I don`t understand you :`(")

def AnswerButtons():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True ,resize_keyboard=True)
    check_num = types.KeyboardButton('Check with number')
    detect_num = types.KeyboardButton('Detect numplate')

    #markup.add(detect_num, check_num)
    return markup

def MainMenu():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    main_menu = types.KeyboardButton('Back to menu')
    markup.add(main_menu)
    return markup

@bot.message_handler(content_types=['photo'])
def photo(message):
    #print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    chatID = message.chat.id
    #print('chat_id = ', chatID)
    bot.send_message(chatID, 'Got a photo!')
    #print('fileID =', fileID)
    file_info = bot.get_file(fileID)
    #print('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    result = Yolo.detection()
    if result == -1:
        bot.send_message(chatID, "Sorry, but image size is low")
    elif result == -2:
        bot.send_message(chatID, "Sorry, but here is no number plate")
    else:
        if result > 2:
            bot.send_message(chatID, "Here is a number plates!")
        elif result == 2:
            bot.send_message(chatID, "Here is a number plate!")
        for i in range(1, result):
            bot.send_photo(chatID, photo=open(str(i)+'.jpg', 'rb'))
            read_num = Tess.Reading(i)
            if len(read_num) == 0:
                bot.send_message(chatID, "Sorry, I could not read this number :`(")
            else:
                bot.send_message(chatID, "Text on numplate: " + read_num)

while True:
    try:
        print('...')
        bot.polling()
    except:
        time.sleep(1)