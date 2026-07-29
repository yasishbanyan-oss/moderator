import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from aiohttp import web

# اطلاعات کانال و بات شما
TOKEN = "8989176817:AAHBHAOorua7GAZcTm4fmCQsD7tAEVxLiJk"
DISCUSSION_GROUP_ID = -1002243223128
PORT = int(os.environ.get("PORT", "10000"))

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

async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    handler = MessageHandler(filters.Chat(DISCUSSION_GROUP_ID) & filters.FORWARDED, auto_comment)
    application.add_handler(handler)

    app = web.Application()
    app.router.add_get("/", handle)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    print("Bot is up and running!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
