# Task_3:Telegram Bot Creation using Python:
from telegram import Update
from telegram.ext import Application, CommandHandler

Token = "7648355202:AAFnv1K-TMtZW2DRctMcww8T7NUUsMjLmQI"

# Create an application instance instead of updater
application = Application.builder().token(Token).build()

# Define the start function
async def start(update: Update, context):
    await update.message.reply_text("Welcome to rk_learn")

# Define the help function
async def help(update: Update, context):
    await update.message.reply_text(
        """
        /start -> Welcome to the channel
        /help -> This particular message
        /content -> About various playlists of rk_learn
        /python -> The first video from python playlist
        /SQL -> The first video from SQL playlist
        /Java -> The first video from Java playlist
        /contact -> Contact information
        """
    )
# Define the content function
async def content(update: Update, context):
    await update.message.reply_text("We have various playlists and articles available")

# Define the python function
async def python(update: Update, context):
    await update.message.reply_text("Tutorial link: https://youtu.be/Tm5u97I7OrM")

# Add command handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help))
application.add_handler(CommandHandler("content", content))
application.add_handler(CommandHandler("python", python))

# Start the bot
if __name__ == "__main__":
    application.run_polling()