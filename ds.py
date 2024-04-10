import telegram
from king import home
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Enter the username.')

# Define a function to handle user messages
def echo(update: Update, context: CallbackContext):
    d=home(update.message.text)
    update.message.reply_text(d)
    
def display(update: Update, context: CallbackContext):
    with open('name.json','r') as f:
        d=f.readlines()

    update.message.reply_text(d)
    
    

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("6441353473:AAGGupzFm0Aveq-XTwmVCHIa_XvdWzJO")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("display", display))
    # Register a message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
