from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import random

Status		= ['Jomblo','Menikah','Pacaran']
Greeting	= ['Selamat Pagi','Selamat Siang','Selamat Sore','Selamat Malam']
Gender		= ['Laki-laki','Perempuan']
Job			= ['Sekolah','Guru anak tk','Pengacara','Tidak Ada']
Hobby		= ['Turu','Main game','Ngoprek','Belajar']
Quotes		= ['Jangan semangat!','Teruslah gagal!','Teruslah hidup!','Semangat!']

updater = Updater("#Gunakan API Bot Telegram",
                  use_context=True)

def mulai(update: Update, context: CallbackContext):
    update.message.reply_text("selamat datang di Random Status!! \nsilahkan dilihat /bantuan untuk menjalankan bot ini")

def bantuan(update: Update, context: CallbackContext):
	update.message.reply_text("klik /jalankan dan bot secara otomatis akan berjalan")

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Maaf, perintah '%s' tidak valid!!" % update.message.text)

def bot(update: Update, context: CallbackContext):
	update.message.reply_text(random.choice(Greeting) )

	update.message.reply_text(' statusku saat ini ' +	random.choice(Status) )

	update.message.reply_text(' jenis kelaminku adalah ' +	random.choice(Gender) )

	update.message.reply_text(' dan aku punya hobby ' +	random.choice(Hobby) )
	
	update.message.reply_text(' untuk saat ini, pekerjaanku ' +	random.choice(Job) )

	update.message.reply_text(' Apapun yang sudah kamu lakukan hari ini, ' + random.choice(Quotes))

	update.message.reply_text(' /reset ')

updater.dispatcher.add_handler(CommandHandler('mulai', mulai))
updater.dispatcher.add_handler(CommandHandler('bantuan', bantuan))
updater.dispatcher.add_handler(CommandHandler('reset', mulai))
updater.dispatcher.add_handler(CommandHandler('jalankan', bot))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
