from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8403556318:AAFyA2k1YYoLBfYFvLORCjR_jO_pAmFsc8o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🪪 Aadhaar", callback_data="aadhaar")],
        [InlineKeyboardButton("🆔 PAN Card", callback_data="pan")],
        [InlineKeyboardButton("📜 Caste", callback_data="caste")],
        [InlineKeyboardButton("💰 Income", callback_data="income")],
        [InlineKeyboardButton("🏠 Residence", callback_data="residence")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "कृपया एक सेवा चुनें:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "aadhaar":
        await query.edit_message_text("🪪 Aadhaar सेवा चुनी गई।")
    elif query.data == "pan":
        await query.edit_message_text("🆔 PAN Card सेवा चुनी गई।")
    elif query.data == "caste":
        await query.edit_message_text("📜 Caste Certificate सेवा चुनी गई।")
    elif query.data == "income":
        await query.edit_message_text("💰 Income Certificate सेवा चुनी गई।")
    elif query.data == "residence":
        await query.edit_message_text("🏠 Residence Certificate सेवा चुनी गई।")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()