import os, random
from telebot import TeleBot

folder = 'images'
API_TOKEN = '8600769859:AAE6UQ_AvUHvPBqx3zwfhPzg3RrD81Pegs8'

bot = TeleBot(API_TOKEN) 
ss = os.listdir(f'{folder}')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    sa = random.choice(ss)
    with open(f'{folder}/{sa}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
    #bot.reply_to(message, sa)

 #    bot.reply_to(message, f"Таймер подёт прямо сейчас!!!")
    
if __name__ == '__main__':
    bot.polling(none_stop=True)