import pyowm
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('37759c20f40cfea10113cb1ce340392c', config_dict)

import telebot

owm = pyowm.OWM('37759c20f40cfea10113cb1ce340392c')
mgr =  owm.weather_manager()

bot = telebot.TeleBot("5363068722:AAFcnZ6UK1yvBblLgQoRog3meyn8bKabjPk")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation =  mgr.weather_at_place( message.text )
    w =  observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = f"В городе {message.text} сейчас {w.detailed_status}\n"
    answer += " Температура сейчас в районе "+ str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас прохладно" 
    elif temp < 20:
        answer += "Сейчас холодно, оденься потеплее" 
    else:
        answer += "Сейчас тепло" 

    bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True)