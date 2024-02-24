import asyncio

import aiogram
from aiogram import Bot, Dispatcher, types

# Create the bot object.
bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

# Create an event loop.
loop = asyncio.get_event_loop()

# Create the dispatcher object.
dp = Dispatcher(bot, loop=loop)

# Handle the '/start' command.
@dp.message_handler(commands=['start'])
async def send_hello(message: types.Message):
    await message.answer('hiiiiiii!')


if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.run_until_complete(stop())
