import telebot
import yt_dlp

# توكن البوت
TOKEN = "7988163744:AAGcmXG7V-2InbYmyP6ppF-5Org92Omi3bg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً! ابعتلي رابط فيديو من يوتيوب أو تيك توك أو فيسبوك، وهحمّله ليك.")

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text.strip()

    ydl_opts = {
        'format': 'best[ext=mp4][vcodec^=avc1][acodec^=mp4a]/best',
        'merge_output_format': 'mp4',
        'postprocessors': [],
        'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as video:
            bot.send_video(message.chat.id, video)

    except Exception as e:
        bot.reply_to(message, f"❌ حصل خطأ:\n{e}")

bot.infinity_polling()