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
    _application: Application = None

    def __init__(self, token: str):
        self._token = token

    def run(self):
        app = Application.builder().token(self._token).build()
        _add_handler(app, _test_handler, 'test')

        app.run_polling()

    def run_with_custom_handlers(self, handlers):
        pass

