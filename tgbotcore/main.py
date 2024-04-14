from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


class Tgbot:
    _token = ''
    _dispatcher = None
    _parse_mode = ParseMode.HTML

    def __init__(self, token):
        self._token = token
        self._dispatcher = Dispatcher()

    async def start(self):
        bot = Bot(token=self._token, default=DefaultBotProperties(parse_mode=self._parse_mode))
        await self._dispatcher.start_polling(bot)
