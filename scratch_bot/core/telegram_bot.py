import os

import telebot
from telebot import types

from scratch_bot.core.models import Tariff
from scratch_bot.core.service import create_guest

TOKEN = os.getenv("telegram_bot_token")
API_KEY = os.getenv("telegram_bot_address")

# create a new Telegram Bot
bot = telebot.TeleBot(token=TOKEN)


# command description used in the "help" command
commands = {
    "start": "Начать работу с ботом",
    "help": "Информация о доступных командах",
}


@bot.message_handler(commands=["help"])
def command_help(message):
    """generate help text out of the commands
    dictionary defined at the top"""
    chat_id = message.chat.id
    help_text = "Доступные команды: \n"
    for key in commands:
        help_text += f"/{key}: {commands[key]}\n"
    bot.send_message(chat_id=chat_id, text=help_text)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    create_guest(message)
    tariffs = (
        Tariff.objects.only("title", "position", "price")
        .filter(enable=True)
        .order_by("position")
    )
    markup = types.InlineKeyboardMarkup()
    for tariff in tariffs:
        test_text: str = f"{tariff.position} {tariff.title} ({tariff.price} рублей)"
        markup.add(types.InlineKeyboardButton(text=test_text, callback_data=tariff.id))
    bot.send_message(
        chat_id=message.chat.id,
        text="Благодарим что вы заинтересованы в приобретении нашего "
        "уникального обучения. Выберите удобный для вас формат обучения",
        reply_markup=markup,
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id: int = call.from_user.id
    tariff_id = call.data
    tariff = Tariff.objects.filter(id=tariff_id).first()
    if tariff:
        text: str = (
            f"{tariff.position} - {tariff.title}\n\n"
            f"{tariff.description}\n\n"
            f"Цена: {tariff.price} рублей\n\n"
            f"для продолжения, пройдите по ссылке: "
            f"https://fromscratch.ru/oplata3.html"
        )
    else:
        text: str = "Нам жаль, кажется этот тариф не доступен :("
    bot.delete_message(chat_id=chat_id, message_id=call.message.id)
    bot.send_message(chat_id=chat_id, text=text)
