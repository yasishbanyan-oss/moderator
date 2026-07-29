import os
import asyncio
from aiohttp import web
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN", "8989176817:AAHBHAOorua7GAZcTm4fmCQsD7tAEVxLiJk")
DISCUSSION_GROUP_ID = int(os.environ.get("DISCUSSION_GROUP_ID", "-1002243223128"))

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

# وب سرور برای پاسخ به رندر و باز نگه داشتن پورت
async def handle(request):
    return web.Response(text="Bot is running!")

async main():
    # 1. راه‌اندازی وب سرور aiohttp روی پورت رندر
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server started on port {port}")

    # 2. راه‌اندازی بات تلگرام
    application = ApplicationBuilder().token(TOKEN).build()
    handler = MessageHandler(filters.Chat(DISCUSSION_GROUP_ID) & filters.FORWARDED, auto_comment)
    application.add_handler(handler)

    # استارت زدن بات بدون مسدود کردن رویدادها
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    print("Telegram bot is running smoothly...")

    # نگه‌داشتن برنامه روشن
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
