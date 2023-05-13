import asyncio
import logging

from aiogram import Bot, Dispatcher

from commands.routers import Command

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "5900604347:AAH8_8pwQ7Gz7oxdt3t1-FMorzPXGlnByyA"


# All handlers should be attached to the Router (or Dispatcher)

async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(Command.register_routers())
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    await bot.set_my_commands(Command.collect_my_commands())
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
