from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from subprocess import Popen
from subprocess import PIPE

from Core.config import TG_TOKEN
from Core.config import TG_API_URL


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Я родился!",
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Я милый Стичик!\n"
             "Поиграй со мной!\n"
             "Ты кхароший, я буду тебе помогать!"
    )


def do_love(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Я люблю тебя!",
    )


def do_time(bot: Bot, update: Update):
    process = Popen(["date"], stdout=PIPE)
    text, error = process.communicate()
    if error:
        text = "У меня тут ошибочка, надо что то сделать"
    else:
        text = text.decode("utf-8")
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )


def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Ваш ID = {}\n{}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )


def main():
    bot = Bot(
        token=TG_TOKEN,
        base_url=TG_API_URL,
    )
    updater = Updater(
        bot=bot,
    )

    # создаем хэндлеры
    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    love_handler = CommandHandler("love", do_love)
    message_handler = MessageHandler(Filters.text, do_echo)

    # регестрируем хэндлеры
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(love_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
