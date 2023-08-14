from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton,ContentType
from datetime import datetime
from userfile import id_base,username_base,create_file,put_msg_base,get_put
import pathlib
from pathlib import Path
from cases import cases_base


admin=5965231899
bot=Bot(token="5856871549:AAFtXMLTLmtFMeZt57-wrsZHqhCEY8xz-LM",parse_mode="HTML")
dp=Dispatcher(bot)

statisticbot=Bot(token="6343517427:AAEGBQd0ytfuraaalMR9xQw5evLxHuQ4yqU",parse_mode="HTML")
dp_statistics=Dispatcher(statisticbot)


rkbmenu=ReplyKeyboardMarkup(resize_keyboard=True)
btn1=KeyboardButton("🔗главное меню")
rkbmenu.add(btn1)

last_msg_base={}
check_base={}



time=0
async def get_time():
    global time
    time = datetime.now().strftime("%D %H:%M:%S")

#START
@dp.message_handler(commands="start")
async def start(message: types.Message):

    await message.delete()

    if str(message.from_user.id) in last_msg_base:
        await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    ikb=InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("💬 Обсудить проект",callback_data="callmanager")
    btn3 = InlineKeyboardButton("🫀Наши услуги", callback_data="uslugi")
    btn4 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn2 = InlineKeyboardButton("🧮 Рассчитать стоимость", callback_data="price")

    ikb.row(btn1).row(btn2).row(btn3).row(btn4)

    if message.from_user.id not in id_base:
        id_base.append(message.from_user.id)
        username_base.append("@"+message.from_user.username)
        inbase = "новичок"
    else:
        inbase="бывалый"

    msg = await message.answer("Приветственное сообщение",
                         reply_markup=ikb)

    await get_time()
    if str(message.from_user.id) not in put_msg_base:
        put_msg_base[str(message.from_user.id)]=""
    put_msg_base[str(message.from_user.id)]+=(f"{time}: Вошёл в бота\n")

    last_msg=msg.message_id
    last_msg_base[str(message.from_user.id)]=str(last_msg)
    await statisticbot.send_message(chat_id=admin,text=f"Новый пользователь\n"
                                                       f"В базе сейчас {len(id_base)} человек\n\n"
                                                       f"<b>бот:</b> @slashdigital_bot\n"
                                                       f"<b>юзернейм:</b> @{message.from_user.username}\n"
                                                       f"<b>айди:</b> {message.from_user.id}\n"
                                                       f"<b>дата:</b> {time}\n"
                                                       f"<b>статус:</b> {inbase}")

    await create_file()
    await statisticbot.send_document(chat_id=admin,document=open("idfile.txt","rb"))
    await statisticbot.send_document(chat_id=admin, document=open("userfile.txt", "rb"))


#ГЛАВНОЕ МЕНЮ
@dp.callback_query_handler(text="mainmenu")
async def open_menu(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("💬 Обсудить проект", callback_data="callmanager")
    btn3 = InlineKeyboardButton("🫀 Наши услуги", callback_data="uslugi")
    btn4 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn2 = InlineKeyboardButton("🧮 Рассчитать стоимость", callback_data="price")

    ikb.row(btn1).row(btn2).row(btn3).row(btn4)

    msg = await bot.send_message(message.from_user.id,
                           text="Главное меню",
                           reply_markup=ikb)

    await get_time()
    put_msg_base[str(message.from_user.id)]+=(f"{time}: Вошёл в главное меню\n")

    last_msg = msg.message_id
    last_msg_base[str(message.from_user.id)] = str(last_msg)


#ОБСУДИТЬ ПРОЕКТ
@dp.callback_query_handler(text="callmanager")
async def manager(callback: types.CallbackQuery):

    await bot.delete_message(chat_id=callback.from_user.id, message_id=last_msg_base[str(callback.from_user.id)])

    ikb=InlineKeyboardMarkup()
    btn1=InlineKeyboardButton("Вконтакте",url="https://vk.com/slashdigitalru",callback_data="go_to_vk")
    btn2=InlineKeyboardButton("Сайт",url="https://slashdigital.ru/",callback_data="go_to_site")
    btn3=InlineKeyboardButton("🗺 Главное меню",callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=callback.from_user.id, text="Отлично! Скоро вам напишет наш мегаприятный менеджер\n\n"
                                                               "А пока можете полазить у нас в соцсетях или воспользоваться другими функциями бота",
                           reply_markup=ikb)

    last_msg = msg.message_id
    last_msg_base[str(callback.from_user.id)] = str(last_msg)

    await get_time()
    put_msg_base[str(callback.from_user.id)]+=(f"{time}: Хочет обсудить проект\n")

    await statisticbot.send_message(chat_id=admin,
                                    text=f"@{callback.from_user.username} хочет пообщаться")


#РАССЧИТАТЬ СТОИМОСТЬ УСЛУГИ
@dp.callback_query_handler(text="price")
async def create_price(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    ikb=InlineKeyboardMarkup()
    btn1=InlineKeyboardButton("💻 Сайт",callback_data="buysite")
    btn2 = InlineKeyboardButton("🤖 Телеграмм-бот", callback_data="buybot")
    btn3 = InlineKeyboardButton("💎 Оформление Вконтакте", callback_data="buyvk")
    btn4 = InlineKeyboardButton("💿 Дизайн чего-либо другого", callback_data="buydesign")
    ikb.row(btn1).row(btn2).row(btn3).row(btn4)
    msg = await bot.send_message(chat_id=message.from_user.id, text="Всего пара вопросов и мы автоматически всё посчитаем!\n\n"
                                                                    "Что конкретно вас интересует?",
                                 reply_markup=ikb)

    if str(message.from_user.id) not in check_base:
        check_base[str(message.from_user.id)]=""

    await get_time()
    put_msg_base[str(message.from_user.id)]+=(f"{time}: Хочет рассчитать цену проекта\n")

    last_msg = msg.message_id
    last_msg_base[str(message.from_user.id)] = str(last_msg)

#РАССЧИТАТЬ САЙТ
@dp.callback_query_handler(text="buysite")
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Хочет сайт\n")
    check_base[str(message.from_user.id)]+="<b>Услуга</b>: 💻 Создание сайта\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("💵 Продать товар", callback_data="buysite_tovar")
    btn12 = InlineKeyboardButton("💶 Продать услугу", callback_data="buysite_usluga")
    btn2 = InlineKeyboardButton("📱 Получить контакты", callback_data="buysite_contacts")
    btn3 = InlineKeyboardButton("📎 Другое", callback_data="buysite_more")
    ikb.row(btn12).row(btn1).row(btn2).row(btn3)
    msg = await bot.send_message(chat_id=message.from_user.id,
                                     text=f"Что будет главной целью сайта?",
                                     reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)



#РАССЧЕТ - САЙТ - ТОВАРЫ
@dp.callback_query_handler(text="buysite_tovar")
async def buysite(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Цель сайта - продажа товаров\n")
    check_base[str(message.from_user.id)] += "<b>Цель сайта</b>: 💵 Продажа товаров\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("менее 20", callback_data="buysite_tovar_menee20")
    btn2 = InlineKeyboardButton("20 - 50", callback_data="buysite_tovar_20-50")
    btn3 = InlineKeyboardButton("более 50", callback_data="buysite_tovar_bolee50")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Сколько товаров будет на сайте?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ТОВАРЫ - КОЛИЧЕСТВО
@dp.callback_query_handler(text=["buysite_tovar_bolee50",
                                 "buysite_tovar_20-50",
                                 "buysite_tovar_menee20"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_tovar_bolee50":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Более 50 товаров\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: Более 50\n"
    elif message.data=="buysite_tovar_20-50":
        put_msg_base[str(message.from_user.id)] += (f"{time}: 20-50 товаров\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: От 20 до 50\n"
    elif message.data=="buysite_tovar_menee20":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Менее 20 товаров\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: Менее 20\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ да", callback_data="buysite_tovar_oplata_yes")
    btn2 = InlineKeyboardButton("❌ нет", callback_data="buysite_tovar_oplata_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Нужна ли онлайн оплата?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ТОВАРЫ - ОНЛАЙН ОПЛАТА
@dp.callback_query_handler(text=["buysite_tovar_oplata_no",
                                 "buysite_tovar_oplata_yes"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_tovar_oplata_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Без онлайн оплаты\n")
        check_base[str(message.from_user.id)] += "<b>Онлайн оплата</b>: ❌\n"
    elif message.data=="buysite_tovar_oplata_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: С онлайн оплатой\n")
        check_base[str(message.from_user.id)] += "<b>Онлайн оплата</b>: ✅\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ да", callback_data="buysite_tovar_smm_yes")
    btn2 = InlineKeyboardButton("❌ нет", callback_data="buysite_tovar_smm_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Есть ли у вас свои текста/фото/видео или сммщик который всё это сделает?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ТОВАРЫ - СММЩИК - КОНЕЦ
@dp.callback_query_handler(text=["buysite_tovar_smm_yes",
                                 "buysite_tovar_smm_no"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_tovar_smm_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Есть свой контент\n")
        check_base[str(message.from_user.id)] += "<b>Контент/свой сммщик</b>: ✅\n"
    elif message.data=="buysite_tovar_smm_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нет своего контента\n")
        check_base[str(message.from_user.id)] += "<b>Контент/свой сммщик</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Теперь мы знаем, что тебе нужно!\n\n"
                                      f"------------------------\n"
                                      f"{check_base[str(message.from_user.id)]}"
                                      f"------------------------\n\n"
                                      f"Тут надо написать что нибудь рекламное и ссылочку на сайт по типу tone of web\n\n"
                                      f"Стоимость начинается от 45000 рублей",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)




#РАССЧЕТ - САЙТ - УСЛУГИ - НАЧАЛО
@dp.callback_query_handler(text="buysite_usluga")
async def buysite(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Цель сайта - продажа услуг\n")
    check_base[str(message.from_user.id)] += "<b>Цель сайта</b>: 💵 Продажа услуг\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("менее 10", callback_data="buysite_usluga_menee10")
    btn2 = InlineKeyboardButton("более 10", callback_data="buysite_usluga_bolee10")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Сколько услуг будет на сайте?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ТОВАРЫ - ОПЛАТА
@dp.callback_query_handler(text=["buysite_usluga_bolee10",
                                 "buysite_usluga_menee10"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_usluga_bolee10":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Более 10 услуг\n")
        check_base[str(message.from_user.id)] += "<b>Количество услуг</b>: Более 10\n"
    elif message.data=="buysite_usluga_menee10":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Менее 10 услуг\n")
        check_base[str(message.from_user.id)] += "<b>Количество услуг</b>: Менее 10\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ да", callback_data="buysite_usluga_oplata_yes")
    btn2 = InlineKeyboardButton("❌ нет", callback_data="buysite_usluga_oplata_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Нужна ли онлайн оплата?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ТОВАРЫ - ОНЛАЙН ОПЛАТА
@dp.callback_query_handler(text=["buysite_usluga_oplata_no",
                                 "buysite_usluga_oplata_yes"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_usluga_oplata_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Без онлайн оплаты\n")
        check_base[str(message.from_user.id)] += "<b>Онлайн оплата</b>: ❌\n"
    elif message.data=="buysite_usluga_oplata_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: С онлайн оплатой\n")
        check_base[str(message.from_user.id)] += "<b>Онлайн оплата</b>: ✅\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ да", callback_data="buysite_usluga_smm_yes")
    btn2 = InlineKeyboardButton("❌ нет", callback_data="buysite_usluga_smm_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Есть ли у вас свои текста/фото/видео или сммщик который всё это сделает?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ТОВАРЫ - СММЩИК - КОНЕЦ
@dp.callback_query_handler(text=["buysite_usluga_smm_yes",
                                 "buysite_usluga_smm_no"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_usluga_smm_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Есть свой контент\n")
        check_base[str(message.from_user.id)] += "<b>Контент/свой сммщик</b>: ✅\n"
    elif message.data=="buysite_usluga_smm_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нет своего контента\n")
        check_base[str(message.from_user.id)] += "<b>Контент/свой сммщик</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Теперь мы знаем, что тебе нужно!\n\n"
                                      f"------------------------\n"
                                      f"{check_base[str(message.from_user.id)]}"
                                      f"------------------------\n\n"
                                      f"Тут надо написать что нибудь рекламное и ссылочку на сайт по типу tone of web\n\n"
                                      f"Стоимость начинается от 45000 рублей",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)



#РАССЧЕТ - САЙТ - КОНТАКТЫ - 1
@dp.callback_query_handler(text="buysite_contacts")
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Цель сайта - получить контакты\n")
    check_base[str(message.from_user.id)] += "<b>Цель сайта</b>: 📱 Получить контакты\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ Есть", callback_data="buysite_contacts_yes")
    btn2 = InlineKeyboardButton("❌ Нет", callback_data="buysite_contacts_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Есть ли у вас свой фото/видео контент?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - КОНТАКТЫ - 2
@dp.callback_query_handler(text=["buysite_contacts_yes",
                                 "buysite_contacts_no"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_contacts_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Есть свой контент\n")
        check_base[str(message.from_user.id)] += "<b>Контент</b>: ✅\n"
    elif message.data=="buysite_contacts_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нет своего контента\n")
        check_base[str(message.from_user.id)] += "<b>Контент</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ Да", callback_data="buysite_contacts_utp_yes")
    btn2 = InlineKeyboardButton("❌ Нет", callback_data="buysite_contacts_utp_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Вы уже определили свою целевую аудиторию, позиционирование, УТП?",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")


    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - КОНТАКТЫ - 3 - КОНЕЦ
@dp.callback_query_handler(text=["buysite_contacts_utp_yes",
                                 "buysite_contacts_utp_no"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_contacts_utp_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Есть утп, позиционирование и т.д\n")
        check_base[str(message.from_user.id)] += "<b>ЦА, УТП и т.д</b>: ✅\n"
    elif message.data=="buysite_contacts_utp_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нет своего контента\n")
        check_base[str(message.from_user.id)] += "<b>ЦА, УТП и т.д</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Теперь мы знаем, что тебе нужно!\n\n"
                                      f"------------------------\n"
                                      f"{check_base[str(message.from_user.id)]}"
                                      f"------------------------\n\n"
                                      f"Тут надо написать что нибудь рекламное и ссылочку на сайт по типу tone of web\n\n"
                                      f"Стоимость начинается от 45000 рублей",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)



#РАССЧЕТ - САЙТ - ДРУГОЕ - 1
@dp.callback_query_handler(text="buysite_more")
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Цель сайта - предстоит определить\n")
    check_base[str(message.from_user.id)] += "<b>Цель сайта</b>: 📱 Предстоит определить\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ Есть", callback_data="buysite_more_yes")
    btn2 = InlineKeyboardButton("❌ Нет", callback_data="buysite_more_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Есть ли у вас свой фото/видео контент?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ДРУГОЕ - 2
@dp.callback_query_handler(text=["buysite_more_yes",
                                 "buysite_more_no"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_contacts_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Есть свой контент\n")
        check_base[str(message.from_user.id)] += "<b>Контент</b>: ✅\n"
    elif message.data=="buysite_contacts_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нет своего контента\n")
        check_base[str(message.from_user.id)] += "<b>Контент</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ Да", callback_data="buysite_more_utp_yes")
    btn2 = InlineKeyboardButton("❌ Нет", callback_data="buysite_more_utp_no")
    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Вы уже определили свою целевую аудиторию, позиционирование, УТП?",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")


    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ - САЙТ - ДРУГОЕ - 3 - КОНЕЦ
@dp.callback_query_handler(text=["buysite_more_utp_yes",
                                 "buysite_more_utp_no"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buysite_more_utp_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Есть утп, позиционирование и т.д\n")
        check_base[str(message.from_user.id)] += "<b>ЦА, УТП и т.д</b>: ✅\n"
    elif message.data=="buysite_more_utp_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нет своего контента\n")
        check_base[str(message.from_user.id)] += "<b>ЦА, УТП и т.д</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Теперь мы знаем, что тебе нужно!\n\n"
                                      f"------------------------\n"
                                      f"{check_base[str(message.from_user.id)]}"
                                      f"------------------------\n\n"
                                      f"Тут надо написать что нибудь рекламное и ссылочку на сайт по типу tone of web\n\n"
                                      f"Стоимость начинается от 45000 рублей",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

people_on_case_base={}

@dp.callback_query_handler(text=["cases"])
async def cases(message:types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Зашёл в кейсы\n")

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("< Назад", callback_data="cases_back")
    btn2 = InlineKeyboardButton("Дальше >", callback_data="cases_up")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.add(btn1,btn2).row(btn3)

    people_on_case_base[str(message.from_user.id)]="0"

    photo=open(cases_base[people_on_case_base[str(message.from_user.id)]][0],"rb")
    caption=cases_base[people_on_case_base[str(message.from_user.id)]][1]

    msg = await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption=caption,
                         reply_markup=ikb)


    photo.close()

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

@dp.callback_query_handler(text=["cases_up"])
async def cases(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Листнул дальше\n")

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("< Назад", callback_data="cases_back")
    btn2 = InlineKeyboardButton("Дальше >", callback_data="cases_up")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.add(btn1, btn2).row(btn3)

    people_on_case_base[str(message.from_user.id)] = str(int(people_on_case_base[str(message.from_user.id)]) + 1)

    if int(people_on_case_base[str(message.from_user.id)]) > len(cases_base)-1:
        people_on_case_base[str(message.from_user.id)] = "0"

    if int(people_on_case_base[str(message.from_user.id)]) < 0:
        people_on_case_base[str(message.from_user.id)] = str(len(cases_base) - 1)

    photo = open(cases_base[people_on_case_base[str(message.from_user.id)]][0], "rb")
    caption = cases_base[people_on_case_base[str(message.from_user.id)]][1]

    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=photo,
                               caption=caption,
                               reply_markup=ikb)

    photo.close()

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

@dp.callback_query_handler(text=["cases_back"])
async def cases(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Листнул назад\n")

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("< Назад", callback_data="cases_back")
    btn2 = InlineKeyboardButton("Дальше >", callback_data="cases_up")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.add(btn1, btn2).row(btn3)

    people_on_case_base[str(message.from_user.id)] = str(int(people_on_case_base[str(message.from_user.id)]) - 1)

    if int(people_on_case_base[str(message.from_user.id)]) > len(cases_base)-1:
        people_on_case_base[str(message.from_user.id)] = "0"

    if int(people_on_case_base[str(message.from_user.id)]) < 0:
        people_on_case_base[str(message.from_user.id)] = str(len(cases_base)-1)

    photo = open(cases_base[people_on_case_base[str(message.from_user.id)]][0], "rb")
    caption = cases_base[people_on_case_base[str(message.from_user.id)]][1]

    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=photo,
                               caption=caption,
                               reply_markup=ikb)

    photo.close()

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#ЗАГРУЗКА АЙДИШНИКОВ
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def base_in(doc: types.Message):
    file = await doc.document.download(destination_file=r"C:\Users\ivanb\OneDrive\Рабочий стол\SLASH\БОТ ДЛЯ САЙТА\users.txt")
    for i in open("users.txt"):
        if i not in id_base and int(i) not in id_base:
            id_base.append(i.replace("\n",""))
    await statisticbot.send_message(chat_id=admin,text="База загружена")
    await create_file()
    await statisticbot.send_document(chat_id=admin, document=open("idfile.txt", "rb"))

#ТЕКСТОВЫЕ КОМАНДЫ
@dp.message_handler()
async def menu(message: types.Message):
    if message.text=="🔗главное меню":
        await start(message)

    elif message.from_user.id==admin:
        if message.text=="users":
            await create_file()
            await statisticbot.send_document(chat_id=admin, document=open("idfile.txt", "rb"))
            await statisticbot.send_document(chat_id=admin, document=open("userfile.txt", "rb"))

        if message.text=="cjm":
            await message.delete()
            await get_put()
            await statisticbot.send_document(chat_id=admin, document=open("cjm.txt", "rb"))

        else:
            for i in id_base:
                await bot.send_message(chat_id=i,text=message.text)
            await statisticbot.send_message(chat_id=admin,text=f"Сообщение - {message.text} - отправлено {len(id_base)} людям")

    else:
        await statisticbot.send_message(chat_id=admin, text=f"<b>ошибка:</b> {message.text}\n"
                                                                   f"<b>пользователь:</b> @{message.from_user.username}\n"
                                                                   f"<b>айди:</b> <code>{message.from_user.id}</code>")


if __name__=="__main__":
    executor.start_polling(dispatcher=dp,skip_updates=True)

