# Updated secure version
import os
from telegram.ext import Application
from dotenv import load_dotenv

load_dotenv()

async def start(update, context):
    await update.message.reply_text("🤖 Bot is online!")

if __name__ == "__main__":
    app = Application.builder().token(os.getenv("8211462719:AAG-E5gWUo_gGa6lorCn1byph5oR8Q3IVS8")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
