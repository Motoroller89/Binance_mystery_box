from aiogram import executor
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging

import input_data

import input_data2
import input_data3
import input_code

import os
import threading

from create_bot import dp, bot, db
from binance1.handlers import headers_is_right, send_requests_to_buy
from box_date import avalible_boxes
from binance1.box import Box
from config import URL_APP

import asyncio
from datetime import datetime

logging.basicConfig(level=logging.INFO)


async def on_statrap(dp):
    await bot.set_webhook(URL_APP)


async def on_shourdown(dp):
    await bot.delete_webhook()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    try:
        if " " in message.text:
            referrer_candidate = message.text.split()[1]
            if not db.have_users(message.chat.id):
                db.add_invite(referrer_candidate)

        db.add_subscriber(message.chat.id, message.from_user.username)


    except:
        pass

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)


    buttons = ["Subscribe", "Contact Admin", 'Referral system', 'Our social media']

    keyboard.add(*buttons)

    await bot.send_message(message.chat.id, "Okay , let's start")


    await bot.send_message(message.chat.id, 'Click the «subscribe» button to subscribe to telegram bot ',
                           reply_markup=keyboard)




@dp.message_handler(Text(equals="Contact Admin"))
async def contact_admin(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Contact Admin", url='https://t.me/diachylum')
    markup.add(button1)
    await bot.send_message(message.chat.id, 'For all questions', reply_markup=markup)



@dp.message_handler(Text(equals='Referral system'))
async def referal(message: types.Message):
    try:
        db.add_referal(message.chat.id, message.from_user.username)
    except:
        pass

    if db.code_cheak(message.chat.id):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Create referral code", "How the referral system works?", 'Main menu']
        keyboard.add(*buttons)
        await bot.send_message(message.chat.id, 'Referral account partner ProMint bot',
                               reply_markup=keyboard)

    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ['View referral code', "Referral statistics", "How the referral system works?", 'Main menu']
        keyboard.add(*buttons)
        await bot.send_message(message.chat.id, 'Referral account partner ProMint bot',
                               reply_markup=keyboard)


@dp.message_handler(Text(equals='View referral code'))
async def referal(message: types.Message):
    await bot.send_message(message.chat.id, f'https://t.me/Binance_nftbox_bot?start={db.return_code(message.chat.id)}')


@dp.message_handler(Text(equals='Referral statistics'))
async def referal_stas(message: types.Message):
    await bot.send_message(message.chat.id, f'Unique members total invited: {db.return_users(message.chat.id)}\n\n'
                                            f'Members who combined payment: 0\n\n'
                                            f'Total earned: $0.00.\n\n'
                                            f'Withdrawn from the referral system: $0.00.\n\n'
                                            f'Referral system balance: $0.00')



@dp.message_handler(Text(equals="Main menu"))
async def check_media(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Subscribe", "Contact Admin", 'Referral system', 'Our social media']
    keyboard.add(*buttons)
    await bot.send_message(message.chat.id, 'Go to main menu',
                           reply_markup=keyboard)


@dp.message_handler(Text(equals="How the referral system works?"))
async def check_media(message: types.Message):
    await bot.send_message(message.chat.id,
                           '💰Invite your friends and acquaintances to ProMint Bot, earn real money!\n\nWhat bonuses do we give:\n\n''🧑🏻‍💻 To you:\n'
                           'For each referred user who purchases a subscription from the academy, you will receive 10% of the price of their subscription, and you will also receive 10% every time your friend renews their subscription.\n'
                           '\n🧑‍💼 To Friend:\n'
                           'For entering your referral code, a new user will receive a $5 discount on payment.\n'
                           'Payments for the referral system are made once a week in manual mode, after submitting a withdrawal request.')


input_code.register_handlers_code(dp)



@dp.message_handler(Text(equals="Our social media"))
async def check_media(message: types.Message):
    markup1 = types.InlineKeyboardMarkup()
    button2 = types.InlineKeyboardButton("YouTube", url='https://www.youtube.com/channel/UCzkzcIX9Bdi8VvRwKovygMQ')
    markup1.add(button2)
    await bot.send_message(message.chat.id, "Follow us", reply_markup=markup1)


@dp.message_handler(Text(equals="Subscribe"))
async def check_subscription(message: types.Message):
    if not (db.subscriber_exists(message.from_user.id)):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Admin", url='https://t.me/diachylum')
        markup.add(button1)
        await bot.send_message(message.chat.id, "To subscribe , write to the admin in a private message",
                               reply_markup=markup)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Config", 'Start bot','Main menu']
        keyboard.add(*buttons)
        await message.answer("Your subscription is active",
                             reply_markup=keyboard)  # сделать чтоб показывало до какого времени активна



@dp.message_handler(Text(equals="Config"))
async def conf(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["USER №1", "USER №2", 'USER №3', 'Reload input data', 'Сome back']
    keyboard.add(*buttons)
    await bot.send_message(message.chat.id, 'Choose user',
                           reply_markup=keyboard)


input_data.register_handlers_data(dp)
input_data2.register_handlers_data2(dp)
input_data3.register_handlers_data3(dp)


@dp.message_handler(Text(equals="Сome back"))
async def conf(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Config", 'Start bot', 'Main menu']
    keyboard.add(*buttons)
    await message.answer("We have returned",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Start bot"))
async def conf(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Start 1 account", "Start 2 account", "Start 3 account", 'Сome back']
    keyboard.add(*buttons)
    await message.answer("We have returned",
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Start 1 account"))
async def account1(message: types.Message):
    if db.subscriber_exists(message.from_user.id):
        try:
            selected_box = db.post_product_id(message.chat.id, account='')

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


@dp.message_handler(Text(equals="Start 2 account"))
async def account2(message: types.Message):
    if db.subscriber_exists(message.from_user.id):
        try:
            selected_box = db.post_product_id(message.chat.id, account='2')

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


@dp.message_handler(Text(equals="Start 3 account"))
async def account3(message: types.Message):
    if db.subscriber_exists_super_sub(message.from_user.id):
        pass
    else:
        await bot.send_message(message.chat.id,
                               'You need to increase your subscription level, contact the administrator',
                               reply_markup=InlineKeyboardMarkup(). \
                               add(InlineKeyboardButton("Contact Admin", url='https://t.me/diachylum')))



async def scheduled(wait_for):
    while True:

        await asyncio.sleep(wait_for)

        new_box = avalible_boxes

        if len(new_box) != 0:
            for i in range(len(new_box)):

                news = new_box[f'{i + 1}']
                if not db.check_name_box(news['name']):
                    db.add_name_box(news['name'])
                    ts = news["starttime"] / 1000
                    time = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

                    date_user_id = db.get_all_user_id()
                    for id in date_user_id:

                        await bot.send_photo(id[0],
                                             f"{news['image']}",
                                             f'NEW BOX!!!\n'
                                             f'{news["name"]}\n'
                                             f'Count : {news["store"]}\n'
                                             f'price : {news["price"]} {news["currency"]}\n'
                                             f'Start: {time}\n'
                                             f'https://www.binance.com/ru/nft/mystery-box/detail?productId={news["product_id"]}&number=1',
                                             )

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(3600))
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_statrap,
        on_shutdown=on_shourdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 5000)),
    )
