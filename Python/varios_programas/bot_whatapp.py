import pywhatkit
from datetime import datetime
import time



cont = 0
while True:
    seconds = time.time() + 60

    date = datetime.fromtimestamp(seconds)
    seconds_2  = date.second + 15
    mensaje = input('Ingrese mensaje: ')
    numero = input('Ingrese numero: ')
    pywhatkit.sendwhatmsg(numero,mensaje,date.hour,date.minute,seconds_2,True,2)

    cont += 1
    if cont == 2:
        break
