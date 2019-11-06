from datetime import datetime
def datos():
    a=str(input("digite la placa de el auto"))
    x = datetime.now()
    h=(x.hour)*60
    m=x.minute
    total=h+m
    print("el vehiculo entró a las: ",x) 
    return[a,total]

carro1=datos()            
print("recuerde que su auto es el numero 1")
print(carro1[1])