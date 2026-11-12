import os
from datetime import date
import telebot

TOKEN = os.getenv("9254739622:AAE0QQFuVTqC51KaGKCxWIFAJKJCxrnWf6A")
CHANNEL_ID = -1004451460840  # 
ADMIN_IDS = [7700854177, 1497040250]

# === CUSTOM BALESAN BOT - EDIT DI SINI AJA KALO MAU GANTI ===
REPLY_START = "haii rakyat cksp🤓\nkirim menfess sini yaa muah😘"
REPLY_SUKSES = "udah ke-post!"
REPLY_LIMIT = "limit lu hari ini udah abis (5/5) \nbesok lagi woi"
REPLY_ADMIN_INFO = "📩 MENFESS BARU dari @{username} ({nama}) ID: {id}"

bot = telebot.TeleBot(TOKEN)
limit_data = {}

def cek_limit(user_id):
    today = str(date.today())
    if user_id not in limit_data or limit_data[user_id][0] != today:
        limit_data[user_id] = [today, 0]
    if limit_data[user_id][1] >= 5:
        return False
    limit_data[user_id][1] += 1
    return True

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, REPLY_START)

@bot.message_handler(content_types=['text','photo','video','audio','voice','sticker','document','animation','video_note'])
def menfess(message):
    user_id = message.from_user.id
    if not cek_limit(user_id):
        bot.reply_to(message, REPLY_LIMIT)
        return

    username = message.from_user.username or "no_username"
    nama = message.from_user.first_name or "anon"
    info_admin = REPLY_ADMIN_INFO.format(username=username, nama=nama, id=user_id)

    try:
        if message.content_type == 'text':
            bot.send_message(CHANNEL_ID, f"📩 MENFESS:\n\n{message.text}")
        elif message.content_type == 'photo':
            bot.send_photo(CHANNEL_ID, message.photo[-1].file_id, caption=message.caption or "📩 MENFESS")
        elif message.content_type == 'video':
            bot.send_video(CHANNEL_ID, message.video.file_id, caption=message.caption or "📩 MENFESS")
        elif message.content_type == 'voice':
            bot.send_voice(CHANNEL_ID, message.voice.file_id, caption="📩 MENFESS VN")
        elif message.content_type == 'audio':
            bot.send_audio(CHANNEL_ID, message.audio.file_id, caption=message.caption or "📩 MENFESS")
        elif message.content_type == 'sticker':
            bot.send_sticker(CHANNEL_ID, message.sticker.file_id)
        elif message.content_type == 'document':
            bot.send_document(CHANNEL_ID, message.document.file_id, caption=message.caption or "📩 MENFESS")
        elif message.content_type == 'animation':
            bot.send_animation(CHANNEL_ID, message.animation.file_id, caption=message.caption or "📩 MEN
