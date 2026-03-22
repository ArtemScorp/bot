import telebot

API_TOKEN = '8600769859:AAE6UQ_AvUHvPBqx3zwfhPzg3RrD81Pegs8'

telebot.teleBot = 'API_TOKEN'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")