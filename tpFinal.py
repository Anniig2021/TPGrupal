from datetime import datetime
def cargar_datos():
  lista = []
  entrada = input("desea ingresar? ")
  while entrada != "no":
    informe = int(input("Año del informe: "))
    if informe >= 2021:
      semestre = int(input("Ingrese semestre(1 o 2): "))
      if semestre == 1 or semestre == 2:
        n_exp = int(input("Ingrese numero de expediente: "))   
        fecha = input("Ingrese fecha de denuncia: ")
        formato = "%d/%m/%Y"
        fecha_y = datetime.strptime(fecha, formato)
        fecha_z = fecha_y.date()
        datetime.strptime(fecha, formato)
        fecha_1 = "1/7/2021"
        fecha_1_y = datetime.strptime(fecha_1, formato)
        fecha_1_z = fecha_1_y.date()
        if semestre == 1 and fecha_z < fecha_1_z or semestre == 2 and fecha_z > fecha_1_z:
          genero_denunciante = input("Ingrese genero del denunciante(m:mujer,h:hombre, x:otre): ")
              
          if genero_denunciante == "m" or genero_denunciante == "h" or genero_denunciante == "x":
            claustro = input("Ingrese claustro(e: estudiante, n: no-docente, d:docente, g:graduado): ")
            if claustro == "e" or claustro == "n" or claustro == "d" or claustro == "g":
              hvs = input("hechos de violencia sexual?(si/no): ")
              has = input("hechos de acoso sexual?(si/no): ")
              hcs = input("hechos con connotacion sexista?(si/no): ")
              cav = input("comportamientos y acciones de violencia?(si/no): ")
              tipo_situacion = [hvs, has, hcs, cav]
              if hvs == "si" or has == "si" or hcs == "si" or cav == "si":
                genero_denunciado = input("Ingrese genero de la persona denunciada(m:mujer,h:hombre, x:otre: ")
                if genero_denunciado == "m" or  genero_denunciado == "h" or genero_denunciado == "x":
                  claustro_2 = input("Ingrese claustro del denunciado(e: estudiante, n: no-docente, d:docente, g:graduade): ")
                  if claustro_2 == "e" or claustro_2 == "n" or claustro_2 == "d" or claustro_2 == "g":           
                    datos = [informe, semestre,n_exp, fecha_z, genero_denunciante, claustro,tipo_situacion,genero_denunciado,claustro_2]
                    lista.append(datos)
                    entrada = input("desea ingresar otro? ")
                  else:
                    print("Ingrese otra vez")   
              else:
                print("Ingrese otra vez")
            else:
              print("Ingrese otra vez")
        else:
          print("Ingrese otra vez")
      else:
        print("Ingrese otra vez")                                 

    else:
      print("Ingrese otra vez")                                 
  return lista

def contable(lista):
  cont_hvs = 0
  cont_has = 0
  cont_hcs = 0
  cont_cav = 0
  cont_e = 0
  cont_d = 0
  cont_n = 0
  cont_g = 0
  for x in lista:
    if x[6][0] == "si":
      cont_hvs = cont_hvs +1
    if x[6][1] == "si":
      cont_has = cont_has +1
    if x[6][2] == "si":
      cont_hcs = cont_hcs +1
    if x[6][3] == "si":
      cont_cav = cont_cav +1 
    if x[5] == "e" and x[8] == "e":
      cont_e = cont_e +1
    if x[5] == "n" and x[8] == "n":
      cont_n = cont_n +1
    if x[5] == "d" and x[8] == "d":
      cont_d = cont_d +1
    if x[5] == "g" and x[8] == "g":
      cont_g = cont_g +1
    

  return "Hechos de violencia sexual: "+str(cont_hvs)+", Hechos de acoso sexual: "+str(cont_has)+", Hechos con connotacion sexista: "+str(cont_hcs)+" y Comportamientos y acciones de violencia: "+str(cont_cav) + ". Casos de denuncias del mismo claustro: estudiante/estudiante: "+ str(cont_e)+ ", no-docente/no-docente: "+ str(cont_n)+", docente/docente: "+str(cont_d)+" y graudado/graudado: "+ str(cont_g)
  
def determinar(lista):
  cont_denuncias = 0
  cont_hvs = 0
  cont_has = 0
  cont_hcs = 0
  cont_cav = 0
  cont_m = 0
  cont_h = 0
  cont_x = 0
  mayor = -1
  for x in lista:
    cont_denuncias = cont_denuncias +1
    if x[6][0] == "si":
      cont_hvs = cont_hvs +1
    if x[6][1] == "si":
      cont_has = cont_has +1
    if x[6][2] == "si":
      cont_hcs = cont_hcs +1
    if x[6][3] == "si":
      cont_cav = cont_cav +1 
    if x[4] == "m":
      cont_m = cont_m +1
    if x[4] == "h":
      cont_h = cont_h +1
    if x[4] == "x":
      cont_x = cont_x +1
    if x[2] > mayor:
      mayor = x[2]
    
    total = cont_hvs+ cont_has + cont_hcs + cont_cav
    porc_hvs = cont_hvs/total
    porc_has = cont_has/total
    porc_hcs =cont_hcs/total
    porc_cav = cont_cav/total
  return "La cantidad total de denuncias es de: "+str(cont_denuncias)+", el porcentaje de denuncias de Hechos de violencia sexual: "+str(porc_hvs*100)+"%, Hechos de acoso sexual: "+str(porc_has*100)+"%"+ ", Hechos con connotacion sexista: " +str(porc_hcs*100)+"%"+" y Comportamientos y acciones de violencia:"+str(porc_cav*100)+"%. La cantidad de denunciantes de mujeres: "+ str(cont_m)+", hombres: "+str(cont_h)+"y otres: "+str(cont_x)+". El mayor numero de expediente ingresado es: "+str(mayor)
  
prog =cargar_datos()
print(contable(prog))
print(determinar(prog))
