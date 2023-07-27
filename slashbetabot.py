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
    await message.answer("Привет! Отправь номер снилс в формате 15017702930 и я автоматически посчитаю твоё актуальное место с учётом приоритетов\n\n"
                         "<code>Чем ниже твои баллы, тем дольше я буду считать. Это займёт пару минут</code>")


@dp.message_handler(commands=["users"])
async def razrab(message: types.Message):
    for i in range(len(peoples_id)):
        await bot.send_message(chat_id="5965231899", text=peoples_id[i])

@dp.message_handler()
async def schet(message: types.Message):
    
    await message.answer(chance(message.text))
    await bot.send_message(chat_id="5965231899", text="посчитал")


if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
