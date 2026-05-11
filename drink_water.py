import asyncio
from telegram import Bot

TOKEN = "8798118154:AAFHLysUdYJH03UUmW3y8LEDbzOBSAfYwXQ"
CHAT_ID = "5336869933"

bot = Bot(token=TOKEN)

async def water_reminder():
    while True:
        await bot.send_message(
            chat_id=CHAT_ID,
            text="💧 Water Taagu"
        )

        # 1.5 hours
        await asyncio.sleep(3600)

asyncio.run(water_reminder())