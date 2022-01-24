import telebot
import xlrd
import random
from telebot import types
 


loc = (Geo-10242.xls")
bot = telebot.TeleBot('5097552028:AAE6KEZRgvBCVNlMnn-x9f1mj18VshMaFHA')
print ('ishga tushdi')

@bot.message_handler(commands=['start'])
def start (message):
    #bot.send_message(message.chat.id, 'Salom ' + message.chat.first_name) 
    #markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
    #but1 = types.KeyboardButton("TP raqam bo'yicha")
    #but2 = types.KeyboardButton("DCU bo'yicha")
    #markup.add(but1,but2)
    
    bot.reply_to(message,"Salom , {0.first_name}\nASKUE bo'limining lokatsiya botiga XUSH kelibsiz\nSiz bu bot orqali Konsentratorning joylashgan joyini aniqlashingiz mumkin".format(message.from_user),parse_mode='html',reply_markup=markup)
    
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    meter = message.text
    rowa = 1
    cola = 4
    for row in range(sheet.nrows): 
        if meter == sheet.cell_value(row,0):
            for col in range(sheet.row_len(row)):
             print (str(sheet.cell_value(row,col)))
             rowa = row
             cola = col    
    #def handle_text(message):
    #bot.send_message(message.chat.id, "Potstansiya: " + sheet.cell_value(rowa,3), "Potstansiya" + sheet.cell_value(rowa,4)  )
    #bot.send_message(message,"Potstansiya: , {1.sheet.cell_value(rowa,3)}\nFider: ,{2.sheet.cell_value(rowa,4)}")
            messageText = '🏢 ESP: '+sheet.cell_value(rowa,5)+'\n🏭 Potstansiya: '+sheet.cell_value(rowa,3)+'\n🗼 Fider: '+sheet.cell_value(rowa,4)+'\n📌 TP-raqami: '+sheet.cell_value(rowa,6)+'\nLokatsiyasi 👇'
            bot.send_message(message.chat.id, messageText, parse_mode='HTML')
            bot.send_location(message.chat.id, latitude=sheet.cell_value(rowa,1) , longitude=sheet.cell_value(rowa,2))
    #except:
        #bot.send_message.answer("Kiritilgan konsentrator raqami mavjud emas")
    

bot.polling()

