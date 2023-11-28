import telebot

bot = telebot.TeleBot('6953502297:AAHKJchd1W7DgJ5jzdOClHtddljuE7B4X0Q')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Меня зовут ТолкБот, и я обожаю общаться с живыми людьми! Надеюсь, что Вы любите общаться с ботами.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['Bye'])
def main(message):
    bot.send_message(message.chat.id, 'Прощайте! Приятно было пообщаться с Вами. Надеюсь ещё загляните!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['What_do_you_like'])
def main(message):
    bot.send_message(message.chat.id, 'Я люблю многие вещи, но *общение с Вами* стоит на первом месте!',
                     parse_mode='Markdown')


bot.infinity_polling()