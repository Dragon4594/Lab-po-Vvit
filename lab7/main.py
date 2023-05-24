import telebot, datetime, calendar, psycopg2
from telebot import types
token = "6048054116:AAHAZKbYUffHFXB04tcQx_y4L0Z6JsTv0cY"

bot = telebot.TeleBot(token)
conn = psycopg2.connect(database="rasp_bd",
                        user="postgres",
                        password="1242EefD933",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()
#SELECT  day, subject1, full_name, room_numb, start_time, num, ned FROM timetable, teacher;
'''cursor.execute("SELECT * FROM timetable  WHERE day=%s and ned=%s", (str(day1),str(ned1)))
records = cursor.fetchall()
print(records)
for row in records:
    a=str(row[1]) +' | '+ str(row[3]) +' | '+ str(row[4])+' | '+ str(row[5])+' | '+str(row[6])+' | '+ str(row[2])
    print(a)'''
#str(f'{cursor.execute("SELECT * FROM timetable,teacher WHERE timetable.day=%s and timetable.ned=%s", (str(day1),str(ned1)))}!\n')
def bd(ned1,day1):
    data = str(datetime.datetime.today())
    d = int(data[8] + data[9])
    g = int(data[0] + data[1] + data[2] + data[3])
    m = int(data[6])
    s = calendar.Calendar()
    sd = s.monthdays2calendar(g, m)
    dd = d // 7
    pn = str(sd[dd])
    if pn[3] == ',':
        pn1 = int(pn[2]) % 2
    else:
        pn1 = int(pn[2] + pn[3]) % 2
    ned = 0
    if pn1 == 1:
        ned = 'нч'
    else:
        ned = 'чтн'
    if ned1==1:
        if ned=='чтн':
            ned='нч'
        else:
            ned='чтн'
    ned1=ned
    a=cursor.execute("SELECT day,room_numb,start_time,num,ned,subject1,full_name FROM timetable JOIN teacher on teacher.subjectt=timetable.subject1 WHERE timetable.day=%s and timetable.ned=%s", (str(day1),str(ned)))
    if day1=='ПТ':
        day1=' пятницу '

    if day1=='ПН':
        day1=' понедельник '

    if day1=='ВТ':
        day1=' вторник '

    if day1=='СР':
        day1=' среду '

    if day1=='ЧТ':
        day1=' четверг '
    records = cursor.fetchall()
    if len(records)==0:
        return ('на'+ day1 + 'пар нет в расписании')
    else:
        a=''
        for row in records:
            a = a+ f'{row[0]}\n{row[1]} | {row[2]} | {row[3]}\n{row[5]}\n{row[6]}\n----------------------------------\n'
            #a = a+str(row[1]) + ' | ' + str(row[3]) + ' | ' + str(row[4]) + ' | ' + str(row[5]) + ' | ' + str(row[6]) + ' | ' + str(row[2])
        return a


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Да", "/help")
    bot.send_message(message.chat.id, 'Здравствуйте! Желаете ли вы узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:')
    bot.send_message(message.chat.id, '/week выдаёт расписание на любой день в институте')
    bot.send_message(message.chat.id, '/mtuci перейти на сайт МТУСИ')

@bot.message_handler(commands=['week'])
def start(message2):
    keyboard2 = types.ReplyKeyboardMarkup()
    keyboard2.row("на эту нед", "на следующую нед")
    bot.send_message(message2.chat.id, 'На какую неделю вы хотите увидеть расписание?', reply_markup=keyboard2)



@bot.message_handler(commands=['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ - https://mtuci.ru/')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "Да":
        bot.send_message(message.chat.id, 'Предлагаю вам перейти по ссылке на официальный сайт МТУСИ - https://mtuci.ru/')

    if message.text.lower() == "на пн":
        d = bd(0, 'ПН')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на вт":
        d = bd(0, 'ВТ')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на ср":
        d = bd(0, 'СР')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на чт":
        d = bd(0, 'ЧТ')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на пт":
        d = bd(0, 'ПТ')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на неделю":
        a=[('ПН'),('ВТ'),('СР'),('ЧТ'),('ПТ')]
        for i in range(0,5):
            d = bd(0, a[i])
            print(d)
            bot.send_message(message.chat.id, d)
    if message.text.lower() == "на пн.":
        d = bd(1, 'ПН')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на вт.":
        d = bd(1, 'ВТ')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на ср.":
        d = bd(1, 'СР')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на чт.":
        d = bd(1, 'ЧТ')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на пт.":
        d = bd(1, 'ПН')
        print(d)
        bot.send_message(message.chat.id, d)
    if message.text.lower() == "на неделю.":
        a=[('ПН'),('ВТ'),('СР'),('ЧТ'),('ПТ')]
        for i in range(0,5):
            d = bd(1, a[i])
            print(d)
            bot.send_message(message.chat.id, d)


    if message.text.lower() == "на эту нед":
        keyboard3 = types.ReplyKeyboardMarkup()
        keyboard3.row("на неделю", "на пн", "на вт", "на ср", "на чт", "на пт",)
        bot.send_message(message.chat.id, 'выввести расписание на всю неделю или на конкретный день?', reply_markup=keyboard3)


    if message.text.lower() == "на следующую нед":
        keyboard4 = types.ReplyKeyboardMarkup()
        keyboard4.row("на неделю.", "на пн.", "на вт.", "на ср.", "на чт.", "на пт.",)
        bot.send_message(message.chat.id, 'выввести расписание на всю неделю или на конкретный день?!', reply_markup=keyboard4)



bot.polling(none_stop=True, interval=0)
# Удалов Андрей