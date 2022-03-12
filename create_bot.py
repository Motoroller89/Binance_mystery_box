from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from database import PostgreSql
from binance1.box import BaseBox


storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
db = PostgreSql('Binance_bot.db')






box_info = BaseBox()
avalible_boxes = box_info.get_avalible_boxes()