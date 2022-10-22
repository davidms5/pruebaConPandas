
import re
import pandas as pd
import glob
import os
from pathlib import Path


datos = ["cine", "museo", "biblioteca"]

filtro = {
 'codigo_localidad':['cod_localidad','Cod_Loc'], 

 'provincia_id':['IdProvincia','id_provincia'],

 'departamento_id':['id_departamento','IdDepartamento'],

 'CATEGORIA':['Categoría','categoria'],

 'PROVINCIA':['provincia','Provincia'],

 'LOCALIDAD':['localidad','Localidad'],

 'NOMBRE':['nombre','Nombre'],

 'DIRECCION':['Domicilio','direccion'],

 'codigo_postal':['CP','cp'],

 'TELEFONO':['telefono','Teléfono'],

 'correo':['Mail'],

 'pagina_web':['Web','web'],

 'FUENTE':['fuente','Fuente']
}


filtro_nuevo = [datos for valores in filtro.values() for datos in valores]



#--------------------------datos para filtrar----------------------------------------------------------------#

#con datos ver si usar pathlib para conseguir los nombres de las carpetas del directorio actual, o dejarlo como esta e
#implementarlo como que se podra cambiar como un todo con un input una vez juntado todo

# ver pathlib

def respuesta():
   for i in datos:
      #este codigo completo convierte directamente el csv bajado a latin 1 
      ruta = rf"{i}s\fecha 2022-09\{i}s-17-09-2022.csv"
      df = pd.read_csv(ruta, encoding='utf-8-sig')# utf 8 cuando lo recien lo baja y latin 1 cuando ya lo convirtio
      #df = pd.read_csv(ruta, encoding='utf-8-sig')
      #df.to_csv(ruta, encoding='latin1', index=False) #hacer un bucle con esto para corregir los acentos cuando recien lo descarga
      #mambos raros entre latin1, utf-8 y utf-8-sig
      yield df

data = [x for x in respuesta()]

#-----------------------------------------------------------------------------------------------------------------


def concatenacion(dataframe):

   if not len(filtro[x]) < 2:
      dataframe[filtro[x]] = dataframe[filtro[x]].fillna("").astype(str)
      unificacion = dataframe[filtro[x][0]] + dataframe[filtro[x][1]]

      dataframe.insert(0, x, unificacion)

      dataframe.drop(filtro[x], axis=1, inplace=True)


#-----------------------------------------------defs para cosas-----------------------------------------------------

full_data = pd.concat(data, axis=0).filter(filtro_nuevo)
#siento que en la parte de filtro_nuevo puedo ahorrarme codigo con filtro.values()pero desempaquetados

for x in reversed(filtro):

   if x == "FUENTE":
      full_data.drop(filtro[x], axis=1, inplace=True)

   else:
      concatenacion(full_data)
   
#aqui estaria la primera tabla

#-------------------------------tabla numero 1--------------------------------------------------------

registros_totales = pd.concat(data, axis=0).filter(filtro_nuevo)

for x in reversed(filtro):
   concatenacion(registros_totales)

provincia = registros_totales['PROVINCIA'].unique()

categorias =  registros_totales['CATEGORIA'].unique()

fuentes =   registros_totales['FUENTE'].unique()

lista3 = [*categorias, *fuentes]


fuentes_total = registros_totales.groupby(['PROVINCIA'])['FUENTE'].value_counts()

prov_category = registros_totales.groupby(['PROVINCIA'])['CATEGORIA'].value_counts()


def suma_por_provincia(data):
   

   for indice in lista3:
      for localidad in provincia:
         data.loc[indice][localidad] = prov_category.loc[localidad][indice]#aqui hay un error KeyError
         #ver si con .append en un dataframe vacio puedo llenarlo usando un for como vi en una pagina
   #la idea aqui es que con cada for le aplique el valor a cada provincia mientras itera por las categorias y luego fuentes
   # ver luego sobre como llenar casillas especificas de un dataframe con un for


   #poner el codigo con data.loc

   
#.loc["Buenos Aires"]["Bibliotecas Populares"]


tabla_final = pd.DataFrame(index=lista3, columns=provincia)  


#suma_por_provincia(tabla_final)

print(tabla_final)

#print(tabla_final.loc["Bibliotecas Populares"])

#tabla_final = pd.concat([prov_category, fuentes_total])
#print(registros_totales.head())
#  IDEAS PARA USAR:
#1 convertir provincia, fuente y categoria en cantidades y luego usar pivot_table:
#prueba 1:
"""para esta tarea, y ahorrar tiempo, hare lo siguiente:
1- convertir cada dato que pondre en la tabla en una serie. usar groupby talvez
2- una vez que luzca decente unir los tres o en un concat, o merge o un dataframe, creo que con copy=false, que no haya 
copias de index ni duplicados
3- aqui si queda bien perfecto, sino usar pivot table """
#2 usar unique y luego un for y hacerlo manualmente
#3 aplicar un combo entre pivot table y una lista unique con provincias
#prov_category.to_csv('tabla2.csv',encoding='utf-8-sig', index=False)

#print(fuentes_total)
#print(provincia)











#print(registros_totales)



#registros_totales['total_categoria'] = registros_totales['CATEGORIA']

#total_provincia = registros_totales['PROVINCIA'].unique()



#table_data = registros_totales.groupby(["PROVINCIA"])['CATEGORIA'].value_counts()#['CATEGORIA'].value_counts()


#tabla_final = registros_totales.pivot_table(index='CATEGORIA', columns='PROVINCIA',aggfunc='sum') 

#print(tabla_final)


#print(registros_totales.head())
#usar pd.agg en esta, acepta una funcion y la puedo usar para sacar el total de las columnas

#probar o pivot table o .unique en provincia para conseguir una lista unica y hacer un for loop con ella o talvez un combo
#------------------------------------tabla numero 2-----------------------------------------------------







#VER SI SE PUEDE ARREGLAR CON LA FUNCION MAP() o seguir buscando multiple files multiple folders y glob

#ver si con pandas puedo leer sql queries escritos aparte por fuera de python
