import logging
import os

from telegram.ext import Filters, MessageHandler, Updater

# Retrieve values from environment variables
TOKEN = os.environ.get('BOT_TOKEN')
ADDITIONAL_TEXT = os.environ.get('ADDITIONAL_TEXT')

if TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable is not set")
if ADDITIONAL_TEXT is None:
    raise ValueError("ADDITIONAL_TEXT environment variable is not set")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def add_text_to_message(update, context):
    message = update.effective_message

    if message.photo:
        caption = message.caption if message.caption else ''
        caption += ADDITIONAL_TEXT
        context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)
    elif message.video:
        caption = message.caption if message.caption else ''
        caption += ADDITIONAL_TEXT
        context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)
    elif message.audio:
        caption = message.caption if message.caption else ''
        caption += ADDITIONAL_TEXT
        context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)
    elif message.animation:
        caption = message.caption if message.caption else ''
        caption += ADDITIONAL_TEXT
        context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)
    else:
        # No media type specified, add text to text message
        edited_text = message.text + ADDITIONAL_TEXT
        context.bot.edit_message_text(chat_id=message.chat_id, message_id=message.message_id, text=edited_text)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, add_text_to_message))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
