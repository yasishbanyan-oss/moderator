import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8989176817:AAHBHAOorua7GAZcTm4fmCQsD7tAEVxLiJk"
DISCUSSION_GROUP_ID = -1002243223128

PORT = int(os.environ.get("PORT", "10000"))
RENDER_EXTERNAL_URL = "https://moderator-1-6esw.onrender.com"

COMMENT_TEXT = (
    "سلام رفقا! لطفا ری اکشن و کامنت بزارید و پستو برای دوستاتون فوروارد کنید! 👊\n\n"
    "ما برای اینکه شما بهترین محتوا رو داشته باشید روزی ۳ الی ۶ ساعت روی پست هامون وقت میزاریم! با ری اکشن و کامنت و فوروارد از ما حمایت کنید! ❤️🙏"
)

async def auto_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and message.chat.id == DISCUSSION_GROUP_ID and message.forward_origin:
        try:
            await message.reply_text(COMMENT_TEXT)
        except Exception as e:
            print(f"Error: {e}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    handler = MessageHandler(filters.Chat(DISCUSSION_GROUP_ID) & filters.FORWARDED, auto_comment)
    application.add_handler(handler)

    # راه‌اندازی وب‌هوک اختصاصی با لینک رندر شما
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{RENDER_EXTERNAL_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
