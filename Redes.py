# 178.49.0.0/16
#Asignadas -> 536
#Asignar -> 632

#Primos divisibles por el mismo 

import pandas as pd
import csv

def convertir_csv(df,nombre="redes.csv"):
    df.to_csv(nombre, index=True, sep="\t")

def isPrimo(numero):
    count = 0



def calcular_redes(bits):

    for i in range(bits):
        if 2**i >= sr:
            n = i
            break
    m = bits - n
    saltos = 2**m

    print("n: ", n)
    print("m: ", m)
    print("saltos:", saltos)

    redes_decimal = []
    
    for i in range(sr):
        redes_decimal.append(agregar_0(bits,decimal_a_binario(i*saltos)))
    
    return redes_decimal


def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

def binario_a_decimal(numero_binario):
	numero_decimal = 0 

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

def agregar_0(bits, binario):
    while len(binario) < bits:
        binario = "0" + binario
    return binario


ip = input("Digite la ip de la red: ")
sr = int(input("Digite el numero de sub redes: "))

octales = ip.split(".")

redes_final =[]

if int(octales[0]) <= 127:
    tipo = 'A'
    bits = 24
    redes_decimal = calcular_redes(bits)
   
    for i in redes_decimal:
        octal1 = i[0:8]
        octal2 = i[8:16]    
        octal3 = i[16:24]
        redes_final.append( octales[0]+"."+str(binario_a_decimal(octal1))+"."+str(binario_a_decimal(octal2))+"."+str(binario_a_decimal(octal3)))

    

elif int(octales[0])  <= 191:
    tipo = 'B'
    bits = 16
    redes_decimal = calcular_redes(bits)
    
    for i in redes_decimal:
        octal1 = i[:len(i)//2]
        octal2 = i[len(i)//2:]    
        redes_final.append( octales[0]+"."+octales[1]+"."+str(binario_a_decimal(octal1))+"."+str(binario_a_decimal(octal2)))


elif int(octales[0]) <= 223:
    tipo = 'C'
    bits = 8
    redes_decimal = calcular_redes(bits)
    
    for i in redes_decimal:
        redes_final.append( octales[0]+"."+octales[1]+"."+octales[2]+"."+str(binario_a_decimal(i)))


index = range(1,len(redes_final)+ 1)
df = pd.DataFrame(redes_final,index=index,columns=['SubRedes'])


if len(df) > 150:
    print(df.head(50)) 
    print(df.tail(50)) 
else:
    print(df.head(150))

convertir_csv(df)

print(f"La red es de tipo {tipo}.")
