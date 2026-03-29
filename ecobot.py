import os, json
from telebot import TeleBot

folder = "images2"

API_TOKEN = "8714968070:AAEXAuZXUsjugRaiMHS0ICvI-YBfonouVAc"
bot = TeleBot(API_TOKEN)


ab = "zero_fakt"
ac = "one_fakt"
ad = "two_fakt"
ae = "three_fakt"

@bot.message_handler(commands=["start"])
def send_detail(message):
    bot.reply_to(
        message, "Тут список всех команд которые раскажут по 1 факту о экологии"
    )

    bot.reply_to(message, "/" + ab)
    bot.reply_to(message, "/" + ac)
    bot.reply_to(message, "/" + ad)
    bot.reply_to(message, "/" + ae)


@bot.message_handler(commands=[ab])
def sent_one(message):
    bot.reply_to(
        message,
        "В Тихом океане есть мусорное пятно, площадь которого достигает 1,5 млн км², что больше площади большинства стран мира. Течения сносят сюда миллионы тонн мусора ежегодно",
    )
    with open(f"{folder}/1.jpeg", "rb") as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=[ac])
def sent_two(message):
    bot.reply_to(
        message,
        "Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок.",
    )
    with open(f"{folder}/2.jpeg", "rb") as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=[ad])
def sent_gss(message):
    bot.reply_to(
        message,
        "Ежегодно океан становится всё более кислым, на это влияют выбросы парниковых газов, в частности, от переработанного топлива автомобилями. Подкисление океана — это самый опасный вид загрязнения.",
    )
    with open(f"{folder}/3.jpeg", "rb") as f:
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=[ae])
def sent_fro(message):
    bot.reply_to(
        message,
        "Повышение средней мировой температуры от заводов всего на 3–4 градуса может привести к таянию льдов, глобальному наводнению и исчезновению большей части лесов на Земле.",
    )
    with open(f"{folder}/4.jpeg", "rb") as f:
        bot.send_photo(message.chat.id, f)


if __name__ == "__main__":
    bot.polling(none_stop=True)
