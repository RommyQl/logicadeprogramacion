
nombre=input("ingrese su nombre")
programa= input("ingrese nombre del programa de estudios")
promedio=float(input("ingrese su promedio del (0-20) : "))

if promedio >= 17:
    print("beca de exelencia ")
    print("su matricula es de: S/0.00 ")
    
elif promedio>=13 and promedio<=16.9:
    print("admitido regular")
    print("matricula a pagar: S/150.00" )
    print (f"nombre{nombre}")  
else:
    print("lista de espera")
    print (f"nombre{nombre}")  

 
