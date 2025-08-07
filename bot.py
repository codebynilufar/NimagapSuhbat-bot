from config import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import handle_photo, start, handle_text, handle_contact

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))
    dispatcher.add_handler(MessageHandler(Filters.contact, handle_contact))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
