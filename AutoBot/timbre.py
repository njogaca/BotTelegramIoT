import RPi.GPIO as GPIO
import time,os
import subprocess
import threading
def Backup():
   os.system("sudo python backup.py")


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
         subprocess.call(['sudo','systemctl','start','mjpg_streamer.service'])
         #subprocess.call([pf,str(EXTERNAL_PORT),str(INTERNAL_PORT)])
         #out = subprocess.check_output([ipaddr])
         #ip = dict([line.split('=') for line in out.decode('ascii').strip().split('\n')])
         #reply = 'http://%s:%d/?action=stream' % (ip['External'],EXTERNAL_PORT)
         #reply = 'http://%s:%d/?action=stream' % (ip['Internal'],INTERNAL_PORT)
         reply = 'http://172.71.10.23:8080/?action=stream'
         os.system('telegram-send '+ reply)
         #reply = 'http://%s:%d/?action=stream' % (ip['External'],EXTERNAL_PORT)
         #if ip['External'] != ip['Public']:
         #   reply += '\n No es posible realizar streaming de manera Externa'

         #os.system('telegram-send '+ reply)
         time.sleep(30) #100
         os.system("telegram-send 'Comenzando a finalizar Streaming'")
         #subprocess.call([pf,'delete',str(EXTERNAL_PORT)])
         subprocess.call(['sudo','systemctl','stop','mjpg_streamer.service'])
         os.system("telegram-send 'Streaming Finalizado'")
         pass
except:
   GPIO.cleanup()
