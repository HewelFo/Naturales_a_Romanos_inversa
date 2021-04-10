import math
   # Funcion de arabico a romano
def romano():
   # creo una un directorio donde guardo los valores de la unidad
   Unidad = {
       0 : ' ',
       1 : 'l',
       2 : 'll',
       3 : 'lll',
       4 : 'lV',
       5 : 'V',
       6 : 'Vl',
       7 : 'Vll',
       8 : 'Vlll',
       9 : 'lX'
   }
   # creo una un directorio donde guardo los valores de la decena
   Decena = {
       0 : ' ',
       10 : 'X',
       20 : 'XX',
       30 : 'XXX',
       40 : 'XL',
       50 : 'L',
       60 : 'LX',
       70 : 'LXX',
       80 : 'LXXX',
       90 : 'XC'
   }
   # creo una un directorio donde guardo los valores de la cetena
   Centena = {
       0 : ' ',
       100 : 'C',
       200 : 'CC',
       300 : 'CCC',
       400 : 'CD',
       500 : 'D',
       600 : 'DC',
       700 : 'DCC',
       800 : 'DCCC',
       900 : 'CM'
   }

   print("ingrese el numero q va transforma")
   roman_number = int(input("->"))
   while roman_number < 1 or roman_number> 1000 :
       print("has ingreso un numero fuera de rango")
       print("ingresa un numero entre 1-1000")
       roman_number = int(input("->"))
   # imprime los el numero romano
   print(Centena[((roman_number/100)%10)100], Decena[((roman_number/10)%10)10], Unidad[(roman_number%10)])



# Funcion de romano a arabico
def arabico():
   # Con upper() la letra siempre sera pasada a mayuscula
   numero_Romano = raw_input(" ").upper()
   # Resultado de la transformacion
   rst = 0

   # Usamos un diccionario
   RomN = {
      'C' : 100,
      'L' : 50,
      'X' : 10,
      'V' : 5,
      'I' : 1
   }

   if len(numero_Romano) > 0:
      # Con esto, siempre sumamos el primer numero
      Vanterior = numero_Romano[0]

   for letra in numero_Romano:
      # Si la letra se encuentra en el diccionario
      if letra in RomN:
         # Obtenemos su valor
         Vactual = RomN[letra]
      else:
         # La letra es incorrecta
         print 'Valor invalido:', letra
         return "No numero" 

      if Vanterior >= Vactual:
         rst += Vactual
      else:
         rst += Vactual - (2 * Vanterior)

      Vanterior = Vactual

   return rst

romano()
print "Ingresa el Numero Romano:", arabico()
