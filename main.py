import asyncio
from ping3 import ping
from telegram import Bot

TOKEN = 8454012215
CHAT_ID = 312486348
HOST = 46.219.211.190

CHECK_INTERVAL = 30

bot = Bot(token=TOKEN)
last_status = None

async def monitor():
    global last_status
    while True:
        alive = ping(HOST, timeout=2) is not None

        if alive != last_status:
            if alive:
                await bot.send_message(CHAT_ID, "✅ Роутер доступен — питание есть.")
            else:
                await bot.send_message(CHAT_ID, "❌ Роутер недоступен! Возможно пропало питание.")
            last_status = alive

        await asyncio.sleep(CHECK_INTERVAL)

asyncio.run(monitor())
