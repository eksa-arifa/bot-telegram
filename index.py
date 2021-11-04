import telebot

api = '2092436932:AAEC8eYlym5w4sHsy8cjfPqBFPafOq5W-6A'

bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hai,aku bot eksa,kamu bisa menuliskan beberapa command dibawah ini\n/creator : untuk mengetahui siapa yang membuatku\n/github : untuk meminta link github")

@bot.message_handler(commands=['creator'])
def creator(message):
	bot.reply_to(message, "Eksa arifa")

@bot.message_handler(commands=['github'])
def github(message):
	bot.reply_to(message, "https://github.com/eksaarifa")

print("[+]bot berjalan...")
bot.polling()
