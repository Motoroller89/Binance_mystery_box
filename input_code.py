from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_bot import db, bot

class FSMAdmin(StatesGroup):
    code = State()

async def enter_date(message: types.Message):
        await FSMAdmin.code.set()
        await bot.send_message(message.chat.id, "Enter the name of your referral code:")

async def load_code(message: types.Message, state: FSMContext):
        try:
            db.add_code(user_id=message.from_user.id,code=message.text)
            await bot.send_message(message.chat.id, 'Referral code successfully set!\n'
                                                'You can invite people through this link:\n'
                                                f'https://t.me/Binance_nftbox_bot?start={message.text}')
        except:
            await bot.send_message(message.chat.id,'Enter another code')

        await state.finish()




def register_handlers_code(dp: Dispatcher):
    dp.register_message_handler(enter_date, Text(equals="Create referral code"), state=None)
    dp.register_message_handler(load_code, state=FSMAdmin.code)
