from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
import logging
import asyncio
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from btn9 import menu5,contact, menu4,telefonlar,sagatlar,rolex,gucci
from datas9 import add_to_db, show_users




class RegState(StatesGroup):
    name=State()
    phone=State()
    adress=State()
    reklama=State()

class ToAdminState(StatesGroup):
    name=State()
    adres=State()
    photo=State()




admin='8177375903'
api = '8777704401:AAHT6hTiuarrTHoO9TbLTzrbBbxZqbkVFwc'
bot = Bot(api)
dp=Dispatcher()





@dp.message(Command("start"))
async def send_salem(sms: types.Message):
    await sms.answer(text=f"Salem {sms.from_user.first_name}",
                     reply_markup=menu5)


@dp.message(F.text == 'R')
async def start(sms: types.Message, state: FSMContext):
    await sms.answer('название рекламы:')
    await state.set_state(ToAdminState.name)

@dp.message(ToAdminState.name)
async def ati(sms: types.Message, state: FSMContext):
    await state.update_data(name=sms.text)
    await sms.answer("text:")
    await state.set_state(ToAdminState.adres)



@dp.message(ToAdminState.adres)
async def address(sms: types.Message, state: FSMContext):
    await state.update_data(adres=sms.text)
    await sms.answer("foto tasta:")
    await state.set_state(ToAdminState.photo)



@dp.message(ToAdminState.photo)
async def photo(sms: types.Message, state: FSMContext):
    await state.update_data(photo=sms.photo[-1].file_id)
    data = await state.get_data()
    users=await show_users()
    for i in users:
        await bot.send_photo(
            chat_id=i,
            photo=data['photo'],
            caption=f"""
    {data['name']}
    {data['adres']}
    """
    )
    await state.clear()


@dp.message(Command("start"))
async def send_salem(sms: types.Message):
    await sms.answer(text="Salem",
                     reply_markup=menu5)
@dp.message(F.text == 'Registraciya')
async def start_reg(sms: types.Message, state: FSMContext):
    await sms.answer("atingdi jaz:")
    await state.set_state()
    await state.set_state(RegState.name)
@dp.message(RegState.name)
async def ati(sms: types.Message, state: FSMContext):
    await state.update_data(ati=sms.text)
    await sms.answer("nomer tasta:",
                     reply_markup=contact)
    await state.set_state(RegState.phone)
@dp.message(RegState.phone)
async def familiya(sms: types.Message, state: FSMContext):
    phone = sms.contact.phone_number
    await state.update_data(nomer=phone)
    await sms.answer("adres jbering")
    await state.set_state(RegState.adress)
@dp.message(RegState.adress)
async def save_all(sms: types.Message, state: FSMContext):
    await state.update_data(adress=sms.text)
    datas=await state.get_data()
    await state.clear()
    await add_to_db(
        id=sms.from_user.id,
        name=datas['ati'],
        phone=datas['nomer'],
        adress=datas['adress']
        )



@dp.message(F.text=='Tovarlar')
async def send_salem(sms:types.Message):
    await sms.answer('sagat turleri',
                     reply_markup=sagatlar)







@dp.callback_query(F.data == 'rolex')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo='https://avatars.mds.yandex.net/i?id=06088dbd17c5839a61fcfe83a97a2608ea4db3e8-5296782-images-thumbs&n=13',
        caption="rolex turleri",
        reply_markup=rolex
    )
    await call.answer()






@dp.callback_query(F.data == 'gucci')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo='https://avatars.mds.yandex.net/i?id=efd9ce854b0762988f0bf18d196b49c1931777b9-5440253-images-thumbs&n=13',
        caption="gucci turleri",
        reply_markup=gucci
    )
    await call.answer()





@dp.callback_query(F.data == 'nazad')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        reply_markup=menu5
    )
    await call.answer()



@dp.callback_query(F.data == 'r1')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo='https://avatars.mds.yandex.net/i?id=0138ec40361c99500374a3b16736180932e68738-4429870-images-thumbs&n=13',
        caption="1.200.000"
    )
    await call.answer()


@dp.callback_query(F.data == 'r2')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo='https://avatars.mds.yandex.net/i?id=d05969e422d560503a780f97ebc42354a138370b-5245014-images-thumbs&n=13',
        caption="34.444.555"
    )
    await call.answer()

@dp.callback_query(F.data == 'g1')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo='https://avatars.mds.yandex.net/i?id=421bd55c1dff7d61a302df4a36ab8b7cf4b6420d-4987522-images-thumbs&n=13',
        caption="56.000.000"
    )
    await call.answer()

@dp.callback_query(F.data == 'g2')
async def batan(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo='https://avatars.mds.yandex.net/i?id=c1c3efcea871e131353cb5d96d7e789c238567f5-4600186-images-thumbs&n=13',
        caption="12.400.000"
    )
    await call.answer()




async def main():
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())