from aiogram import Bot, Dispatcher, types
from aiogram import executor

peoples_id=[]

bot=Bot(token="5856871549:AAFtXMLTLmtFMeZt57-wrsZHqhCEY8xz-LM",parse_mode="HTML")
dp=Dispatcher(bot)

@dp.message_handler(commands="reklama")
async def reklama(message: types.Message):
    for id2 in range(len(peoples_id)):
        await bot.send_message(chat_id=peoples_id[id2][1], text="Привет! На связи <code>{слэшдиджитал}</code>\n"
                             "мы занимаемся созданием сайтов, телеграмм ботов и дизайном социальных медиа\n\n"
                             "<b>Сайт</b> slashdigital.ru\n"
                             "<b>ВК</b> vk.com/slashdigitalru")

@dp.message_handler(commands=["start"])
async def scam(message: types.Message):
    await message.answer("Поздравляю, вы стали жертвой партизанского маркетинга!")
    await bot.send_message(chat_id="5965231899",text=f"ник=@{message.from_user.username}\n"
                                                     f"имя={message.from_user.first_name} {message.from_user.last_name}\n")
    if ("@"+message.from_user.username, message.from_user.id) not in peoples_id:
        peoples_id.append(("@"+message.from_user.username, message.from_user.id))

@dp.message_handler(commands=["info"])
async def info(message: types.Message):
    for id in range(len(peoples_id)):
        await message.answer(text=f"{id+1}  =  {peoples_id[id][0]}")


@dp.message_handler()
async def golosboga(message: types.Message):
    if message.from_user.id==5965231899:
        for id1 in peoples_id:
            await bot.send_message(chat_id=id1[1],text=message.text)
            await message.answer(text=f"отправлено {id1[0]}")

if __name__=="__main__":
    executor.start_polling(dp)