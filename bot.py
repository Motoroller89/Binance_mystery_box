from aiogram.types import update

from aiogram import  Dispatcher, types, executor

import input_data

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types

import logging

from create_bot import dp,bot,db

logging.basicConfig(level=logging.INFO)







@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["check subscription", "Contact Admin"]
    keyboard.add(*buttons)
    await message.answer("Ты попал в лучший ...", reply_markup=keyboard)

@dp.message_handler(Text(equals="Contact Admin"))
async def contact_admin(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Contact Admin", url='https://t.me/d_gn1')
    markup.add(button1)
    await bot.send_message(message.chat.id, "For all questions, please contact us 👇", reply_markup=markup)


@dp.message_handler(Text(equals="check subscription"))
async def check_subscription(message: types.Message):
    if not(db.subscriber_exists(message.from_user.id)):
        await message.reply("You don't have a subscription. Contact seller")
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Config",'start bot']
        keyboard.add(*buttons)
        await message.answer("Your subscription is active", reply_markup=keyboard) #сделать чтоб показывало до какого времени активна


input_data.register_handlers_data(dp)






#@dp.message_handler(Text(equals="start bot"))
#async def with_puree(message: types.Message):
#    pass


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False)