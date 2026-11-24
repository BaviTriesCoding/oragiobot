import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

OPZIONI_MACCHINE = [
    "ho bisogno di un passaggio",
    "sono autonomo",
    "ho la macchina (1 posto)",
    "ho la macchina (2 posti)",
    "ho la macchina (3 posti)",
    "ho la macchina (4 posti)",
]


async def allenamento(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_poll(
        update.message.chat_id,
        question="allenamento stasera?",
        is_anonymous=False,
        options=["👍", "👎"],
    )


async def macchine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_poll(
        update.message.chat_id,
        question="macchine andata",
        is_anonymous=False,
        options=OPZIONI_MACCHINE,
    )
    await context.bot.send_poll(
        update.message.chat_id,
        question="macchine ritorno",
        is_anonymous=False,
        options=OPZIONI_MACCHINE,
    )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("allenamento", allenamento))
    app.add_handler(CommandHandler("macchine", macchine))
    app.run_polling()


if __name__ == "__main__":
    main()