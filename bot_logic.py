import time
from telebot import TeleBot

# Инициализация бота
API_TOKEN = '8600769859:AAE6UQ_AvUHvPBqx3zwfhPzg3RrD81Pegs8'
bot = TeleBot(API_TOKEN)  # Создаем экземпляр бота

# Глобальная переменная для счетчика
api = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global api
    bot.reply_to(message, f"Таймер подёт прямо сейчас!!!")
    bot.reply_to(message, f"Таймер пошёл! {api}")
# Исправленная функция с правильным названием и параметрами


# Бесконечный цикл для увеличения счетчика
def increment_api():
    global api
    while True:
        time.sleep(1)
        api += 1
        def send_time(message):
            bot.reply_to(message, f"{api} секунд")

# Запуск бота
if __name__ == '__main__':
    import threading
    # Запускаем инкремент счетчика в отдельном потоке
    threading.Thread(target=increment_api, daemon=True).start()
    bot.infinity_polling()
