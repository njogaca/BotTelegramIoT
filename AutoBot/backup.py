import sys
import time
import os

nombreArchivobase = time.strftime("%Y%m%d-%H%M%S")

def generarBackupFoto():
   nombreArchivofoto = "Foto_"+nombreArchivobase + ".png"
   comandoFoto = "raspistill -o /home/pi/Backup/"+nombreArchivofoto
   os.system(comandoFoto);

def generarBackupVideo():
   nombreArchivoVideo = "Video_"+nombreArchivobase+".mp4"
   comandoVideo = "raspivid -o /home/pi/Backup/video.h264 -t 10000"
   comandoTransformVideo = "MP4Box -add /home/pi/Backup/video.h264 /home/pi/Backup/"+nombreArchivoVideo
   os.system(comandoVideo)
   os.system(comandoTransformVideo)
   os.system("rm /home/pi/Backup/video.h264")


generarBackupVideo()
