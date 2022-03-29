from aiogram import executor
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

import input_data
import threading
import os

from create_bot import dp, bot, db
from binance1.handlers import headers_is_right, send_requests_to_buy
from box_date import avalible_boxes
from binance1.box import Box
from config import URL_APP

logging.basicConfig(level=logging.INFO)


async def on_statrap(dp):
    await bot.set_webhook(URL_APP)

async def on_shourdown(dp):
    await bot.delete_webhook()

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    try:
        db.add_subscriber(message.chat.id, message.from_user.username)
    except:
        pass

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Subscribe", "Contact Admin",'Our social media']
    keyboard.add(*buttons)

    await bot.send_message(message.chat.id,"Okay , let's start")

    await bot.send_message(message.chat.id, 'Click the «subscribe» button to subscribe to telegram bot ',reply_markup=keyboard)


@dp.message_handler(Text(equals="Contact Admin"))
async def contact_admin(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Contact Admin", url='https://t.me/diachylum')
    markup.add(button1)
    await bot.send_message(message.chat.id,'For all questions', reply_markup=markup)


@dp.message_handler(Text(equals="Subscribe"))
async def check_subscription(message: types.Message):
    if not (db.subscriber_exists(message.from_user.id)):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Admin", url='https://t.me/diachylum')
        markup.add(button1)
        await bot.send_message(message.chat.id, "To subscribe , write to the admin in a private message",reply_markup=markup)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Config", 'Start bot']
        keyboard.add(*buttons)
        await message.answer("Your subscription is active",
                             reply_markup=keyboard)  # сделать чтоб показывало до какого времени активна



@dp.message_handler(Text(equals="Our social media"))
async def check_media(message: types.Message):
    markup1 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("YouTube", url='https://www.youtube.com/channel/UCzkzcIX9Bdi8VvRwKovygMQ')
    markup1.add(button2)
    await bot.send_message(message.chat.id, "Follow us", reply_markup=markup1)


input_data.register_handlers_data(dp)


@dp.message_handler(Text(equals="Start bot"))
async def main(message: types.Message):
    if db.subscriber_exists(message.from_user.id):
        try:
            selected_box = db.post_product_id(message.chat.id)

            if headers_is_right(id=message.chat.id):

                await bot.send_message(message.chat.id, 'Successfully connected')

                product_id = avalible_boxes[selected_box[0]]['product_id']
                box = Box(product_id=product_id, amount=selected_box[1], id=message.chat.id)
                start_sale_time = box._get_start_sale_time
                send = threading.Thread(target=send_requests_to_buy,
                                        args=(box, start_sale_time,))

                await bot.send_message(message.chat.id, 'Waiting for start')
                send.start()

                # await send_requests_to_buy(box, start_sale_time)




            else:
                await bot.send_message(message.chat.id, 'Something wrong...')
                await bot.send_message(message.chat.id, 'Check please: COOKIE, CSRFTOKEN')



        except AttributeError:
            await bot.send_message(message.chat.id, 'First, fill in the data by clicking on the button Config')


    else:
        await bot.send_message(message.chat.id, 'Subscription has expired. You can renew by writing to the admin',
                               reply_markup=InlineKeyboardMarkup(). \
                               add(InlineKeyboardButton("Contact Admin", url='https://t.me/diachylum')))


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path= '',
        on_startup= on_statrap,
        on_shutdown= on_shourdown,
        skip_updates= True,
        host = '0.0.0.0',
        port = int(os.environ.get("PORT",5000)),
        )
