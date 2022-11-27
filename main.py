import telebot
from telebot import types
import config
import managment_user

bot = telebot.TeleBot(config.token)



# Начало диалога
@bot.message_handler(commands=["start"])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Медицина")
    btn2 = types.KeyboardButton("Легализация")
    btn3 = types.KeyboardButton("Жилье")
    btn4 = types.KeyboardButton("Развлечения")
    btn5 = types.KeyboardButton("Образование")
    btn6 = types.KeyboardButton("Туры")
    btn7 = types.KeyboardButton("Поддержка")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.chat.id,
                     f"Здравствуйте, {message.from_user.first_name}. Я ваш виртуальный ассистент, что вас интересует?. \n\nВыберите из меню ниже: ",
                     parse_mode='html', reply_markup= markup)

#Кнопка /help
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,
                     "Чтобы удалить свои интересы воспользуйтесь функцией /delete."
                     "Чтобы обновить просто введите новый поисковой запрос."
                     )



user_store = {}

#Прием сообщений с выбором пункта меню от клиента
@bot.message_handler(content_types=['text'])
def add_to_search(message):
    global user_store
    global rds

    if message.text == "Медицина":

        keyboard = types.InlineKeyboardMarkup(row_width = 2)


        callback_button1 = types.InlineKeyboardButton(text="Стоматолог", callback_data=f'med-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Гинеколог", callback_data=f'med-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Терапевт", callback_data=f'med-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Психолог", callback_data=f'med-4-{message.chat.id}')
        callback_button5 = types.InlineKeyboardButton(text="Подолог", callback_data=f'med-5-{message.chat.id}')
        callback_button6 = types.InlineKeyboardButton(text="Проктолог", callback_data=f'med-6-{message.chat.id}')
        callback_button7 = types.InlineKeyboardButton(text="Аллерголог", callback_data=f'med-7-{message.chat.id}')
        callback_button8 = types.InlineKeyboardButton(text="Окулист", callback_data=f'med-8-{message.chat.id}')
        callback_button9 = types.InlineKeyboardButton(text="другое...", callback_data=f'med-9-{message.chat.id}')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9)
        bot.send_message(message.chat.id,
                         "Медицина в Армении очень славится своим профессионализмом и безудержным желанием людей помочь человеку(Красивый и не очень большой текст про медицину в армении",
                         reply_markup=keyboard )
        user = managment_user.Data_user(message.chat.id, message.from_user.username)
        user_store[message.chat.id] = user






    elif message.text == "Легализация":
        keyboard = types.InlineKeyboardMarkup(row_width = 1)



        callback_button1 = types.InlineKeyboardButton(text="ВНЖ-ПМЖ", callback_data=f'legal-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Получение загранпаспорта", callback_data=f'legal-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Оформление шенгенских виз", callback_data=f'legal-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Гражданство", callback_data=f'legal-4-{message.chat.id}')
        callback_button5 = types.InlineKeyboardButton(text="Открытие личного банковского счета", callback_data=f'legal-5-{message.chat.id}')
        callback_button6 = types.InlineKeyboardButton(text="ИНН", callback_data=f'legal-6-{message.chat.id}')
        callback_button7 = types.InlineKeyboardButton(text="SSN", callback_data=f'legal-7-{message.chat.id}')
        callback_button8 = types.InlineKeyboardButton(text="Регистрация адреса", callback_data=f'legal-8-{message.chat.id}')
        callback_button9 = types.InlineKeyboardButton(text="Свидетельство о налоговом резиденстве", callback_data=f'legal-9-{message.chat.id}')
        callback_button10 = types.InlineKeyboardButton(text="другое...",
                                                      callback_data=f'legal-10-{message.chat.id}')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,
                     callback_button6, callback_button7, callback_button8, callback_button9, callback_button10)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по легализации в стране", reply_markup=keyboard )
        user = managment_user.Data_user(message.chat.id, message.from_user.username)
        user_store[message.chat.id] = user

    elif message.text == "Жилье":
        keyboard = types.InlineKeyboardMarkup(row_width = 1)

        callback_button1 = types.InlineKeyboardButton(text="Аренда квартиры", callback_data=f'aprt-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Покупка/Продажа квартиры", callback_data=f'aprt-2-{message.chat.id}')

        keyboard.add(callback_button1, callback_button2)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по жилью в Армении", reply_markup=keyboard )
        user = managment_user.Data_user(message.chat.id, message.from_user.username)
        user_store[message.chat.id] = user
    elif message.text == "Развлечения":
        keyboard = types.InlineKeyboardMarkup(row_width = 1)



        callback_button1 = types.InlineKeyboardButton(text="Музеи Еревана", callback_data=f'event-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Клубы Еревана", callback_data=f'event-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Где выпить вино", callback_data=f'event-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Гле вкусно поесть", callback_data=f'event-4-{message.chat.id}')
        callback_button5 = types.InlineKeyboardButton(text="Армянская кухня", callback_data=f'event-5-{message.chat.id}')
        callback_button6 = types.InlineKeyboardButton(text="Итальянская кухня", callback_data=f'event-6-{message.chat.id}')
        callback_button7 = types.InlineKeyboardButton(text="Русская кухня", callback_data=f'event-7-{message.chat.id}')
        callback_button8 = types.InlineKeyboardButton(text="Французская кухня", callback_data=f'event-8-{message.chat.id}')
        callback_button9 = types.InlineKeyboardButton(text="Грузинская кухня", callback_data=f'event-9-{message.chat.id}')
        callback_button10 = types.InlineKeyboardButton(text="Китайская кухня",
                                                      callback_data=f'event-10-{message.chat.id}')
        callback_button11 = types.InlineKeyboardButton(text="Суши",
                                                      callback_data=f'event-11-{message.chat.id}')

        callback_button12 = types.InlineKeyboardButton(text="другое...",
                                                      callback_data=f'legal-12-{message.chat.id}')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,
                     callback_button6, callback_button7, callback_button8, callback_button9, callback_button10, callback_button11, callback_button12)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по развлечениям", reply_markup=keyboard )
        user = managment_user.Data_user(message.chat.id, message.from_user.username)
        user_store[message.chat.id] = user
    elif message.text == "Образование":
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        callback_button1 = types.InlineKeyboardButton(text="Школы для детей", callback_data=f'studu-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Вузы", callback_data=f'studu-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Уроки Армянского языка", callback_data=f'studu-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="другое...",
                                                       callback_data=f'studu-4-{message.chat.id}')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы про образование",
                         reply_markup=keyboard)
        user = managment_user.Data_user(message.chat.id, message.from_user.username)
        user_store[message.chat.id] = user
    elif message.text == "Туры":
        keyboard = types.InlineKeyboardMarkup(row_width=2)

        callback_button1 = types.InlineKeyboardButton(text="Ереван", callback_data=f'tour-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Дилижан", callback_data=f'tour-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Татев", callback_data=f'tour-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Гюмри", callback_data=f'tour-4-{message.chat.id}')

        callback_button5 = types.InlineKeyboardButton(text="другое...",
                                                       callback_data=f'tour-5-{message.chat.id}')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по турам",
                         reply_markup=keyboard)
        user = managment_user.Data_user(message.chat.id, message.from_user.username)
        user_store[message.chat.id] = user
    elif message.text == "Поддержка":
        bot.send_message(message.chat.id,
                         "Перейдет в чат с поддержкой")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):   #функция определения на какую кнопку нажал пользователь и дальнейшие действия
    global user_store
    # Если сообщение из чата с ботом
    if call.message:
        call_data = call.data.split("-")
        user = user_store[int(call_data[2])]

        if call_data[0] == "med":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про стоматологов")
            elif call_data[1]== "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Гинекологов")
            elif call_data[1]== "3":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Терапевтов")
            elif call_data[1]== "4":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Психологов")
            elif call_data[1]== "5":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Подологов")
            elif call_data[1]== "6":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Проктологов")
            elif call_data[1]== "7":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Аллергологов")
            elif call_data[1]== "8":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Окулистов")
            elif call_data[1]== "9":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про что-то другое")
        elif call_data[0] == "legal":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про ВНЖ-ПМЖ")
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Получение загранпаспорта")
            elif call_data[1] == "3":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про оформление шенгена")
            elif call_data[1] == "4":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Гражданство")
            elif call_data[1] == "5":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Открытие личного банковского счета")
            elif call_data[1] == "6":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про ИНН")
            elif call_data[1] == "7":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про SSN")
            elif call_data[1] == "8":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Регистрацию адреса")
            elif call_data[1] == "9":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Свидетельство о налоговм резиденстве")
            elif call_data[1] == "10":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про что-то другое")
        elif call_data[0] == "aprt":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про аренду квартир")
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про покупку/продажу квартир")
        elif call_data[0] == "event":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про музеи Еревана")
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про клубы Еревана")
            elif call_data[1] == "3":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация где выпить вино")
            elif call_data[1] == "4":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация где вкусно поесть")
            elif call_data[1] == "5":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Армянскую кухню")
            elif call_data[1] == "6":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Итальянскую кухню")
            elif call_data[1] == "7":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Русскую кухню")
            elif call_data[1] == "8":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Французскую кухню")
            elif call_data[1] == "9":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Грузинскую кухню")
            elif call_data[1] == "10":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Китайскую кухню")
            elif call_data[1] == "11":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про Суши")
            elif call_data[1] == "12":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про что-то другое")
        elif call_data[0] == "studu":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про образование для детей")
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про вузы")
            elif call_data[1] == "3":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про уроки Армянского языка")
            elif call_data[1] == "4":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про что-то другое")
        elif call_data[0] == "tour":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про туры в Ереван")
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про туры в Дилижпн")
            elif call_data[1] == "3":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про туры в Татев")
            elif call_data[1] == "4":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про туры в Гюмри")

            elif call_data[1] == "5":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про что-то другое")

if __name__ == "__main__":
    bot.infinity_polling()