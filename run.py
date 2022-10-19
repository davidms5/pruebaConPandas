import os
import requests
from time import strftime
import re
import pandas as pd



with open("links.txt", "r") as file:
    for link in file:
        newFile = requests.get(link)

        def descargas(variable):
            
            route = strftime(rf"{variable}s\fecha %Y-%m")
            deleteFile = os.listdir(route)
            

            if re.search(f"{variable}", link):
                if not os.path.exists(route):
                    os.makedirs(route)
                    with open(os.path.join(route, strftime(f"{variable}s-%d-%m-%Y.csv")), 'w', newline='', encoding='utf-8') as fp:
                        fp.write(newFile.text)
                        

                else:
                    for item in deleteFile:
                      if item.endswith(".csv"):
                        #try:
                           os.remove(os.path.join(route, item))
                        #except OSError:
                          # pass   

                    with open(os.path.join(route, strftime(f"{variable}s-%d-%m-%Y.csv")), 'w', newline='', encoding='utf-8') as fp:
                        fp.write(newFile.text)     
            # hacer un codigo mas para corregir el encoding, pasar de utf-8 a latin1             

        descargas("museo")

        descargas("biblioteca")

        descargas("cine")                

        

# aqui terminamos de descargar los archivos   
# ver si se puede acomodar aun mas el codigo de arriba, meter el with open dentro de la funcion descargas tal vez 
# probar a hacer una funcion anidada con el try except
#uno de los try except por poner con las excepciones posiblemente sea con la conexion con la base de datos
# ver si cambiar el if re.search(f"{variable}", link): por---> for re.search(f"{variable}", link):