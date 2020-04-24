#JSON
#convertir un diccionario  python a un diccionaario json
import json

producto1 = {"nombre":"silla","color":"negra","persio":100}


estructura_json = json.dump(producto1)
print(estructura_json)


