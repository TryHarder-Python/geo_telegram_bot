from aiogram import Router
from aiogram.types import BotCommand


class Command:
    router = Router()
    commands = {
        'start': 'Start the bot',
        'get_location': 'Get saved location',
    }

    @classmethod
    def register_routers(cls) -> Router:
        """
        This function register all routers in the project
        """
        from handlers import start

        # Create a router and register all handlers from all routers

        cls.router.include_router(start.start_router)
        return cls.router

    @classmethod
    def collect_my_commands(cls) -> list:
        """
        This function collect all commands from all routers
        """
        return [
            BotCommand(command=command, description=description)
            for command, description in cls.commands.items()
        ]
