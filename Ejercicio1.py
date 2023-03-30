#programa de multas 
print("====================================================================")
print("===================== Bievenido a tu programa ======================")
print("====================================================================")
#Declaracion de varaibles
nombre_poli = input("Ingrese el nombre del policia: ")
multas = int(input("Ingresar cantidad de multas: "))
#evaluacion de promedio de multas 
multas_matutinas = int((multas * 0.20)/30)
multas_vespertino  = int((multas * 0.35)/30)
multas_nocturna = int((multas * 0.45)/30)
#Impresion de respuesta o resultado en pantalla
print("------------------------------------------------------------------")
print("El Policia ",nombre_poli," Registro ",multas," multas"," en el mes")
print("------------------------------------------------------------------")
print(""
      "Promedio de multas diarias matutinas es de ",multas_matutinas," multas","\n"
      "Promedio de multas diarias vispertinas es de ",multas_vespertino," multas","\n"
      "Promedio de multas diarias Nocturno es de ",multas_nocturna," multas","\n"
      "")

print("FIN DEL PROGRAMA")