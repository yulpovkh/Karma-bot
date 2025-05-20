import telebot
import re

TOKEN = '6689364491:AAEItc7haGOOb_sMZ4-LukaWTh_FJxTLaUA'
bot = telebot.TeleBot(TOKEN)

def to_arkan(value):
    while value > 22:
        value -= 22
    return value

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    match = re.search(r'\b(\d{2})\.(\d{2})\.(\d{4})\b', message.text)
    if match:
        day = int(match.group(1))
        month = int(match.group(2))
        year = match.group(3)

        # Аркани
        arkan_day = to_arkan(day)
        arkan_year = to_arkan(sum(int(d) for d in year))

        # Плюсова карма
        plus1 = to_arkan(arkan_day + month)
        plus2 = to_arkan(arkan_day + arkan_year)
        plus3 = to_arkan(plus1 + plus2)
        plus4 = to_arkan(month + arkan_year)
        plus5 = to_arkan(plus1 + plus2 + plus3 + plus4)

        # Мінусова карма
        minus1 = abs(arkan_day - month)
        minus2 = abs(arkan_day - arkan_year)
        minus3 = abs(minus1 - minus2)
        minus4 = abs(month - arkan_year)
        minus5 = to_arkan(minus1 + minus2 + minus3 + minus4)

        reply = (
            f"Карма для дати: {match.group(0)}\n\n"
            f"Плюсова карма:\n{plus1} | {plus2} | {plus3} | {plus4} | {plus5}\n\n"
            f"Мінусова карма:\n{minus1} | {minus2} | {minus3} | {minus4} | {minus5}"
        )
        bot.reply_to(message, reply)

bot.polling()