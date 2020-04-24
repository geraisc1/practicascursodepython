#creamos e importamos la libreria datetime

from datetime import datetime #importamos la libreria de fecha y hora

fechayhora = datetime.now()#Definimos nuestra variable fehayhora
print(fechayhora)

año = datetime.year #formato para cada tiempo
mes = datetime.month
dia = datetime.day

#HORA
hora = datetime.hour#formato para tiempos mas especificos
minutos = datetime.minute
segundos = datetime.second
microsegundos = datetime.microsecond

print("La hora del sistema es {}:{}:{}".format(hora,minutos,segundos))
