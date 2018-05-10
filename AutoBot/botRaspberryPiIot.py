#Autor: Johan Garcia - Guillermo Romero -IoT 2018
#Librerias
import telegram
from telegram.ext import *
import os
import sys
import time
import subprocess
import telepot
from telepot.loop import MessageLoop

pf= '/usr/local/bin/pf'
ipaddr = '/usr/local/bin/ipaddr'
EXTERNAL_PORT = 54321
INTERNAL_PORT = 8080 #Puerto default del servicio mjpg_streamer

#Indicar el Id del Bot sobre el cual vamos a trabajar
mi_bot = telegram.Bot(token='502350411:AAF6jhgJ1PoQO40MRaTI5Q1RfwV9QfCcSf4')
#Actualizar con regularidad el ID del bot
mi_bot_updater = Updater(mi_bot.token)
#Definicion de funcion Start
def start(bot, update, pass_chat_data=True):
   update.message.chat_id
   bot.sendMessage(chat_id=update.message.chat_id,text='Hola, Soy Brainiac')
   bot.sendMessage(chat_id=update.message.chat_id,text='Soy quien se encarga de estar atento por si alguien llama a tu puerta')
#Definicion de funcion Close
def close(bot, update, pass_chat_data=True):
   update.message.chat_id
   bot.sendMessage(chat_id=update.message.chat_id,text='Lo siento pero vigilo 24/7, yo no descanso Jefe.')
   #os.system('telegram-send --image noDormir.jpg --caption "Lo siento pero yo no descanso Jefe"')
#Definicion de funcion ObtenerFoto
def obtenerFoto(bot, update,pass_chat_data=True):
   update.message.chat_id
   bot.sendMessage(chat_id=update.message.chat_id,text='Con gusto jefe dame un momento y te envio la foto...')
   os.system('rm foto.jpg')
   os.system('raspistill -o foto.jpg')
   #os.system('telegram-send --image foto.jpg --caption "Aqui tienes Jefe"')
   bot.send_photo(chat_id=update.message.chat_id,photo=open('foto.jpg','rb'))
#Definicion de funcion ObtenerVideo
def obtenerVideo(bot, update, pass_chat_data=True):
   update.message.chat_id
   bot.sendMessage(chat_id=update.message.chat_id,text='Con gusto jefe dame un momento y te envio el video...')
   os.system('rm video.h264')
   os.system('rm video.mp4')
   os.system("raspivid -o video.h264 -t 5000")
   os.system("MP4Box -add video.h264 video.mp4")
   os.system('telegram-send --file video.mp4 --timeout 40.0')
   bot.sendMessage(chat_id=update.message.chat_id,text='Lamento la demora, espero puedas disculparme')
#Definicion de funcion para inicio de streaming
def iniciarStreaming(bot,update,pass_chat_data=True):
   global pf,ipaddr
   
   subprocess.call(['sudo', 'systemctl', 'start' , 'mjpg_streamer.service'])
   update.message.chat_id
   subprocess.call([pf,str(EXTERNAL_PORT),str(INTERNAL_PORT)])
   out = subprocess.check_output([ipaddr])
   ip = dict([line.split('=') for line in out.decode('ascii').strip().split('\n')])
   reply = 'http://%s:%d/?action=stream' % (ip['External'], EXTERNAL_PORT)
   if ip['External'] != ip['Public']:
      reply += '\nNo es posible realizar streaming'

   bot.sendMessage(chat_id=update.message.chat_id, text=reply)
#Definicion de funcion para finalizar streaming
def finalizarStreaming(bot,update,pass_chat_data=True):
   global pf,ipaddr
   update.message.chat_id
   subprocess.call([pf, 'delete', str(EXTERNAL_PORT)])
   subprocess.call(['sudo', 'systemctl', 'stop', 'mjpg_streamer.service'])
   bot.sendMessage(chat_id=update.message.chat_id,text='Streaming Finalizado')
#Listener de conversacion
def listener(bot,update,pass_chat_data=True):
   update.message.chat_id
   mensaje = update.message.text
   mensajeLower = mensaje.lower()
   if(mensajeLower == 'hola'):
      bot.sendMessage(chat_id=update.message.chat_id,text='Si deseas usar alguna de mis funciones puedes usar las siguientes: ')
      bot.sendMessage(chat_id=update.message.chat_id,text='/obtenerFoto ,  esta funcion hara que tome una foto y te la envie.')
      bot.sendMessage(chat_id=update.message.chat_id,text='/obtenerVideo, esta funcion me permite enviarte un video del momento, suelo demorarme un poco con esta tarea espero me disculpes')
      bot.sendMessage(chat_id=update.message.chat_id,text='/iniciarStreaming, iniciar streaming')
      bot.sendMessage(chat_id=update.message.chat_id,text='/finalizarStreaming, terminar streaming')
   elif(mensajeLower.find('preocupes')):
      bot.sendMessage(chat_id=update.message.chat_id,text='Eres el mejor')
   else:
      bot.sendMessage(chat_id=update.message.chat_id,text='lo siento pero no tengo nada que responder ante eso :´( ')
#------------------------------------------------Fin de Definiciones -----------------------------------------------
close_handler = CommandHandler('close',close)
start_handler = CommandHandler('start',start)
obtenerFoto_handler = CommandHandler('obtenerFoto',obtenerFoto)
obtenerVideo_handler = CommandHandler('obtenerVideo',obtenerVideo)
listener_handler = MessageHandler(Filters.text,listener)
iniStreaming_handler = CommandHandler('iniciarStreaming',iniciarStreaming)
finStreaming_handler = CommandHandler('finalizarStreaming',finalizarStreaming)

dispatcher = mi_bot_updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(close_handler)
dispatcher.add_handler(obtenerFoto_handler)
dispatcher.add_handler(obtenerVideo_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(iniStreaming_handler)
dispatcher.add_handler(finStreaming_handler)
mi_bot_updater.start_polling()
mi_bot_updater.idle()
MessageLoop(mi_bot.token, iniciarStreaming).run_as_thread()

while True:
   pass
