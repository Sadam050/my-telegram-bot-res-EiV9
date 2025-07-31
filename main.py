from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import urllib.parse

# Store user data in memory
user_data = {}
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your token

# /start command with optional referral ID
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    referred_by = None

    if user_id not in user_data:
        user_data[user_id] = {"coins": 0, "last_claimed": None, "referrals": [], "referred_by": None}

        # Referral processing
        if args:
            referred_by = int(args[0])
            if referred_by != user_id and referred_by in user_data:
                if user_id not in user_data[referred_by]["referrals"]:
                    user_data[referred_by]["coins"] += 2  # Reward for referral
                    user_data[referred_by]["referrals"].append(user_id)
                    user_data[user_id]["referred_by"] = referred_by

    await update.message.reply_text(
        "👋 Welcome! Use /GET to get today's coins, /wallet to check coins, and /referral to invite friends!"
    )

# /daily command
async def GET(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    today = datetime.date.today()

    if user_id not in user_data:
        user_data[user_id] = {"coins": 0, "last_claimed": None, "referrals": [], "referred_by": None}

    if user_data[user_id]["last_claimed"] == today:
        await update.message.reply_text("❗ You already claimed today's coin.")
    else:
        user_data[user_id]["coins"] += 1
        user_data[user_id]["last_claimed"] = today
        await update.message.reply_text("✅ You received 1 coin today!")

# /balance command
async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    coins = user_data.get(user_id, {}).get("coins", 0)
    await update.message.reply_text(f"💰 You have {coins} coin(s).")

# /referral command
async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    bot_username = (await context.bot.get_me()).username
    ref_link = f"https://t.me/{bot_username}?start={user_id}"
    referrals = user_data.get(user_id, {}).get("referrals", [])
    await update.message.reply_text(
        f"🔗 Your referral link:\n{ref_link}\n👥 Total referrals: {len(referrals)}"
    )

# Setup
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("get", GET))
app.add_handler(CommandHandler("wallet", wallet))
app.add_handler(CommandHandler("referral", referral))
app.run_polling()