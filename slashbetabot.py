from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


peoples_id=[]

bot=Bot(token="5856871549:AAFtXMLTLmtFMeZt57-wrsZHqhCEY8xz-LM",parse_mode="HTML")
dp=Dispatcher(bot)


kb1=InlineKeyboardMarkup(row_width=1)
btn1=InlineKeyboardButton(text="Группа Вконтакте",
                          url="https://vk.com/slashdigitalru")
kb1.add(btn1)

@dp.message_handler(commands="reklama")
async def reklama(message: types.Message):

    stroka = ""
    for i in peoples_id:
        stroka += i[0] + "\n"

    for id2 in range(len(peoples_id)):
        photo = open("bitva.png", "rb")
        await bot.send_photo(chat_id=peoples_id[id2][1],photo=photo,caption="Привет! На связи <b>SlashDigital</b> <code>{слэш диджитал}</code>\n\n"
                             "Мы занимаемся созданием сайтов, телеграмм ботов и дизайном социальных медиа\n\n"
                             "Дарим скидку <b>10%</b> на все услуги по промокоду <b>[битвакреаторов]</b>\n\n"
                             "<tg-spoiler>Напишите нам в ВК, чтобы воспользоваться</tg-spoiler>",
                             reply_markup=kb1)
        photo.close()

    await message.answer(text=f"{len(peoples_id)} сообщений отправлено\n"
                              f"{stroka}\n"
                              f"<code>[видно только вам]</code>")


@dp.message_handler(commands=["start"])
async def scam(message: types.Message):
    await message.answer("Поздравляю, вы стали жертвой партизанского маркетинга!")
    await bot.send_message(chat_id="5965231899",text=f"+1 вход @{message.from_user.username}\n")
    if ("@"+message.from_user.username, message.from_user.id) not in peoples_id:
        peoples_id.append(("@"+message.from_user.username, message.from_user.id))


@dp.message_handler(commands=["info"])
async def info(message: types.Message):
    for id in range(len(peoples_id)):
        await message.answer(text=f"{id+1}  =  {peoples_id[id][0]}")



@dp.message_handler()
async def golosboga(message: types.Message):
    if message.from_user.id==5965231899:

        stroka = ""
        for i in peoples_id:
            stroka += i[0] + "\n"

        for id1 in peoples_id:
            await bot.send_message(chat_id=id1[1],text=message.text)

        await message.answer(text=f"{len(peoples_id)} сообщений отправлено\n"
                                  f"{stroka}\n"
                                  f"<code>[видно только вам]</code>")

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
