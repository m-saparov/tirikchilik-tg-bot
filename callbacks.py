from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from telegram.ext import CallbackContext
from uzbek import Uzbek

import re

uzbek = Uzbek()


def start(update: Update, context: CallbackContext) -> None:
    text = (
        "Iltimos, tilni tanlang\n"
        "Пожалуйста, выберите язык\n"
        "Please, choose a language ⬇️"
    )

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[[ 
            InlineKeyboardButton("Uzbek 🇺🇿", callback_data='change_lang:uz'),
            InlineKeyboardButton("English 🇺🇸", callback_data='change_lang:en'),
            InlineKeyboardButton("Russian 🇷🇺", callback_data='change_lang:ru')
        ]]
    )

    update.message.reply_text(text=text, reply_markup=reply_markup)


def handle_language_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if not query:
        return
    query.answer()
    if not query.data.startswith("change_lang:"):
        return

    lang = query.data.split(":")[1]
    name = update.effective_user.first_name

    if lang == "uz":
        text = uzbek.uz_start(name)
        query.edit_message_text(text=text)
        main_menu(update, context)
    elif lang == "en":
        query.edit_message_text(text=f"Hello, {name}! You selected English 🇺🇸")
    elif lang == "ru":
        query.edit_message_text(text=f"Здравствуйте, {name}! Вы выбрали русский язык 🇷🇺")


def handle_language_text(update: Update, context: CallbackContext):
    """KeyboardButton orqali Tilni tanlash bosilganda start funksiyasini chaqiradi"""
    if update.message and update.message.text == "🌐 Tilni tanlash":
        start(update, context)


def main_menu(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🔥 Mahsulotlar", web_app=WebAppInfo(url="https://tirikchilik.uz")),
                KeyboardButton(text="📥 Savat")
            ],
            [
                KeyboardButton(text="💼 Hamkorlik"),
                KeyboardButton(text="ℹ️ Ma'lumot")
            ],
            [
                KeyboardButton(text="🌐 Tilni tanlash")
            ]
        ],
        resize_keyboard=True
    )

    if update.message:
        update.message.reply_text("Asosiy menyu:", reply_markup=reply_markup)
    elif update.callback_query:
        update.callback_query.message.reply_text("Asosiy menyu:", reply_markup=reply_markup)


def send_orders(update: Update, context: CallbackContext):
    update.message.reply_text("Sizning savatingiz bo'sh")


def send_cooperation(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz "
        "va sizning buyurtmangizga asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.\n\n"
        "Menejer bilan bog'lanish uchun: @Mr_Mehroj"
    )


def send_about(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✍️ Izoh qoldirish")],
            [KeyboardButton(text="🚀 Yetkazib berish shartlari"), KeyboardButton(text="☎️ Kontaktlar")],
            [KeyboardButton(text="🏠 Bosh menyu")]
        ],
        resize_keyboard=True
    )
    update.message.reply_text("Iltimos, quyidagilardan birini tanlang:", reply_markup=reply_markup)


def send_comment(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="😊Menga hamma narsa yoqdi, 5 ❤️")],
            [KeyboardButton(text="☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️")],
            [KeyboardButton(text="😐Qo'niqarli, 3⭐️⭐️⭐️")],
            [KeyboardButton(text="☹️Yoqmadi, 2 ⭐️⭐️")],
            [KeyboardButton(text="😤Men shikoyat qilmoqchiman 👎🏻")],
            [KeyboardButton(text="🏠 Bosh menyu")]
        ],
        resize_keyboard=True
    )
    update.message.reply_text("Iltimos, sharhingizni tanlang:", reply_markup=reply_markup)

def send_5(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Mamnun qolganingizdan xursandmiz 😊. Siz va yaqinlaringizni har doim xursand qilishga harakat qilamiz 🤗"
    )
    main_menu()

    
def send_4(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⬅️ Ortga")]], resize_keyboard=True
    )
    update.message.reply_text(
        "Sizga yoqqanidan xursandmiz 😊. Bot ishlashini yaxshilash uchun qanday maslahatlaringiz bor?👇🏻",
        reply_markup=reply_markup
    )


def send_3(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⬅️ Ortga")]], resize_keyboard=True
    )
    update.message.reply_text(
        "Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. "
        "Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. "
        "Yaxshilashga harakat qilamiz🙏🏻.",
        reply_markup=reply_markup
    )


def send_2(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⬅️ Ortga")]], resize_keyboard=True
    )
    update.message.reply_text(
        "Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. "
        "Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. "
        "Yaxshilashga harakat qilamiz🙏🏻.",
        reply_markup=reply_markup
    )


def send_delivery_terms(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Yetkazib berish shartlari:\n"
        "Toshkent bo‘yicha yetkazib berish: 1–3 ish kuni\n"
        "O‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuni\n"
        "Jo‘natmalar seshanba va juma kunlari amalga oshiriladi\n\n"
        "Toshkent bo'ylab yetkazib berish - 30 000 so'm\n"
        "O‘zbekiston bo'ylab yetkazib berish - 40 000 so‘m\n\n"
        "450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!"
    )
    send_about(update, context)


def send_contact(update: Update, context: CallbackContext):
    update.message.reply_text("Teskari aloqa uchun:\n@Mr_Mehroj")
    send_about(update, context)
