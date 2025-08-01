# Updated secure version
import os
from telegram.ext import Application
from dotenv import load_dotenv

load_dotenv()

async def start(update, context):
    await update.message.reply_text("🤖 Bot is online!")

if __name__ == "__main__":
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
