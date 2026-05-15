from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from btn7 import aichat

api = ''
bot = Bot(api)
dp=Dispatcher()




@dp.message(Command("start"))
async def salem(sms: types.Message):
    await sms.answer(text='вопрос')

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa




@dp.message()
async def ai_chat(message: types.Message):
    user_text = message.text
    response = await aichat(user_text)
    await message.answer(response)





async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
