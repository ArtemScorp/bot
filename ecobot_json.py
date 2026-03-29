import os, json
from telebot import TeleBot

folder = "images2"

API_TOKEN = "8714968070:AAEXAuZXUsjugRaiMHS0ICvI-YBfonouVAc"
bot = TeleBot(API_TOKEN)


obj = {
    "zero_fakt0": {
        "message": "В Тихом океане есть мусорное пятно, площадь которого достигает 1,5 млн км², что больше площади большинства стран мира. Течения сносят сюда миллионы тонн мусора ежегодно",
        "imgName": "1.jpeg",
    },
    "one_fakt0": {
        "message": "Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок.",
        "imgName": "2.jpeg",
    },
    "two_fakt0": {
        "message": "Ежегодно океан становится всё более кислым, на это влияют выбросы парниковых газов, в частности, от переработанного топлива автомобилями. Подкисление океана — это самый опасный вид загрязнения.",
        "imgName": "3.jpeg",
    },
    "three_fakt0": {
        "message": "Повышение средней мировой температуры от заводов всего на 3–4 градуса может привести к таянию льдов, глобальному наводнению и исчезновению большей части лесов на Земле.",
        "imgName": "4.jpeg",
    },
}

keys = map(str, obj.keys())
# print(qqq)


@bot.message_handler(commands=["start"])
def send_detail(message):
    bot.reply_to(
        message, "Тут список всех команд которые раскажут по 1 факту о экологии"
    )
    for key in keys:
        bot.reply_to(message, "/" + key)


@bot.message_handler(commands=keys)
def sent_fro(message):
    bot.reply_to(
        message,
        obj[message.text[1:]]["message"],
    )
    with open(f"{folder}/{obj[message.text[1:]]["imgName"]}", "rb") as f:
        bot.send_photo(message.chat.id, f)


if __name__ == "__main__":
    bot.polling(none_stop=True)
