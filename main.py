import telebot

TOKEN = "8211462719:AAG-E5gWUo_gGa6lorCn1byph5oR8Q3IVS8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "✅ Bot running on Koyeb with long polling!")

print("Bot is running...")
bot.infinity_polling()
