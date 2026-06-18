import telebot
from datetime import datetime

TOKEN = "8538891380:AAG8EbCSEjcCB6e_RRPY9myNpN0MHiu3L8M"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я Telegram бот.")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(
        message,
        "/start - запуск бота\n"
        "/help - список команд\n"
        "/time - текущее время\n"
        "/date - текущая дата\n"
        "/about - информация о боте"
    )


@bot.message_handler(commands=['time'])
def show_time(message):
    now = datetime.now().strftime("%H:%M:%S")
    bot.reply_to(message, f"Текущее время: {now}")
    
@bot.message_handler(commands=['date'])
def show_date(message):
    today = datetime.now().strftime("%d.%m.%Y")
    bot.reply_to(message, f"Сегодня: {today}")


@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(
        message,
        "Этот бот написан на Python с использованием telebot."
    )

@bot.message_handler(commands=['author'])
def author(message):
    bot.reply_to(
        message,
        "Автор бота: Адылбек"
    )
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(
        message,
        f"Вы написали: {message.text}"
    )


print("Бот запущен...")
bot.infinity_polling()