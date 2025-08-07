from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext

def handle_contact(update: Update, context: CallbackContext):
    contact = update.message.contact
    context.user_data["phone"] = contact.phone_number

    update.message.reply_text("✅ Sizning telefon raqamingiz muvaffaqiyatli saqalandi.")

    keyboard = [
        [KeyboardButton("🛍 Buyurtma berish", web_app=WebAppInfo(url="https://uzum.uz"))],
        ["📦 Buyurtmalarim", "⚙️ Sozlamalar"],
        ["ℹ️ Biz haqimizda", "✍️ Fikr qoldirish"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Kerakli bo‘limni tanlang:", reply_markup=reply_markup)


def handle_photo(update: Update, context: CallbackContext):
    photo = update.message.photo[0]
    update.message.reply_photo(photo=photo, caption="Siz yuborgan rasm")


def start(update: Update, context: CallbackContext):
    if update.message:
        keyboard = [
            [KeyboardButton("🛍 Buyurtma berish", web_app=WebAppInfo(url="https://uzum.uz"))],
            ["📦 Buyurtmalarim", "⚙️ Sozlamalar"],
            ["ℹ️ Biz haqimizda", "✍️ Fikr qoldirish"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        update.message.reply_text("Kerakli bo‘limni tanlang:", reply_markup=reply_markup)


def handle_text(update: Update, context: CallbackContext):
    text = update.message.text
    user_data = context.user_data

    if text == "Buyurtma berish":
        if "phone" in user_data:
            update.message.reply_text("Buyurtma berish uchun sayt: https://uzum.uz")
        else:
            contact_button = KeyboardButton("Raqamni yuborish", request_contact=True)
            reply_markup = ReplyKeyboardMarkup([[contact_button]], resize_keyboard=True, one_time_keyboard=True)
            update.message.reply_text("Buyurtma berish uchun telefon raqamingizni yuboring:", reply_markup=reply_markup)

    elif text == "Buyurtmalarim":
        update.message.reply_text("Sizda hali buyurtmalar yo‘q.")

    elif text == "Sozlamalar":
        update.message.reply_text("Bu yerda sozlamalarni o‘zgartirasiz.")

    elif text == "Biz haqimizda":
        update.message.reply_text("Elektron pochta: nilufarhamroyeva2006@gmail.com")

    elif text == "Fikr qoldirish":
        update.message.reply_text("Fikringizni yozib qoldiring, iltimos.")
