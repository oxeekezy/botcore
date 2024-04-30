from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler


async def _test_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_html(
        'Ok i\'am here!'
    )
    await update.message.set_reaction(reaction="🗿")


def _add_command_handler(app: Application, command_handler, trigger_text: str):
    app.add_handler(CommandHandler(trigger_text, command_handler))


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
            _add_command_handler(self._application, self._handlers.get(handler), handler)

        return self

    def run(self):
        self._application.run_polling()


