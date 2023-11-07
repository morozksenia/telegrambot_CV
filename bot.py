#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'tape your token'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 My repository")
	item2 = types.KeyboardButton("😋 Text me")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Hello there !, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 My repository':
			bot.send_message(message.chat.id, 'https://github.com/morozksenia')
		elif message.text == '😋 Text me':
			bot.send_message(message.chat.id, 'http://t.me/Kesa_morta')
		else:
			bot.send_message(message.chat.id, 'I dont know what to say...😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
