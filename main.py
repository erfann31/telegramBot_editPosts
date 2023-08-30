import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHANNEL_TEXT_MAP = {}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    message = update.effective_message
    message.reply_text("Welcome to the robot! Please use the /setinfo command to set the channel ID and text.\nTo find the channel ID, just send a message from your channel to the @get_id_bot bot.\n\n\nExample:\n/setinfo -100... yourText")


def set_info(update, context):
    message = update.effective_message
    chat_id = message.chat_id
    text = message.text.split('/setinfo', 1)[1].strip()

    try:
        channel_id, additional_text = text.split(maxsplit=1)
    except ValueError:
        message.reply_text('Invalid input. Please provide the channel ID and additional text separated by a space.')
        return

    CHANNEL_TEXT_MAP[channel_id] = additional_text

    message.reply_text(f'Channel ID and additional text set successfully. Channel ID: {channel_id}, '
                       f'Additional text: {additional_text}')


def add_text_to_message(update, context):
    message = update.effective_message
    chat_id = str(message.chat_id)

    if chat_id in CHANNEL_TEXT_MAP:
        additional_text = CHANNEL_TEXT_MAP[chat_id]

        if message.photo:
            caption = message.caption if message.caption else ''
            caption += '\n\n' + additional_text
            context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)
        elif message.video:
            caption = message.caption if message.caption else ''
            caption += '\n\n' + additional_text
            context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)
        elif message.audio:
            caption = message.caption if message.caption else ''
            caption += '\n\n' + additional_text
            context.bot.edit_message_caption(chat_id=message.chat_id, message_id=message.message_id, caption=caption)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('setinfo', set_info))
    dp.add_handler(MessageHandler(Filters.all, add_text_to_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
