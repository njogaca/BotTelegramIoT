# Bot creado para usar en Telegram

**Bot implemenentado en Raspberry Pi 3 con un modulo de camara, Raspbian Stretch, Python 3.5**  

#Crear Bot por medio de BotFather

BotFather es un bot en telegram que nos permitira crear nuestro propio bot

para configuar el bot que crearemos en telegram con nuestra Raspberry pi debemos instalar el paquete de python telepot

Adicionalmente por medio de BotFather al crear nuestro bot nos proporciona un token [chat con BotFather](https://core.telegram.org/bots).
Comando para instalar telepot:
```
sudo pip3 install telepot
```
el programa principal de nuestro bot es botRaspberryPiIot.py

dentro de este se configuraron las siguientes funciones:

/ObtenerFoto: toma una foto instantanea de la camara y nos la envia
/ObtenerVideo: Graba un corto de video por medio de la camara y nos lo envia (el proceso puede tardar un poco)
/IniciarStreaming: activa la descarga continua de video y nos envia el link por el cual podemos visualizarlo 
/FinalizarStreaming: desactiva la descarga continua de video.


