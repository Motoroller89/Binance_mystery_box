from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp,db







class FSMAdmin(StatesGroup):
    product_id = State()
    number = State()
    csrftoken = State()
    cookie = State()
    device_info = State()
    bnc_uuid = State()


async def enter_date(message: types.Message):
    if db.subscriber_exists(message.from_user.id):
        await FSMAdmin.product_id.set()
        await message.reply("Choose box")


async def load_product(message: types.Message, state: FSMContext):
    if db.subscriber_exists(message.from_user.id):
        async with state.proxy() as data:
            data['product_id'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter the number of boxes')


async def load_number(message: types.Message, state: FSMContext):
    if db.subscriber_exists(message.from_user.id):
        async with state.proxy() as data:
            data['number'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter csrftoken')


async def load_csrftoken(message: types.Message, state: FSMContext):
    if db.subscriber_exists(message.from_user.id):
        async with state.proxy() as data:
            data['csrftoken'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter cookie')


async def load_cookie(message: types.Message, state: FSMContext):
    if db.subscriber_exists(message.from_user.id):
        async with state.proxy() as data:
            data['cookie'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter device_info')


async def load_device_info(message: types.Message, state: FSMContext):
    if db.subscriber_exists(message.from_user.id):
        async with state.proxy() as data:
            data['device_info'] = message.text
        await FSMAdmin.next()
        await message.reply('Enter bnc_uuid')


async def load_bnc_uuid(message: types.Message, state: FSMContext):
    if db.subscriber_exists(message.from_user.id):
        async with state.proxy() as data:
            data['bnc_uuid'] = message.text

        async with state.proxy() as data:
            dictionary = data.as_dict()
            db.add_date(product_id= dictionary['product_id'],number=dictionary['number'],csrftoken=dictionary['csrftoken'],cookie=dictionary['cookie'],device_info=dictionary['device_info'],bnc_uuid=dictionary['bnc_uuid'], user_id=message.from_user.id)
            await message.reply(str(data))

        await state.finish()

async  def cansel_handler(message :types.Message, state :FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


def register_handlers_data(dp: Dispatcher):
    dp.register_message_handler(enter_date, Text(equals="Config"), state=None)
    dp.register_message_handler(load_product, state=FSMAdmin.product_id)
    dp.register_message_handler(load_number, state=FSMAdmin.number)
    dp.register_message_handler(load_csrftoken, state=FSMAdmin.csrftoken)
    dp.register_message_handler(load_cookie, state=FSMAdmin.cookie)
    dp.register_message_handler(load_device_info, state=FSMAdmin.device_info)
    dp.register_message_handler(load_bnc_uuid, state=FSMAdmin.bnc_uuid)
    dp.register_message_handler(cansel_handler, state="*", commands= 'отмена')
    dp.register_message_handler(cansel_handler, Text(equals='отмена', ignore_case= True), state="*")