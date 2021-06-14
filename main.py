"""
Reto Semana 6
Nombre:
Fecha:
"""

from datetime import datetime
import pytz

def fecha_actual():
  tz = pytz.timezone('America/Bogota')
  x = datetime.now(tz) 
  x = x.strftime("%Y-%m-%d %H:%M:%S")
  return x


fecha = fecha_actual()
f = open("./SupermercadoDonPepe"+fecha+".txt", "w")
f.write("Supermercado don Pepe \n")
f.write("Nit: 124545454")

f.close()