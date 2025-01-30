import asyncio
import logging
from bot_config import bot, dp
from handlers.group_admin import admin_router


async def main():
    dp.include_router(admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
