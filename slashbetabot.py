from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton,ContentType
from datetime import datetime
from userfile import id_base,username_base,create_file,put_msg_base,get_put
import pathlib
from pathlib import Path
from cases import cases_base
from uslugi import uslugi_base
#МАШИНА СОСТОЯНИЙ
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

#МАШИНА СОСТОЯНИЙ
storage=MemoryStorage()

"6233960605:AAFiiu2k_HZFN27vFvbZ8ITCtNcxRzFcxRA"
"5952524685:AAHamVB4b9BSG_GefeR5hQXpMPqIpRmEYwM"



admin=5965231899
bot=Bot(token="5856871549:AAFtXMLTLmtFMeZt57-wrsZHqhCEY8xz-LM",parse_mode="HTML")
dp=Dispatcher(bot,storage=MemoryStorage())

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
    png=open(Path(dir_path,"photo","startphoto.png"),"rb")
    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=png,
                               caption="Привет! Мы - <b>Slash <i>Digital</i></b>\n\n"
                               "Мы занимаемся созданием современного цифрового контента в медиа-пространстве.\n\n"
                               "<span class='tg-spoiler'>Мы делаем сайты, <i>дизайн</i>, анимации, <i>SMM</i> и разрабатываем мощных ботов</span>",
                               reply_markup=ikb)
    png.close()


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

    png = open(Path(dir_path, "photo", "startphoto.png"), "rb")
    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=png,
                               caption="Привет! Мы - <b>Slash <i>Digital</i></b>\n\n"
                                       "Мы занимаемся созданием современного цифрового контента в медиа-пространстве.\n\n"
                                       "<span class='tg-spoiler'>Мы делаем сайты, <i>дизайн</i>, анимации, <i>SMM</i> и разрабатываем мощных ботов</span>",
                               reply_markup=ikb)
    png.close()

    await get_time()
    put_msg_base[str(message.from_user.id)]+=(f"{time}: Вошёл в главное меню\n")

    last_msg = msg.message_id
    last_msg_base[str(message.from_user.id)] = str(last_msg)

#ОБСУДИТЬ ПРОЕКТ
@dp.callback_query_handler(text="callmanager")
async def manager(callback: types.CallbackQuery):

    await bot.delete_message(chat_id=callback.from_user.id, message_id=last_msg_base[str(callback.from_user.id)])

    ikb=InlineKeyboardMarkup()
    btn0 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn2=InlineKeyboardButton("💻 Сайт",url="https://slashdigital.ru/",callback_data="go_to_site")
    btn3=InlineKeyboardButton("🗺 Главное меню",callback_data="mainmenu")
    ikb.row(btn0).row(btn2).row(btn3)

    png = open(Path(dir_path, "photo", "schet.png"), "rb")
    msg = await bot.send_photo(chat_id=callback.from_user.id,
                               caption="Отлично! Скоро вам напишет наш мегаприятный менеджер\n\n"
                                       "А пока можете полазить на нашем сайте или воспользоваться другими функциями бота",
                               reply_markup=ikb,
                               photo=png)
    png.close()

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
    png=open(Path(dir_path,"photo","schet.png"),"rb")
    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=png,
                               caption="Всего пара вопросов и мы автоматически всё посчитаем!\n\n"
                                                                    "Что конкретно вас интересует?",
                               reply_markup=ikb)

    png.close()

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

people_on_uslugi_base={}

#УСЛУГИ
@dp.callback_query_handler(text='uslugi')
async def uslugi(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    people_on_uslugi_base[str(message.from_user.id)]="0"

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Зашёл в услуги\n")

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("< Назад", callback_data="uslugi_back")
    btn2 = InlineKeyboardButton("Дальше >", callback_data="uslugi_up")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    ikb.add(btn1, btn2).row(btn4).row(btn3)

    photo = open(uslugi_base[people_on_uslugi_base[str(message.from_user.id)]][0], "rb")
    caption = uslugi_base[people_on_uslugi_base[str(message.from_user.id)]][1]

    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=photo,
                               caption=caption,
                               reply_markup=ikb)

    photo.close()

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

@dp.callback_query_handler(text=["uslugi_up",
                                 "uslugi_back"])
async def uslugi(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()

    if message.data=="uslugi_up":
        people_on_uslugi_base[str(message.from_user.id)]=str((int(people_on_uslugi_base[str(message.from_user.id)])+1)%len(uslugi_base))
        put_msg_base[str(message.from_user.id)] += (f"{time}: Листнул дальше \n")
    else:
        if people_on_uslugi_base[str(message.from_user.id)]=="0":
            people_on_uslugi_base[str(message.from_user.id)]=str(len(uslugi_base)-1)
        else:
            people_on_uslugi_base[str(message.from_user.id)] = str((int(people_on_uslugi_base[str(message.from_user.id)])-1)%len(uslugi_base))
        put_msg_base[str(message.from_user.id)] += (f"{time}: Листнул назад \n")



    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("< Назад", callback_data="uslugi_back")
    btn2 = InlineKeyboardButton("Дальше >", callback_data="uslugi_up")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    ikb.add(btn1, btn2).row(btn4).row(btn3)

    photo = open(uslugi_base[people_on_uslugi_base[str(message.from_user.id)]][0], "rb")
    caption = uslugi_base[people_on_uslugi_base[str(message.from_user.id)]][1]

    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=photo,
                               caption=caption,
                               reply_markup=ikb)

    photo.close()

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)


#МАШИНА СОСТОЯНИЙ
class StepsForm(StatesGroup):
    get_zadacha=State()
    get_price=State()
    get_date=State()

#Рассчет другое
@dp.callback_query_handler(text="buydesign")
async def buydesign(message: types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Хочет что-то другое\n")

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Опишите задачу")

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await StepsForm.get_zadacha.set()

@dp.message_handler(state=StepsForm.get_zadacha)
async def get_name(message: types.Message, state: FSMContext):
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    zadacha=message.text
    await state.update_data(zadacha=zadacha)
    msg=await message.answer("Напишите желаемую 'вилку' проекта\n\n"
                         "(на какой бюджет рассчитываете?)")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)
    await StepsForm.get_price.set()

@dp.message_handler(state=StepsForm.get_price)
async def get_name(message: types.Message, state: FSMContext):
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    zadacha=message.text
    await state.update_data(vilka=zadacha)
    msg=await message.answer("В какие сроки хотите получить готовую работу?")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)
    await StepsForm.get_date.set()

@dp.message_handler(state=StepsForm.get_date)
async def get_name(message: types.Message, state: FSMContext):
    await message.delete()
    await bot.delete_message(chat_id=message.from_user.id,message_id=last_msg_base[str(message.from_user.id)])
    zadacha=message.text
    await state.update_data(sroki=zadacha)

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg=await message.answer("Отлично! Скоро с вами свяжется наш менеджер для того, чтобы уточнить все подробности",
                             reply_markup=ikb)

    data = await state.get_data()
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)
    await state.finish()

    await statisticbot.send_message(chat_id=admin,
                                    text=f"<b>клиент:</b> @{message.from_user.username}\n"
                                         f"<b>айди:</b> {message.from_user.id}\n\n"
                                         f"<b>задача:</b> {data['zadacha']}\n\n"
                                         f"<b>вилка:</b> {data['vilka']}\n\n"
                                         f"<b>срок:</b> {data['sroki']}\n\n")

#РАССЧЕТ БОТА 1
@dp.callback_query_handler(text="buybot")
async def buybot(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id,message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Хочет бота\n")
    check_base[str(message.from_user.id)] += "<b>Услуга</b>: 🤖 Создание телеграмм-бота\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🔗 Cвязь с клиентами", callback_data="buybot_chatbot")
    btn12 = InlineKeyboardButton("🧳 Организация бизнес-процессов", callback_data="buybot_business")
    btn2 = InlineKeyboardButton("📱 Продажа товаров", callback_data="buybot_magazine")
    btn3 = InlineKeyboardButton("🎬 Воронка продаж", callback_data="buybot_voronka")
    btn4 = InlineKeyboardButton("📎 Другое", callback_data="buybot_more")
    ikb.row(btn12).row(btn1).row(btn2).row(btn3).row(btn4)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Что будет главной целью бота?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ БОТА 2
@dp.callback_query_handler(text=["buybot_chatbot",
                                 "buybot_business",
                                 "buybot_magazine",
                                 "buybot_voronka",
                                 "buybot_more"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buybot_chatbot":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Цель бота - связь с клиентами\n")
        check_base[str(message.from_user.id)] += "<b>Цель бота</b>: 🔗 Связь с клиентами\n"

    elif message.data=="buybot_business":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Цель бота - организация бизнесс-процессов\n")
        check_base[str(message.from_user.id)] += "<b>Цель бота</b>: 🔗 Организация бизнес-процессов\n"

    elif message.data=="buybot_magazine":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Цель бота - продажа товаров\n")
        check_base[str(message.from_user.id)] += "<b>Цель бота</b>: 🔗 Продажа товаров\n"

    elif message.data=="buybot_voronka":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Цель бота - воронка продаж\n")
        check_base[str(message.from_user.id)] += "<b>Цель бота</b>: 🔗 Воронка продаж\n"

    elif message.data=="buybot_more":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Цель бота - предстоит определить\n")
        check_base[str(message.from_user.id)] += "<b>Цель бота</b>: 🔗 Предстоит опрелделить\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Уфф, неплохой выбор🦍\n\n"
                                      
                                      f"{check_base[str(message.from_user.id)]}\n"
                                      
                                      f"<span class='tg-spoiler'>Кстати, с таким ботом вы сможете <b>бесплатно собирать контакты пользователей</b> даже без их разрешения🤯\n\n"
                                      f"А дальше можно, например, делать по этим контактам <b>бесплатные рекламные рассылки</b>\n\n"
            
                                      f"<b>Стоимость:</b> от 15000 рублей\n"
                                      f"<b>Сроки:</b> от 4 дней</span>",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)



#РАССЧЕТ ВК 1
@dp.callback_query_handler(text="buyvk")
async def buybot(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id,message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    put_msg_base[str(message.from_user.id)] += (f"{time}: Хочет группу в ВК\n")
    check_base[str(message.from_user.id)] += "<b>Услуга</b>: 💎 Оформление группы Вконтакте\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Да, менее 10", callback_data="buyvk_menee10")
    btn2 = InlineKeyboardButton("Да, от 10 до 30", callback_data="buyvk_1030")
    btn3 = InlineKeyboardButton("Да, более 30", callback_data="buyvk_bolee30")
    btn4 = InlineKeyboardButton("Нет, товаров не будет", callback_data="buyvk_0")

    ikb.row(btn1).row(btn2).row(btn3).row(btn4)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Будут ли товары в группе? Если да, то сколько?",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

# РАССЧЕТ ВК 2
@dp.callback_query_handler(text=["buyvk_menee10",
                                 "buyvk_1030",
                                 "buyvk_bolee30",
                                 "buyvk_0"])
async def buybot(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()

    if message.data=="buyvk_menee10":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Будет менее 10 товаров\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: Менее 10\n"
    elif message.data=="buyvk_1030":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Будет 10-30 товаров\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: От 10 до 30\n"
    elif message.data=="buyvk_bolee30":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Будет более 30 товаров\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: Более 30\n"
    elif message.data=="buyvk_0":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Товаров не будет\n")
        check_base[str(message.from_user.id)] += "<b>Количество товаров</b>: 0\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ Да", callback_data="buyvk_yes")
    btn2 = InlineKeyboardButton("❌ Нет", callback_data="buyvk_no")

    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Нужен ли будет бот внутри группы?\n\n"
                                      f"Он может, к примеру, рассылать рекламу от имени сообщества",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

# РАССЧЕТ ВК 3
@dp.callback_query_handler(text=["buyvk_yes",
                                 "buyvk_no"])
async def buybot(message: types.CallbackQuery):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()

    if message.data=="buyvk_yes":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нужен бот внутри группы\n")
        check_base[str(message.from_user.id)] += "<b>Бот врнутри группы</b>: ✅\n"
    elif message.data=="buyvk_no":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Без бота внутри группы\n")
        check_base[str(message.from_user.id)] += "<b>Бот внутри группы</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("✅ Да", callback_data="buyvk_yes_1")
    btn2 = InlineKeyboardButton("❌ Нет", callback_data="buyvk_no_1")

    ikb.row(btn1).row(btn2)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"Нужна ли будет поддержка в дальнейшем?\n\n"
                                      f"Например, дизайн новых постов или статей",
                                 reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

#РАССЧЕТ ВК 4
@dp.callback_query_handler(text=["buyvk_yes_1",
                                 "buyvk_no_1"])
async def buysite(message: types.CallbackQuery):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await get_time()
    if message.data=="buyvk_yes_1":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Нужна поддержка\n")
        check_base[str(message.from_user.id)] += "<b>Поддержка</b>: ✅\n"
    elif message.data=="buyvk_no_1":
        put_msg_base[str(message.from_user.id)] += (f"{time}: Не нужна поддержка\n")
        check_base[str(message.from_user.id)] += "<b>Поддержка</b>: ❌\n"

    ikb = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🧮 Рассчитать ещё", callback_data="price")
    btn2 = InlineKeyboardButton("📎 Кейсы", callback_data="cases")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn2).row(btn3)

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"☠ После такого твоим конкурентам точно пизд%ц\n\n"
                                      f"{check_base[str(message.from_user.id)]}\n"
                                      
                                      f"<span class='tg-spoiler'>Бизнес стремительно переходит в интернет и Вконтакте самый лёгкий способ заявить о себе в сети. "
                                      f"Гибкий таргет, огромная клиентская база, невероятный потенциал роста\n\n"
                                      f"<b>Стоимость:</b> от 4990 рублей\n"
                                      f"<b>Сроки:</b> от 3 дней</span>",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

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
                                 text=f"Уже готовим мощщщное предложение💽\n\n"
                                      
                                      f"{check_base[str(message.from_user.id)]}\n"
                                      
                                      f"<span class='tg-spoiler'>Создаем уникальный дизайн и не работаем с шаблонными решениями. Перед тем, как написать 10 страниц кода, проводим 30 часов за анализом задач, которые он будет решать. Завершаем задачи в сроки и тестируем продукт, чтобы он работал как швейцарские часы.\n\n"
                                      f"<b>Стоимость:</b> от 35000 рублей\n"
                                      f"<b>Сроки:</b> от 7 дней</span>",
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
                                 text=f"Уже готовим мощщщное предложение💽\n\n"
                                      
                                      f"{check_base[str(message.from_user.id)]}\n"
                                      
                                      f"<span class='tg-spoiler'>Создаем уникальный дизайн и не работаем с шаблонными решениями. Перед тем, как написать 10 страниц кода, проводим 30 часов за анализом задач, которые он будет решать. Завершаем задачи в сроки и тестируем продукт, чтобы он работал как швейцарские часы.\n\n"
                                      f"<b>Стоимость:</b> от 35000 рублей\n"
                                      f"<b>Сроки:</b> от 7 дней</span>",
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
                                 text=f"Уже готовим мощщщное предложение💽\n\n"
                                      
                                      f"{check_base[str(message.from_user.id)]}\n"
                                      
                                      f"<span class='tg-spoiler'>Создаем уникальный дизайн и не работаем с шаблонными решениями. Перед тем, как написать 10 страниц кода, проводим 30 часов за анализом задач, которые он будет решать. Завершаем задачи в сроки и тестируем продукт, чтобы он работал как швейцарские часы.\n\n"
                                      f"<b>Стоимость:</b> от 35000 рублей\n"
                                      f"<b>Сроки:</b> от 7 дней</span>",
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
                                 text=f"Уже готовим мощщщное предложение💽\n\n"
                                      
                                      f"{check_base[str(message.from_user.id)]}\n"
                                      
                                      f"<span class='tg-spoiler'>Создаем уникальный дизайн и не работаем с шаблонными решениями. Перед тем, как написать 10 страниц кода, проводим 30 часов за анализом задач, которые он будет решать. Завершаем задачи в сроки и тестируем продукт, чтобы он работал как швейцарские часы.\n\n"
                                      f"<b>Стоимость:</b> от 35000 рублей\n"
                                      f"<b>Сроки:</b> от 7 дней</span>",
                                 reply_markup=ikb)

    await statisticbot.send_message(chat_id=admin, text=f"Новый рассчёт\n\n"
                                                        f"клиент: @{message.from_user.username}\n"
                                                        f"айди: {message.from_user.id}\n\n"
                                                        f"{check_base[str(message.from_user.id)]}")

    check_base[str(message.from_user.id)]=""

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

class Reklama(StatesGroup):
    reklama_text=State()
    reklama_photo=State()

async def reklama(message: types.Message):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    msg=await bot.send_message(chat_id=message.from_user.id, text="Отправь текст сообщения")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await Reklama.reklama_text.set()

@dp.message_handler(state=Reklama.reklama_text)
async def reklama_text(message: types.Message,state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await message.delete()
    await state.update_data(reklama_text=message.text)

    msg = await bot.send_message(chat_id=message.from_user.id, text="Скинь фото файлом")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await Reklama.reklama_photo.set()

reklama_base=["","photo.png"]
@dp.message_handler(state=Reklama.reklama_photo,content_types=ContentType.DOCUMENT)
async def reklama_text(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await message.delete()

    await message.document.download(destination_file=Path(dir_path, "photo.png"))

    await state.update_data(photo_place=Path(dir_path, "photo.png"))

    data = await state.get_data()
    await state.finish()

    reklama_base[0]=data["reklama_text"]
    photo=open(data["photo_place"],"rb")
    ikb=InlineKeyboardMarkup()
    btn1=InlineKeyboardButton(f"Отправить {len(id_base)} людям",callback_data="send_reklama")
    btn2=InlineKeyboardButton("Заново",callback_data="repeat_reklama")
    ikb.add(btn1).row(btn2)

    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=photo,
                               caption=data["reklama_text"],
                               reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

@dp.callback_query_handler(text="repeat_reklama")
async def repeat_reklama(message: types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    msg = await bot.send_message(chat_id=admin,text="работаю сэр")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)
    await reklama(message)

@dp.callback_query_handler(text="send_reklama")
async def send_reklama(message: types.Message):

    ikb = InlineKeyboardMarkup()
    btn1=InlineKeyboardButton("🫀 Наши услуги", callback_data="uslugi")
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn4).row(btn3)
    for i in id_base:

        if str(i) in last_msg_base:
            await bot.delete_message(chat_id=i, message_id=last_msg_base[str(i)])

        msg = await bot.send_photo(chat_id=str(i),
                                   photo=open(reklama_base[1], "rb"),
                                   caption=reklama_base[0],
                                   reply_markup=ikb)
        last_msg_base[str(i)] = str(msg.message_id)


    await statisticbot.send_message(chat_id=admin,
                                    text="Реклама отправлена")


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
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    ikb.add(btn1,btn2).row(btn4).row(btn3)

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
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    ikb.add(btn1, btn2).row(btn4).row(btn3)

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
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    ikb.add(btn1, btn2).row(btn4).row(btn3)

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

from cases import dir_path
#ЗАГРУЗКА АЙДИШНИКОВ
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def base_in(doc: types.Message):
    await bot.delete_message(chat_id=doc.from_user.id, message_id=last_msg_base[str(doc.from_user.id)])
    await doc.delete()
    file = await doc.document.download(destination_file=Path(dir_path,"users.txt"))
    for i in open("users.txt"):
        if i not in id_base and int(i) not in id_base:
            id_base.append(i.replace("\n",""))
    await statisticbot.send_message(chat_id=admin,text="База загружена")
    msg = await bot.send_message(chat_id=doc.from_user.id,text="База загружена")
    last_msg_base[str(doc.from_user.id)] = str(msg.message_id)
    await create_file()
    await statisticbot.send_document(chat_id=admin, document=open("idfile.txt", "rb"))


class Msg(StatesGroup):
    id_msg=State()
    text_msg=State()

async def send_msg(message):
    await message.delete()
    base="".join([str(i)+'\n' for i in id_base])
    if message.from_user.id==admin:
        await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
        msg=await message.answer(f"Введи айди получателя\n\n <code>{base}</code>")
        last_msg_base[str(message.from_user.id)] = str(msg.message_id)
    else:
        await start()

    await Msg.id_msg.set()

@dp.message_handler(state=Msg.id_msg)
async def send_msg1(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await message.delete()

    await state.update_data(id_user=message.text)

    msg=await message.answer("Введи текст сообщения")

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await Msg.text_msg.set()

@dp.message_handler(state=Msg.text_msg)
async def send_msg2(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    await message.delete()

    await state.update_data(text_msg=message.text)
    data = await state.get_data()
    await state.finish()

    msg = await bot.send_message(chat_id=data["id_user"],text=data["text_msg"])

    last_msg_base[str(data["id_user"])] = str(msg.message_id)

    msg = await statisticbot.send_message(chat_id=admin,
                                          text=f"Сообщение отправлено\n\n"
                                               f"<b>получатель</b>: <code>{data['id_user']}</code>\n"
                                               f"<b>текст</b>: {data['text_msg']}")
    msg=await bot.send_message(chat_id=message.from_user.id,text="Отправлено")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)



class PersonalReklama(StatesGroup):
    reklama_text=State()
    reklama_id=State()
    reklama_photo=State()

async def personal_reklama(message: types.Message):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])

    msg=await bot.send_message(chat_id=message.from_user.id, text="Отправь текст сообщения")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await PersonalReklama.reklama_text.set()

@dp.message_handler(state=PersonalReklama.reklama_text)
async def personal_id(message: types.Message,state:FSMContext):

    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await state.update_data(text=message.text)
    msg=await bot.send_message(chat_id=message.from_user.id, text="Отправь id получателя")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await PersonalReklama.reklama_id.set()

@dp.message_handler(state=PersonalReklama.reklama_id)
async def reklama_text(message: types.Message,state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await message.delete()
    await state.update_data(id=message.text)

    msg = await bot.send_message(chat_id=message.from_user.id, text="Скинь фото файлом")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

    await PersonalReklama.reklama_photo.set()

personal_reklama_base=["","photo.png",""]
@dp.message_handler(state=PersonalReklama.reklama_photo,content_types=ContentType.DOCUMENT)
async def reklama_text(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    await message.delete()

    await message.document.download(destination_file=Path(dir_path, "photo.png"))

    await state.update_data(photo_place=Path(dir_path, "photo.png"))

    data = await state.get_data()
    await state.finish()
    personal_reklama_base[2]=data["id"]
    personal_reklama_base[0]=str(data["text"])
    photo=open(data["photo_place"],"rb")
    ikb=InlineKeyboardMarkup()
    btn1=InlineKeyboardButton(f"Отправить {data['id']}",callback_data="send_reklama_personal")
    btn2=InlineKeyboardButton("Заново",callback_data="repeat_reklama_personal")
    ikb.add(btn1).row(btn2)

    msg = await bot.send_photo(chat_id=message.from_user.id,
                               photo=photo,
                               caption=data["text"],
                               reply_markup=ikb)

    last_msg_base[str(message.from_user.id)] = str(msg.message_id)

@dp.callback_query_handler(text="repeat_reklama_personal")
async def repeat_reklama(message: types.Message):
    await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
    msg = await bot.send_message(chat_id=admin,text="работаю сэр")
    last_msg_base[str(message.from_user.id)] = str(msg.message_id)
    await personal_reklama(message)

@dp.callback_query_handler(text="send_reklama_personal")
async def send_reklama(message: types.Message):

    ikb = InlineKeyboardMarkup()
    btn1=InlineKeyboardButton("🫀 Наши услуги", callback_data="uslugi")
    btn4 = InlineKeyboardButton('🧮 Рассчитать стоимость', callback_data="price")
    btn3 = InlineKeyboardButton("🗺 Главное меню", callback_data="mainmenu")
    ikb.row(btn1).row(btn4).row(btn3)

    if str(personal_reklama_base[2]) in last_msg_base:
        await bot.delete_message(chat_id=personal_reklama_base[2], message_id=last_msg_base[str(personal_reklama_base[2])])

    msg = await bot.send_photo(chat_id=str(personal_reklama_base[2]),
                                photo=open(reklama_base[1], "rb"),
                                caption=personal_reklama_base[0],
                                reply_markup=ikb)
    last_msg_base[str(personal_reklama_base[2])] = str(msg.message_id)


    await statisticbot.send_message(chat_id=admin,
                                    text="Реклама отправлена")

#ТЕКСТОВЫЕ КОМАНДЫ
@dp.message_handler()
async def menu(message: types.Message):
    if message.text=="🔗главное меню":
        await start(message)

    if message.from_user.id==admin:
        if message.text=="users":
            await create_file()
            await statisticbot.send_document(chat_id=admin, document=open("idfile.txt", "rb"))
            await statisticbot.send_document(chat_id=admin, document=open("userfile.txt", "rb"))

        elif message.text=="cjm":
            await message.delete()
            await get_put()
            await statisticbot.send_document(chat_id=admin, document=open("cjm.txt", "rb"))

        elif message.text=="reklama":
            await message.delete()
            await reklama(message)

        elif message.text == "msg":
            await send_msg(message)

        elif message.text=="personal":
            await personal_reklama(message)

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

