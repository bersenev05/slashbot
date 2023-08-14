
id_base=[]
username_base=[]
put_msg_base={}

async def create_file():

    file_id=open("idfile.txt","w+")
    file_users=open("userfile.txt","w+")

    for i in id_base:
        file_id.write(str(i)+"\n")

    for i in username_base:
        file_users.write(str(i)+"\n")

    file_id.close()
    file_users.close()

async def get_put():
    file_users_map=open("cjm.txt","w+")
    for i in range(len(id_base)):
        file_users_map.write(str(username_base[i])+"\n")
        file_users_map.write(str(id_base[i])+"\n")
        file_users_map.write(put_msg_base[str(id_base[i])])
        file_users_map.write("---------\n\n")
    file_users_map.close()


# # РАССЧИТАТЬ СТОИМОСТЬ - сайт - (какие цели?)
# @dp.callback_query_handler(text="buysite")
# async def buysite(message: types.CallbackQuery):
#     await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
#
#     ikb = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("💵 Продать товар", callback_data="answer_tovar")
#     btn12 = InlineKeyboardButton("💶 Продать услугу", callback_data="answer_usluga")
#     btn2 = InlineKeyboardButton("📱 Получить контакты", callback_data="answer_contacts")
#     btn3 = InlineKeyboardButton("📎 Другое", callback_data="answer_more")
#     ikb.row(btn12).row(btn1).row(btn2).row(btn3)
#
#     msg = await bot.send_message(chat_id=message.from_user.id,
#                                  text="Что будет главной целью сайта?",
#                                  reply_markup=ikb)
#     await get_time()
#     put_msg_base[str(message.from_user.id)] += (f"Хочет сайт: {time}\n")
#
#     last_msg = msg.message_id
#     last_msg_base[str(message.from_user.id)] = str(last_msg)
#
#
# # РАССЧИТАТЬ СТОИМОСТЬ сайт - продать товар - (сколько товаров?)
# @dp.callback_query_handler(text="answer_tovar")
# async def buysite(message: types.CallbackQuery):
#     await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
#
#     ikb = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("менее 20", callback_data="answer_tovar_menee20")
#     btn2 = InlineKeyboardButton("20 - 50", callback_data="answer_tovar_20-50")
#     btn3 = InlineKeyboardButton("более 50", callback_data="answer_tovar_bolee50")
#     ikb.row(btn1).row(btn2).row(btn3)
#
#     msg = await bot.send_message(chat_id=message.from_user.id,
#                                  text="Сколько будет товаров на сайте?",
#                                  reply_markup=ikb)
#     await get_time()
#     put_msg_base[str(message.from_user.id)] += (f"Цель сайта - продать товар: {time}\n")
#
#     last_msg = msg.message_id
#     last_msg_base[str(message.from_user.id)] = str(last_msg)
#
#
# # РАССЧИТАТЬ СТОИМОСТЬ сайт - продать товар - менее 20
# @dp.callback_query_handler(text="answer_tovar_menee20")
# async def buysite(message: types.CallbackQuery):
#     await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
#
#     ikb = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("да", callback_data="answer_tovar_menee20_yes")
#     btn2 = InlineKeyboardButton("нет", callback_data="answer_tovar_menee20_no")
#     ikb.row(btn1).row(btn2)
#
#     msg = await bot.send_message(chat_id=message.from_user.id,
#                                  text="Нужна ли будет онлайн оплата?",
#                                  reply_markup=ikb)
#     await get_time()
#     put_msg_base[str(message.from_user.id)] += (f"Будет менее 20 товаров: {time}\n")
#
#     last_msg = msg.message_id
#     last_msg_base[str(message.from_user.id)] = str(last_msg)
#
#
# # РАССЧИТАТЬ СТОИМОСТЬ - сайт - продать товар - 20-50
# @dp.callback_query_handler(text="answer_tovar_20-50")
# async def buysite(message: types.CallbackQuery):
#     await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
#
#     ikb = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("да", callback_data="answer_tovar_2050_yes")
#     btn2 = InlineKeyboardButton("нет", callback_data="answer_tovar_2050_no")
#     ikb.row(btn1).row(btn2)
#
#     msg = await bot.send_message(chat_id=message.from_user.id,
#                                  text="Нужна ли будет онлайн оплата?",
#                                  reply_markup=ikb)
#     await get_time()
#     put_msg_base[str(message.from_user.id)] += (f"Будет 20-50 товаров: {time}\n")
#
#     last_msg = msg.message_id
#     last_msg_base[str(message.from_user.id)] = str(last_msg)
#
#
# # РАССЧИТАТЬ СТОИМОСТЬ - сайт - продать товар - более 50
# @dp.callback_query_handler(text="answer_tovar_bolee50")
# async def buysite(message: types.CallbackQuery):
#     await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
#
#     ikb = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("да", callback_data="answer_tovar_bolee50_yes")
#     btn2 = InlineKeyboardButton("нет", callback_data="answer_tovar_bolee50_no")
#     ikb.row(btn1).row(btn2)
#
#     msg = await bot.send_message(chat_id=message.from_user.id,
#                                  text="Нужна ли будет онлайн оплата?",
#                                  reply_markup=ikb)
#     await get_time()
#     put_msg_base[str(message.from_user.id)] += (f"Будет более 50 товаров: {time}\n")
#
#     last_msg = msg.message_id
#     last_msg_base[str(message.from_user.id)] = str(last_msg)
#
#
# # РАССЧИТАТЬ СТОИМОСТЬ - сайт - продать товар - более 50
# @dp.callback_query_handler(text=["answer_tovar_bolee50_yes",
#                                  "answer_tovar_bolee50_no",
#                                  "answer_tovar_menee50_yes",
#                                  "answer_tovar_menee50_no",
#                                  "answer_tovar_2050_yes",
#                                  "answer_tovar_2050_no"])
# async def buysite(message: types.CallbackQuery):
#     await bot.delete_message(chat_id=message.from_user.id, message_id=last_msg_base[str(message.from_user.id)])
#     await get_time()
#     callback_data = message.data
#     if callback_data == "answer_tovar_bolee50_yes":
#         put_msg_base[str(message.from_user.id)] += (f"Нужна онлайн оплата: {time}\n")
#
#     ikb = InlineKeyboardMarkup()
#     btn1 = InlineKeyboardButton("да", callback_data="answer_tovar_bolee50_yes")
#     btn2 = InlineKeyboardButton("нет", callback_data="answer_tovar_bolee50_no")
#     ikb.row(btn1).row(btn2)
#
#     msg = await bot.send_message(chat_id=message.from_user.id,
#                                  text="Есть ли сммщик?",
#                                  reply_markup=ikb)
#
#     last_msg = msg.message_id
#     last_msg_base[str(message.from_user.id)] = str(last_msg)