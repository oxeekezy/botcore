from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler


async def _test_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        'Ok i\'am here!'
    )


def _add_handler(app: Application, handler, trigger_text: str):
    app.add_handler(CommandHandler(trigger_text, handler))


class TgBotCore:
    _token: str = ''
    _handlers: dict = None
    _application: Application = None

    def __init__(self, token: str, handlers: dict = None):
        self._token = token
        self._handlers = handlers
        self._handlers['test'] = _test_handler
        self._application = Application.builder().token(self._token).build()

    def add_custom_handlers(self):
        for handler in self._handlers.keys():
            _add_handler(self._application, self._handlers.get(handler), handler)

        return self

    def run(self):
        self._application.run_polling()


