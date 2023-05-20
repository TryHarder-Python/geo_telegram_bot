import asyncio
import logging

from aiogram import Dispatcher

from routers import Command
from settings import STORAGE, BOT


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher(storage=STORAGE)
    dp.include_router(Command.register_routers())
    await BOT.set_my_commands(Command.collect_my_commands())
    await dp.start_polling(BOT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
