import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
#GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:
        #while True:
                #button_state = GPIO.input(23)
                #if button_state == False:
                        #GPIO.output(24, True)
                        print("Activando Camara...")
                        print("Capturando Imagen")
                        os.system("raspistill -o foto.jpg")
                        os.system('telegram-send --image foto.jpg --caption "Tenemos Visita"')
                        os.system("telegram-send 'Dame un momento ya te envio el video'")
                        os.system("raspivid -o video.h264 -t 10000")
                        os.system("MP4Box -add video.h264 video.mp4")
                        os.system("telegram-send --file video.mp4")
                        #print("Enviando correo ...")
                        #os.system("python3 mailf.py")
                        #time.sleep(0.2)
                #else:
                        #GPIO.output(24, False)
except:
        GPIO.cleanup()

