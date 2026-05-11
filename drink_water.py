import asyncio
from telegram import Bot

TOKEN = "8798118154:AAFHLysUdYJH03UUmW3y8LEDbzOBSAfYwXQ"
CHAT_ID = "5336869933"

bot = Bot(token=TOKEN)

async def reminder():
    print("Bot Started")

    while True:
        await bot.send_message(
            chat_id=5336869933,
            text="💧 Drink Water!"
        )

        print("Message Sent")

        await asyncio.sleep(10)

asyncio.run(reminder())