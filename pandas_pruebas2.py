filtro = {
 'codigo_localidad':['cod_localidad','Cod_Loc'], 

 'provincia_id':['IdProvincia','id_provincia'],

 'departamento_id':['id_departamento','IdDepartamento'],

 'categoria':['Categoría','categoria'],

 'provincia':['provincia','Provincia'],

 'localidad':['localidad','Localidad'],

 'nombre':['nombre','Nombre'],

 'direccion':['Domicilio','direccion'],

 'codigo_postal':['CP','cp'],

 'telefono':['telefono','Teléfono'],

 'correo':['Mail'],

 'pagina_web':['Web','web']
}

for x in filtro:
    if len(filtro[x]) < 2:
        print("si")
        print(x)
    else:
        print("no hay")    
       

#print(filtro['direccion'][0])  
#print(list(filtro.values()))

filtro_totales = [
   valores for valores in filtro.items()
   #for datos in valores
   #if filtro.keys() == 'CATEGORIA'
   #or filtro.keys()=='PROVINCIA'
   #or filtro.keys() == 'FUENTE'
   ]

print(filtro_totales)

