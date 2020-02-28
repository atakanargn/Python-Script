from telegram.ext import Updater, CommandHandler

# BotFather tarafından verilen API_KEY ile bota bağlandık
updater = Updater('828454971:AAF6cJxfs98m1b1E8T_UquOniEVkDmdVgDw')

# Komutlar

# /merhaba
def merhaba(bot, update):
    update.message.reply_text(
        'Merhaba {}'.format(update.message.from_user.first_name)+', ben TelegramBot scripti Atakan Argın tarafından yazıldım !'+
        '\n"/yardim" yazarak yardım alabilirsin.')
    update.message.voice

# /yardim
def yardim(bot, update):
    # BEN YANIT OLARAK GÖNDERİLECEK
    # VERİYİ DOSYADAN ÇEKTİM
    # SİZ DAAH FARKLI YÖNTEMLER KULLANABİLİRSİNİZ.
    dosya=open("yardim.txt","r")

    # YANIT
    update.message.reply_text(dosya.read())

"""
def yeniKomut(bot, update):

    # YAPILMASINI ISTEDIĞINIZ KOMUTLAR
    # BURAYA YAZILACAK

    update.message.reply_text("YANIT OLARAK GÖNDERİLECEK VERİ BURAYA YAZILACAK!")
"""

# KOMUTLAR
updater.dispatcher.add_handler(CommandHandler('merhaba', merhaba))
updater.dispatcher.add_handler(CommandHandler('yardim', yardim))
# updater.dispatcher.add_handler(CommandHandler('yeniKomut', yeniKomut))

# BOTU BAŞLATTIK
updater.start_polling()
updater.idle()