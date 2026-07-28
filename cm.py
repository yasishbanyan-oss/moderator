import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# توکن بات که از BotFather گرفتی
TOKEN = os.environ.get("BOT_TOKEN", "8989176817:AAHBHAOorua7GAZcTm4fmCQsD7tAEVxLiJk")

# آیدی عددی گروه کامنت‌ها (باید با منفی شروع شود)
DISCUSSION_GROUP_ID = int(os.environ.get("DISCUSSION_GROUP_ID", "-1002243223128"))

COMMENT_TEXT = (
    "سلام رفقا! لطفا ری اکشن و کامنت بزارید و پستو برای دوستاتون فوروارد کنید! 👊\n\n"
    "ما برای اینکه شما بهترین محتوا رو داشته باشید روزی ۳ الی ۶ ساعت روی پست هامون وقت میزاریم! با ری اکشن و کامنت و فوروارد از ما حمایت کنید! ❤️🙏"
)

async def auto_comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    
    # بررسی اینکه پیام در گروه کامنت‌ها ارسال شده و یک پیام فوروارد شده (از کانال) است
    if message and message.chat.id == DISCUSSION_GROUP_ID and message.forward_origin:
        try:
            # ارسال متن به عنوان ریپلای (کامنت) زیر پست جدید
            await message.reply_text(COMMENT_TEXT)
        except Exception as e:
            print(f"Error: {e}")

def main():
    # ساخت اپلیکیشن بات
    application = ApplicationBuilder().token(TOKEN).build()

    # فیلتر برای گرفتن پیام‌های فوروارد شده در گروه مورد نظر
    handler = MessageHandler(filters.Chat(DISCUSSION_GROUP_ID) & filters.FORWARDED, auto_comment)
    application.add_handler(handler)

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()