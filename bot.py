from aiogram import executor

import input_data
import time

from aiogram.dispatcher.filters import Text
from aiogram import types

import logging


from create_bot import dp,bot,db,avalible_boxes
from binance1.handlers import headers_is_right,send_requests_to_buy

from binance1.box import Box


logging.basicConfig(level=logging.INFO)

user_id = 0

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
        buttons = ["Config",'Start bot']
        keyboard.add(*buttons)
        await message.answer("Your subscription is active", reply_markup=keyboard) #сделать чтоб показывало до какого времени активна


input_data.register_handlers_data(dp)



@dp.message_handler(Text(equals="Start bot"))
async def main(message: types.Message):
    global user_id
    user_id = message.from_user.id
    time.sleep(3)
    selected_box = db.post_product_id(message.chat.id)
    if headers_is_right():
        await bot.send_message(message.chat.id, 'Successfully connected')
    else:
        await bot.send_message(message.chat.id, 'Something wrong...')
        await bot.send_message(message.chat.id, 'Check please: COOKIE, CSRFTOKEN')

    product_id = avalible_boxes[selected_box[0]]['product_id']
    box = Box(product_id=product_id, amount=selected_box[1])
    start_sale_time = box._get_start_sale_time
    await bot.send_message(message.chat.id, 'Waiting for start')
    await send_requests_to_buy(box, start_sale_time)




if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=False)