import telebot
import requests
from bs4 import BeautifulSoup as BS

TOKEN = '5319948944:AAFgiCewapgWL89O_in2eE_Gguk1d1SEjCk'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
@bot.message_handler(commands=['Hi'])
def start_message(message):
  bot.send_message(message.chat.id,"Hello dude ✌️ ")
@bot.message_handler(commands=['stopgame'])
def start_message(message):
  for p in range (1,18):
        r = requests.get("https://stopgame.ru/review/new/izumitelno/p"+str(p))
        html = BS(r.content, 'html.parser')
        items = html.select(".items > .article-summary")
        for el in items:
            title = el.select('.caption > a')
            res = title[0].text
            bot.send_message(message.chat.id, res)



bot.infinity_polling()
