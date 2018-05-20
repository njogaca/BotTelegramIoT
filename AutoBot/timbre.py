import RPi.GPIO as GPIO
import time,os
import subprocess
import threading
def Backup():
   os.system("sudo python /home/pi/Desktop/BotTelegramIoT/AutoBot/backup.py")
def StartMjpgService():
   #os.system('/home/pi/Desktop/BotTelegramIoT/Streaming/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -i "./input_raspicam.so -fps 60 -quality 10 -x 400 -y 300" -o "./output_http.so -c SmartDoor:IoT2018"')
   os.system('/home/pi/Desktop/BotTelegramIoT/Streaming/mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer -i "/home/pi/Desktop/BotTelegramIoT/Streaming/mjpg-streamer/mjpg-streamer-experimental/input_raspicam.so -fps 60 -quality 10 -x 400 -y 300" -o "/home/pi/Desktop/BotTelegramIoT/Streaming/mjpg-streamer/mjpg-streamer-experimental/output_http.so"')
def StopMjpgService():
   os.system("killall mjpg_streamer")

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP) #BOTON
pf = '/usr/local/bin/pf'
ipaddr = '/usr/local/bin/ipaddr'
EXTERNAL_PORT = 54321
INTERNAL_PORT = 8080
try:
   while True:
      boton = GPIO.input(23)
      if boton == False:
         threading.Thread(target=Backup).start()
         print("Timbre Activado")
         time.sleep(5)
         os.system("telegram-send 'Hey ... estan timbrando ...'")
         time.sleep(5)
         #subprocess.call(['sudo','systemctl','start','mjpg_streamer.service'])
         threading.Thread(target=StartMjpgService).start()
         subprocess.call([pf,str(EXTERNAL_PORT),str(INTERNAL_PORT)])
         out = subprocess.check_output([ipaddr])
         ip = dict([line.split('=') for line in out.decode('ascii').strip().split('\n')])
         #reply = 'http://%s:%d/?action=stream' % (ip['External'],EXTERNAL_PORT)
         reply = 'http://%s:%d/?action=stream' % (ip['Internal'],INTERNAL_PORT)
         #reply = 'http://192.168.43.29:8080/?action=stream'
         os.system('telegram-send '+ reply)
         #reply = 'http://%s:%d/?action=stream' % (ip['External'],EXTERNAL_PORT)
         #if ip['External'] != ip['Public']:
         #   reply += '\n No es posible realizar streaming de manera Externa'

         #os.system('telegram-send '+ reply)
         time.sleep(40) #100
         os.system("telegram-send 'Comenzando a finalizar Streaming'")
         #subprocess.call([pf,'delete',str(EXTERNAL_PORT)])
         StopMjpgService()
         #subprocess.call(['sudo','systemctl','stop','mjpg_streamer.service'])
         os.system("telegram-send 'Streaming Finalizado'")
         pass
except:
   GPIO.cleanup()
