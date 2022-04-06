from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from create_bot import db, bot
from box_date import avalible_boxes


class FSMAdmin3(StatesGroup):
    product_id = State()
    number = State()
    csrftoken = State()
    cookie = State()
    device_info = State()
    bnc_uuid = State()


async def enter_date3(message: types.Message):
    if db.subscriber_exists_super_sub(message.from_user.id):
        await FSMAdmin3.product_id.set()
        await bot.send_message(message.chat.id, "Active boxes :")
        for i in range(len(avalible_boxes)):
            await bot.send_message(message.chat.id, f"{i + 1}." + ' ' + avalible_boxes[f'{i + 1}']['name'])
        await bot.send_message(message.chat.id, 'Select the number of the desired box')

    else:
        await bot.send_message(message.chat.id, 'You need to increase your subscription level, contact the administrator',
                               reply_markup=InlineKeyboardMarkup(). \
                               add(InlineKeyboardButton("Contact Admin", url='https://t.me/diachylum')))


async def cansel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.chat.id, 'Input canceled')


async def load_product3(message: types.Message, state: FSMContext):
    if db.subscriber_exists_super_sub(message.from_user.id):
        async with state.proxy() as data:
            data['product_id'] = message.text

        await FSMAdmin3.next()
        await bot.send_message(message.chat.id, 'Enter the number of boxes')


async def load_number3(message: types.Message, state: FSMContext):
    if db.subscriber_exists_super_sub(message.from_user.id):
        async with state.proxy() as data:
            data['number'] = int(message.text)
        await FSMAdmin3.next()
        await bot.send_message(message.chat.id, 'Enter csrftoken')


async def load_csrftoken3(message: types.Message, state: FSMContext):
    if db.subscriber_exists_super_sub(message.from_user.id):
        async with state.proxy() as data:
            data['csrftoken'] = message.text
        await FSMAdmin3.next()
        await bot.send_message(message.chat.id, 'Enter cookie')


async def load_cookie3(message: types.Message, state: FSMContext):
    if db.subscriber_exists_super_sub(message.from_user.id):
        async with state.proxy() as data:
            data['cookie'] = message.text
        await FSMAdmin3.next()
        await bot.send_message(message.chat.id, 'Enter device_info')


async def load_device_info3(message: types.Message, state: FSMContext):
    if db.subscriber_exists_super_sub(message.from_user.id):
        async with state.proxy() as data:
            data['device_info'] = message.text
        await FSMAdmin3.next()
        await bot.send_message(message.chat.id, 'Enter bnc_uuid')


async def load_bnc_uuid3(message: types.Message, state: FSMContext):
    if db.subscriber_exists_super_sub(message.from_user.id):
        async with state.proxy() as data:
            data['bnc_uuid'] = message.text

        async with state.proxy() as data:
            dictionary = data.as_dict()
            try:
                db.add_date(product_id=dictionary['product_id'], number=dictionary['number'],
                            csrftoken=dictionary['csrftoken'], cookie=dictionary['cookie'],
                            device_info=dictionary['device_info'], bnc_uuid=dictionary['bnc_uuid'],
                            user_id=message.from_user.id,nomer='3')
                await bot.send_message(message.from_user.id, 'Data entry is complete.')
            except:
                await bot.send_message(message.chat.id, 'Data entered incorrectly, please try again')

        await state.finish()


def register_handlers_data3(dp: Dispatcher):
    dp.register_message_handler(enter_date3, Text(equals="USER №3"), state=None)
    dp.register_message_handler(cansel_handler, state="*", commands='отмена')
    dp.register_message_handler(cansel_handler, Text(equals='stop', ignore_case=True), state="*")
    dp.register_message_handler(load_product3, state=FSMAdmin3.product_id)
    dp.register_message_handler(load_number3, state=FSMAdmin3.number)
    dp.register_message_handler(load_csrftoken3, state=FSMAdmin3.csrftoken)
    dp.register_message_handler(load_cookie3, state=FSMAdmin3.cookie)
    dp.register_message_handler(load_device_info3, state=FSMAdmin3.device_info)
    dp.register_message_handler(load_bnc_uuid3, state=FSMAdmin3.bnc_uuid)
