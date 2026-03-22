import os, random
from telebot import TeleBot

folder = 'images'
API_TOKEN = '8600769859:AAE6UQ_AvUHvPBqx3zwfhPzg3RrD81Pegs8'

bot = TeleBot(API_TOKEN) 
animals = ['обычный медведь', 'странный медведь', 'эпический медведь']
ss = os.listdir(f'{folder}')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    sa = random.choice(ss)
    with open(f'{folder}/{sa}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
    #bot.reply_to(message, sa)

 #    bot.reply_to(message, f"Таймер подёт прямо сейчас!!!")

@bot.message_handler(commands=['animals'])
def send_animal(message):
    try:
        chances = [0.9, 0.09, 0.01]
        animal = random.choices(animals, weights=chances, k=10)
        bot.reply_to(message, animal)  
    except print(0):
        bot.reply_to(message, "Ошибка")  

@bot.message_handler(commands=['help'])
def send_ffZ(message):
    bot.reply_to(message, '/start - ...',)
    bot.reply_to(message, '/animals - ...',)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
    
    