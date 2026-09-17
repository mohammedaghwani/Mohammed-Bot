import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توكن البوت الخاص بك
TOKEN = "8731514826:AAGK7qOosQJ_O3IzcxFAhuJpYaKDVzqkNXw"

# رسالة الترحيب عند الضغط على /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! أنا بوت سوبر جوكر، تم تفعيلي برمجياً بنجاح وسأقوم بالرد على رسائل الجميع تلقائياً.")

# الرد التلقائي على كافة الرسائل والناس دون شروط
async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # هنا يمكنك كتابة ردود مخصصة، حالياً سيرد البوت بتأكيد استلام الرسالة
    response_text = f"تم استلام رسالتك: '{user_message}'\nانتظرني، سأجيبك قريباً!"
    await update.message.reply_text(response_text)

def main():
    # بناء تطبيق البوت برمجياً
    application = Application.builder().token(TOKEN).build()

    # تفعيل الموجهات للترحيب والرد العام
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))

    # بدء التشغيل وسحب الرسائل
    print("البوت يعمل الآن ومستعد لاستقبال الرسائل...")
    application.run_polling()

if __name__ == '__main__':
    main()

