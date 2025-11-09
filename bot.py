from telegram.ext import(
    Updater, 
    CommandHandler, 
    MessageHandler, 
    Filters, 
    CallbackQueryHandler
)
import re

from config import Config
from callbacks import (
    start, 
    handle_language_callback, 
    send_orders, 
    send_cooperation, 
    send_about,
    send_comment,
    send_5,
    send_4,
    send_3,
    send_2,
    send_delivery_terms,
    send_contact,
    main_menu,
    handle_language_text
)

def main():
    updater = Updater(Config.TOKEN)
    dispatcher = updater.dispatcher

    # /start komandasi
    dispatcher.add_handler(
        CommandHandler(command='start', callback=start)
    )

    # Inline tugma callbacklari (til tanlash)
    dispatcher.add_handler(
        CallbackQueryHandler(callback=handle_language_callback, pattern="^change_lang:")
    )

    # KeyboardButton tugmalar uchun MessageHandler lar
    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("📥 Savat")), callback=send_orders)
    )
    
    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("💼 Hamkorlik")), callback=send_cooperation)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("ℹ️ Ma'lumot")), callback=send_about)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("✍️ Izoh qoldirish")), callback=send_comment)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️")), callback=send_5)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️")), callback=send_4)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("😐Qo'niqarli, 3⭐️⭐️⭐️")), callback=send_3)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("☹️Yoqmadi, 2 ⭐️⭐️")), callback=send_2)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("😤Men shikoyat qilmoqchiman 👎🏻")), callback=send_2)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("⬅️ Ortga")), callback=send_comment)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("🌐 Tilni tanlash")), callback=handle_language_text)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("🚀 Yetkazib berish shartlari")), callback=send_delivery_terms)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("☎️ Kontaktlar")), callback=send_contact)
    )

    dispatcher.add_handler(
        MessageHandler(Filters.regex(re.escape("🏠 Bosh menyu")), callback=main_menu)
    )

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()


main()
