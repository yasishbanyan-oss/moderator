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
    # بررسی اینکه پیام در گروه کامنت‌ها آمده است (بدون شرط سخت‌گیرانه فوروارد)
    if message and message.chat.id == DISCUSSION_GROUP_ID:
        try:
            # ارسال کامنت به عنوان ریپلای زیر آخرین پست آمده در گروه
            await message.reply_text(COMMENT_TEXT)
        except Exception as e:
            print(f"Error: {e}")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    # گرفتن تمام پیام‌هایی که در گروه کامنت‌ها ارسال می‌شود (شامل پست‌های کانال)
    handler = MessageHandler(filters.Chat(DISCUSSION_GROUP_ID) & ~filters.COMMAND, auto_comment)
    application.add_handler(handler)

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{RENDER_EXTERNAL_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
