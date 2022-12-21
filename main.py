import telebot
from telebot import types
import config
import model
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
    addusers = managment_user.Managment_user()
    addusers.AddUser(model.Data_user(message.chat.id, message.from_user.username, message.from_user.first_name))

#Кнопка /help


user_store = {}

#Прием сообщений с выбором пункта меню от клиента
@bot.message_handler(content_types=['text'])
def add_to_search(message):
    global user_store
    global rds
    user = model.Data_user(message.chat.id, message.from_user.username, message.from_user.first_name)
    user_store[message.chat.id] = user
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
        callback_button9 = types.InlineKeyboardButton(text="другое...",
                                                      url=f'https://t.me/concierge_gotoarmenia')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9)
        bot.send_message(message.chat.id,
                         """Граждане РФ без страховки в Армении могут вызвать скорую. Медицинскую помощь окажут бесплатно.
Лечение будет бесплатным до тех пор, пока сохраняется угроза жизни. Дальше, если вы не прикреплены к поликлинике — за ваш счет. Прикрепиться к поликлинике можно после получения ВНЖ (work permit) и социальной карты (SSN).
Если у вас нет ВНЖ, вы можете воспользоваться платной медициной. Цены в Армении примерно такие же, как и в России.
Для обладателей социальной карты стоимость услуг будет ниже. Есть примеры того, как заплатив за единоразовый прием, пациент посещал врача еще раз бесплатно (например, если стало хуже или нужен контрольный осмотр).
Вызов скорой помощи — 103.
Горячая линия мэрии Еревана для медпомощи иностранцам:
• для звонков по будням с 09:00 до 18:00 – 010-54-40-58
• для звонков после 18:00 до 21:00 по будням и выходным – 094-26-75-55 и 091-65-40-64""",
                         reply_markup=keyboard )

    elif message.text == "Легализация":
        keyboard = types.InlineKeyboardMarkup(row_width = 1)



        callback_button1 = types.InlineKeyboardButton(text="ВНЖ", callback_data=f'legal-1-{message.chat.id}')
        callback_button12 = types.InlineKeyboardButton(text="ПМЖ", callback_data=f'legal-12-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="ССП", callback_data=f'legal-3-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Получение загранпаспорта", callback_data=f'legal-2-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Гражданство", callback_data=f'legal-4-{message.chat.id}')
        callback_button5 = types.InlineKeyboardButton(text="Открытие личного банковского счета", callback_data=f'legal-5-{message.chat.id}')
        callback_button6 = types.InlineKeyboardButton(text="ИНН", callback_data=f'legal-6-{message.chat.id}')
        callback_button7 = types.InlineKeyboardButton(text="SSN", callback_data=f'legal-7-{message.chat.id}')
        callback_button8 = types.InlineKeyboardButton(text="Регистрация адреса", callback_data=f'legal-8-{message.chat.id}')
        callback_button10 = types.InlineKeyboardButton(text="другое...",
                                                      url=f'https://t.me/concierge_gotoarmenia')
        callback_button11 = types.InlineKeyboardButton(text="Поддержка юриста",
                                                       url=f'https://t.me/concierge_gotoarmenia')

        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,
                     callback_button6, callback_button7, callback_button8, callback_button10, callback_button11, callback_button12)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по легализации в стране", reply_markup=keyboard )

    elif message.text == "Жилье":
        keyboard = types.InlineKeyboardMarkup(row_width = 1)

        callback_button1 = types.InlineKeyboardButton(text="Аренда квартиры", callback_data=f'aprt-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Покупка/Продажа квартиры", callback_data=f'aprt-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Основные онлайн базы",
                                                      callback_data=f'aprt-3-{message.chat.id}')
        keyboard.add(callback_button1, callback_button2, callback_button3)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по жилью в Армении", reply_markup=keyboard )


    elif message.text == "Развлечения":
        keyboard = types.InlineKeyboardMarkup(row_width = 1)



        callback_button1 = types.InlineKeyboardButton(text="Коворкинги", callback_data=f'event-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Салоны Еревана ", callback_data=f'event-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Барбершопы", callback_data=f'event-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Музеи Еревана", callback_data=f'event-4-{message.chat.id}')
        callback_button5 = types.InlineKeyboardButton(text="Клубы Еревана ", callback_data=f'event-5-{message.chat.id}')
        callback_button6 = types.InlineKeyboardButton(text="Где выпить вино ", callback_data=f'event-6-{message.chat.id}')
        callback_button7 = types.InlineKeyboardButton(text="Где вкусно поесть", callback_data=f'event-7-{message.chat.id}')

        callback_button12 = types.InlineKeyboardButton(text="другое...",
                                                      url=f'https://t.me/concierge_gotoarmenia')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,
                     callback_button6, callback_button7, callback_button12)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по развлечениям", reply_markup=keyboard )

    elif message.text == "Образование":
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        callback_button1 = types.InlineKeyboardButton(text="Школы для детей на русском языке", callback_data=f'studu-1-{message.chat.id}')
        callback_button5 = types.InlineKeyboardButton(text="Перечень документов, необходимых для зачисления в русскоязычные школы Армении",
                                                      callback_data=f'studu-5-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Вузы", callback_data=f'studu-2-{message.chat.id}')
        callback_button3 = types.InlineKeyboardButton(text="Уроки Армянского языка", callback_data=f'studu-3-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="другое...",
                                                      url=f'https://t.me/concierge_gotoarmenia')
        keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы про образование",
                         reply_markup=keyboard)
    elif message.text == "Туры":
        keyboard = types.InlineKeyboardMarkup(row_width=2)

        callback_button1 = types.InlineKeyboardButton(text="Ереван", callback_data=f'tour-1-{message.chat.id}')
        callback_button2 = types.InlineKeyboardButton(text="Дилижан", callback_data=f'tour-2-{message.chat.id}')
        callback_button4 = types.InlineKeyboardButton(text="Гюмри", callback_data=f'tour-4-{message.chat.id}')

        callback_button5 = types.InlineKeyboardButton(text="другое...",
                                                       url=f'https://t.me/concierge_gotoarmenia')
        keyboard.add(callback_button1, callback_button2,  callback_button4, callback_button5)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете выбрать интересующие вопросы по турам",
                         reply_markup=keyboard)

    elif message.text == "Поддержка":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        callback_button1 = types.InlineKeyboardButton(text="Поддержка",
                                                       url=f'https://t.me/concierge_gotoarmenia')

        keyboard.add(callback_button1)
        bot.send_message(message.chat.id,
                         "В этом пункте меню вы можете перейти на чат с поддержкой кликнув по кнопке",
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):   #функция определения на какую кнопку нажал пользователь и дальнейшие действия
    global user_store
    # Если сообщение из чата с ботом
    if call.message:
        call_data = call.data.split("-")
        user = user_store[int(call_data[2])]
        getData = managment_user.Managment_user()
        if call_data[0] == "med":
            send = getData.GetMedical(call_data[1])
            for i in send:
                try:
                    bot.send_message(user.telegchatID,
                                     f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone} \n <a href="{i.website}">Сайт клиники</a>',
                                     parse_mode='html')
                except:
                    continue



        elif call_data[0] == "legal":

            bot.send_photo(user.telegchatID, open(f'legal_picture/{call_data[1]}.jpg', 'rb'))

            if call_data[1] == "1":
                bot.send_photo(user.telegchatID, open(f'legal_picture/1.jpg', 'rb'))
            elif call_data[1]== "4":
                bot.send_photo(user.telegchatID, open(f'legal_picture/10.jpg', 'rb'))

        elif call_data[0] == "aprt":
            if call_data[1] == "1":
                bot.send_message(user.telegchatID,
                                 text="Во избежание негативного опыта, рекомендуем совершать все сделки в правовом поле (т.е. с договором, а не на “честном слове”). Также исключите такого понятия как внутренний договор, те есть без регистрации в Кадастре. Так как все сделки по недвижимости должны быть зарегистрированы то учтите что только с момента госрегистрации Ваш договор вступит в законную силу. Если у Вас будут вопросы по недвижимости то позвоните в горячую линию Кадастра по номеру 060 47 42 05 или переходите по этой ссылке https://www.e-cadastre.am/ru/contracts/browse")
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Найти жилье можно на тех же онлайн-базах по поиску жилья. По той же ссылке можете ознакомиться с другими договорами имеющими стандартный характер и облегчающий заключение Вашего договора прямо в Кадастре без нотариуса. Имейте ввиду что в этом случае Вы можете заключить договор только по стандартным договорам, имеющимся прямо в Кадастре. www.e-cadastre.am/ru/contracts/browse Не граждане Армении могут покупать жильё. Банки в Армении предоставляют ипотеку только гражданам РА. Условия необходимо уточнять индивидуально в банке. Подробнее по банкам зайдите по этой ссылке: https://banks.am/ru.")
            elif call_data[1] == "3":
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                url_button1 = types.InlineKeyboardButton(text="list.am", url="https://www.list.am/ru/")
                url_button2 = types.InlineKeyboardButton(text="estate.am",url="https://www.estate.am/ru")
                url_button3 = types.InlineKeyboardButton(text="airbnb.ru",url="https://www.airbnb.ru/armenia/stays")
                url_button4 = types.InlineKeyboardButton(text="booking.com",url="https://www.booking.com/index.pl.html")
                url_button5 = types.InlineKeyboardButton(text="real.estate.armenia",url="https://www.facebook.com/groups/repats.and.expats.real.estate.armenia/")
                url_button6 = types.InlineKeyboardButton(text="real-estate.am",url="https://www.real-estate.am/ru")
                url_button7 = types.InlineKeyboardButton(text="myrealty.am",url="https://myrealty.am/ru ")
                url_button8 = types.InlineKeyboardButton(text="realtors.am",url="https://www.realtors.am/ru")
                keyboard.add(url_button1, url_button2, url_button3, url_button4, url_button5, url_button6, url_button7, url_button8)
                bot.send_message(user.telegchatID,
                                 "Основные онлайн базы",
                                 reply_markup=keyboard)


        elif call_data[0] == "event":
            if call_data[1] != "6":
                send = getData.GetEntertainments(call_data[1])
                for i in send:
                    try:
                        if i.website != '':

                            bot.send_message(user.telegchatID,
                                             f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone} \n <a href="{i.website}">Сайт</a>',
                                             parse_mode='html')
                        else:
                            bot.send_message(user.telegchatID,
                                             f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone}',
                                             parse_mode='html')
                    except:
                        continue
            elif call_data[1] == "6":
                keyboard = types.InlineKeyboardMarkup(row_width=1)
                button1 = types.InlineKeyboardButton(text="Армянская кухня",
                                                         callback_data=f'eat-1-{call_data[2]}')
                button2 = types.InlineKeyboardButton(text="Итальянская кухня",
                                                         callback_data=f'eat-2-{call_data[2]}')
                button3 = types.InlineKeyboardButton(text="Русская кухня",
                                                         callback_data=f'eat-3-{call_data[2]}')
                button4 = types.InlineKeyboardButton(text=" Азиатская кухня",
                                                         callback_data=f'eat-4-{call_data[2]}')
                button5 = types.InlineKeyboardButton(text="Cтейк и бургеры",
                                                         callback_data=f'eat-5-{call_data[2]}')
                button6 = types.InlineKeyboardButton(text="Рыба и морепродукты",
                                                         callback_data=f'eat-6-{call_data[2]}')
                button7 = types.InlineKeyboardButton(text="Мексиканская кухня",
                                                         callback_data=f'eat-7-{call_data[2]}')
                button8 = types.InlineKeyboardButton(text="Греческая кухня",
                                                         callback_data=f'eat-8-{call_data[2]}')
                button9 = types.InlineKeyboardButton(text="Сладости",
                                                         callback_data=f'eat-9-{call_data[2]}')
                button10 = types.InlineKeyboardButton(text="Где позавтракать",
                                                         callback_data=f'eat-10-{call_data[2]}')
                keyboard.add(button1, button2, button3, button4, button5, button6, button7,
                             button8, button9, button10)
                bot.send_message(user.telegchatID,
                                 "Выберете кухню",
                                 reply_markup=keyboard)

        elif call_data[0] == "studu":
            if call_data[1] == "1":
                send = getData.GetSchool(call_data[1])
                for i in send:
                    try:
                        if i.website != '':

                            bot.send_message(user.telegchatID,
                                             f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone} \n <a href="{i.website}">Сайт</a>',
                                             parse_mode='html')
                        else:
                            bot.send_message(user.telegchatID,
                                             f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone}',
                                             parse_mode='html')
                    except:
                        continue
            elif call_data[1] == "3" or  call_data[1] == "2":
                send = getData.GetStudu(call_data[1])
                for i in send:
                    try:
                        if i.website != '':

                            bot.send_message(user.telegchatID,
                                             f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone} \n <a href="{i.website}">Сайт</a>',
                                             parse_mode='html')
                        else:
                            bot.send_message(user.telegchatID,
                                             f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone}',
                                             parse_mode='html')
                    except:
                        continue
            elif call_data[1] == "5":
                bot.send_message(user.telegchatID,
                                 text="""Перечень документов, необходимых для зачисления в русскоязычные школы Армении \n
                                        заполненное заявление;\n 
                                        копию свидетельства о рождении/паспорта ребенка;\n
                                        копию паспорта родителя;\n 
                                        справку с места проживания;\n 
                                        2 фотографии;\n
                                        медицинскую справку о состоянии здоровья.\n
                                        Важно! Как указано выше, переезд в Армению не всегда подразумевает зачисление детей в школу только по вышеуказанному перечню документов. Обратите внимание, что прием в гимназию им. А.Г. Ерицяна предусматривает рейтинг по итогам вступительного теста
                                        Форум про образование и досуг детей в Ереване: https://www.facebook.com/groups/yerevandlyadetei
                                        """)
        elif call_data[0] == "tour":
            if call_data[1] == "1":
                bot.send_photo(user.telegchatID, open(f'tour_picture/1.jpg', 'rb'))
                bot.send_photo(user.telegchatID, open(f'tour_picture/2.jpg', 'rb'))
                bot.send_photo(user.telegchatID, open(f'tour_picture/3.jpg', 'rb'))
            elif call_data[1] == "4":
                bot.send_photo(user.telegchatID, open(f'tour_picture/4.jpg', 'rb'))
            elif call_data[1] == "2":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про туры в Дилижане")
            elif call_data[1] == "5":
                bot.send_message(user.telegchatID,
                                 text="Здесь будет информация про что-то другое")
        elif call_data[0] == "eat":
            send = getData.GetEat(call_data[1])
            for i in send:
                try:
                    if i.website != '':

                        bot.send_message(user.telegchatID,
                                         f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone} \n <a href="{i.website}">Сайт</a>',
                                         parse_mode='html')
                    else:
                        bot.send_message(user.telegchatID,
                                         f' <b>{i.name}</b> \n <b>Адрес</b>: {i.address} \n <b>Тел</b>: {i.number_phone}',
                                         parse_mode='html')
                except:
                    continue
if __name__ == "__main__":
    bot.infinity_polling()