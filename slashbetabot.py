from aiogram import Bot, Dispatcher, types
from aiogram import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from fnmatch import fnmatch
from functionfile import chance

peoples_id=[]

bot=Bot("6233960605:AAFiiu2k_HZFN27vFvbZ8ITCtNcxRzFcxRA",parse_mode="HTML")
dp=Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(chat_id="5965231899", text="вход")
    peoples_id.append("@"+message.from_user.username+"\n")
    await message.answer("Привет! Отправь номер снилс в формате 15017702931 и я автоматически посчитаю твоё актуальное место с учётом приоритетов\n\n"
                         "<code>Чем ниже твои баллы, тем дольше я буду считать. Это займёт пару минут</code>")


@dp.message_handler(commands=["users"])
async def razrab(message: types.Message):
    for i in range(len(peoples_id)):
        await bot.send_message(chat_id="5965231899", text=peoples_id[i])

@dp.message_handler()
async def schet(message: types.Message):
    if len(message.text)==11:
        await message.answer("ща посчитаю")
        await message.answer(chance(message.text))
        await bot.send_message(chat_id="5965231899", text=f"посчитал, @{message.from_user.username}\n{message.text}")
    else:
        await message.answer("ты что-то не то ввёл, давай ещё раз")
        await bot.send_message(chat_id="5965231899", text=f"ошибка: {message.text}")


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
