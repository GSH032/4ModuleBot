import telebot
import sqlite3
from telebot import types
import random

TOKEN = "7145425047:AAHaaLAkRK0x_J-6bDbiRWxEjPA7wgvyXgw"
bot = telebot.TeleBot(TOKEN)

markups = types.ReplyKeyboardMarkup(resize_keyboard=True)
item11 = types.KeyboardButton("Привет")
item22 = types.KeyboardButton("Помощь")
myConnection = sqlite3.connect("Bot4.db") #Задание 7 М4_Урок_03.docx
myCursor = myConnection.cursor()
myCursor.execute(" " "SELECT * FROM Movies" " ")
myResult = myCursor.fetchall()
for everyElement \
		in myResult:
	print(everyElement)

@bot.message_handler(commands=['start'])
def start(message):
		bot.send_message(message.chat.id, 'Привет дорогой пользователь! Я бот созданный по финальному проекту 4-го модуля Odin , а именно "УРОК 27-34. ИТОГОВЫЙ ПРОЕКТ МОДУЛЯ 4'
		'\nКстати отличное фото профиля <b>{0.first_name}</b>!'.format(message.from_user, bot.get_me()), parse_mode='HTML')
		photos = bot.get_user_profile_photos(message.chat.id)
		bot.send_photo(message.chat.id , photos.photos[0][0].file_id)
		markups.add(item11, item22)
		file = open('help.txt', 'rb')
		if (message.text == "Помощь"):
			bot.send_document(message.chat.id, file,
							  text="Вот список поддерживаемых мною команд в приведенном ниже файле!"
								   "Также там подробно описан мой функционал и возможности")

@bot.message_handler(commands=['photo'])
def photo(message):
	cred = open('cat.png', 'rb')
	bot.send_photo(message.chat.id, 'Лови котика!', cred)

@bot.message_handler(commands=['music'])
def music(message):
	conn = sqlite3.connect('Bot4.db')
	cur = conn.cursor()
	cur.execute('SELECT * FROM music')
	music = cur.fetchall()
	info = ''
	for el in music:
		info += (f'\n Имя {el[1]} '
				 f'\nИсполнитель {el[3]} '
				 f'\n Жанр {el[2]}')
		cur.close()

		bot.send_message(message.chat.id, info)
		conn.close()












@bot.message_handler(commands=['creator'])
def creator(message):
		bot.send_message(message.chat.id, 'Меня создал Шляков.Г.А')


@bot.message_handler(commands=['game'])
def game_choice_buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Камень")
    item2 = types.KeyboardButton("Ножницы")
    item3 = types.KeyboardButton("Бумага")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать в игру 'Камень, Ножницы, Бумага'! Чтобы начать игру, выберите один из вариантов:",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ["Камень", "Ножницы", "Бумага"])
def handle_choice(message):
    user_choice = message.text
    options = ["Камень", "Ножницы", "Бумага"]
    bot_choice = random.choice(options)

    bot.send_message(message.chat.id, f"Вы выбрали: {user_choice}")
    bot.send_message(message.chat.id, f"Выбор опонента: {bot_choice}")

    if user_choice == bot_choice:
        bot.send_message(message.chat.id, "Ничья!")
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or (
            user_choice == "Ножницы" and bot_choice == "Бумага") or (
            user_choice == "Бумага" and bot_choice == "Камень"):
        bot.send_message(message.chat.id, "Вы победили!")
    else:
        bot.send_message(message.chat.id, "Бот победил!")




@bot.message_handler(content_types = "text")
def reply(message):
	if message.text.__contains__("Привет"):
		bot.send_message(message.chat.id, 'Привет!')
	elif message.text.__contains__("Пока"):
		bot.send_message(message.chat.id, 'Пока')


	else:
		bot.send_message(message.chat.id, 'Может вы имели что-то другое ввиду? Напишите /help для получения помощи')



bot.polling(none_stop = True)

