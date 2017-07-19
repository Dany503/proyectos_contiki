from decimal import getcontext, Decimal
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

getcontext().prec = 3 #definimos la precision de los decimales

f5 = open("res_mensaje5.txt",'r')
f10 = open("res_mensaje10.txt",'r')
f15 = open("res_mensaje15.txt",'r')
f20 = open("res_mensaje20.txt",'r')

f5_hp = open("res_mensaje5_hp.txt",'r')
f10_hp = open("res_mensaje10_hp.txt",'r')
f15_hp = open("res_mensaje15_hp.txt",'r')
f20_hp = open("res_mensaje20_hp.txt",'r')

recibidores = [0,0,0,0]
recibidores_hp = [0,0,0,0]

retransmisiones = [0,0,0,0]
retransmisiones_hp = [0,0,0,0]

reachability = [0,0,0,0]
reachability_hp = [0,0,0,0]

n = [5,10,15,20]

print
print "##########"
print "##########"
print "Flooding"
print "##########"
print "##########"
print

for linea in f5:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores[0] = recibidores[0] + 1
	if campos[4] == 'sent':
		retransmisiones[0] = retransmisiones[0] + 1

print "Numero de nodos que han recibido el mensaje de 5 Bytes:", recibidores[0]+1 #contando con el emisor
reachability[0] = Decimal(recibidores[0]+1)/Decimal(150)

for linea in f10:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores[1] = recibidores[1] + 1
	if campos[4] == 'sent':
		retransmisiones[1] = retransmisiones[1] + 1

print "Numero de nodos que han recibido el mensaje de 10 Bytes:", recibidores[1]+1 #contando con el emisor
reachability[1] = Decimal(recibidores[1]+1)/Decimal(150)

for linea in f15:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores[2] = recibidores[2] + 1
	if campos[4] == 'sent':
		retransmisiones[2] = retransmisiones[2] + 1

print "Numero de nodos que han recibido el mensaje de 15 Bytes:", recibidores[2]+1 #contando con el emisor
reachability[2] = Decimal(recibidores[2]+1)/Decimal(150)

for linea in f20:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores[3] = recibidores[3] + 1
	if campos[4] == 'sent':
		retransmisiones[3] = retransmisiones[3] + 1

print "Numero de nodos que han recibido el mensaje de 20 Bytes:", recibidores[3]+1 #contando con el emisor
reachability[3] = Decimal(recibidores[3]+1)/Decimal(150)


print
print
print "Reachabilitys obtenidas: "
print

for i in range(4):
	print "Reachability para mensaje de", n[i], "Bytes:", reachability[i]


print
print
print "Retransmisiones: "
print

for i in range(4):
	print "Retransmisiones para mensaje de", n[i], "Bytes:", retransmisiones[i]



print
print "##########"
print "##########"
print "HP-Flood"
print "##########"
print "##########"
print

for linea in f5_hp:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores_hp[0] = recibidores_hp[0] + 1
	if campos[4] == 'sent':
		retransmisiones_hp[0] = retransmisiones_hp[0] + 1

print "Numero de nodos que han recibido el mensaje de 5 Bytes:", recibidores_hp[0]+1 #contando con el emisor
reachability_hp[0] = Decimal(recibidores_hp[0]+1)/Decimal(150)

for linea in f10_hp:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores_hp[1] = recibidores_hp[1] + 1
	if campos[4] == 'sent':
		retransmisiones_hp[1] = retransmisiones_hp[1] + 1

print "Numero de nodos que han recibido el mensaje de 10 Bytes:", recibidores_hp[1]+1 #contando con el emisor
reachability_hp[1] = Decimal(recibidores_hp[1]+1)/Decimal(150)

for linea in f15_hp:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores_hp[2] = recibidores_hp[2] + 1
	if campos[4] == 'sent':
		retransmisiones_hp[2] = retransmisiones_hp[2] + 1

print "Numero de nodos que han recibido el mensaje de 15 Bytes:", recibidores_hp[2]+1 #contando con el emisor
reachability_hp[2] = Decimal(recibidores_hp[2]+1)/Decimal(150)

for linea in f20_hp:
	# calcular reachability: n nodos reciben el mensaje/nodos totales
	campos = linea.split(" ") # devuelve sent, droped o received
	if campos[4] == 'received':
		recibidores_hp[3] = recibidores_hp[3] + 1
	if campos[4] == 'sent':
		retransmisiones_hp[3] = retransmisiones_hp[3] + 1

print "Numero de nodos que han recibido el mensaje de 20 Bytes:", recibidores_hp[3]+1 #contando con el emisor
reachability_hp[3] = Decimal(recibidores_hp[3]+1)/Decimal(150)

print
print
print "Reachabilitys obtenidas: "
print

for i in range(4):
	print "Reachability para mensaje de", n[i], "Bytes:", reachability_hp[i]


print
print
print "Retransmisiones: "
print

for i in range(4):
	print "Retransmisiones para mensaje de", n[i], "Bytes:", retransmisiones_hp[i]



#############
#### Representaciones graficas
#############
fig, ax = plt.subplots()
index = np.arange(4)
bar_width = 0.35
opacity = 0.4

y1 = (reachability[0], reachability[1], reachability[2], reachability[3])
y2 = (reachability_hp[0], reachability_hp[1], reachability_hp[2], reachability_hp[3])

rects1 = plt.bar(index, y1, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Flooding')
 
rects2 = plt.bar(index + bar_width, y2, bar_width,
                 alpha=opacity,
                 color='c',
                 label='HP-Flooding')
 
plt.xlabel('Tamanyo en Bytes del mensaje')
plt.ylabel('Reachability')
plt.title('Reachability vs. tamanyo del mensaje en Bytes')
plt.xticks(index + bar_width, ('55', '10', '15', '20'))
plt.legend()
 
plt.tight_layout()
#plt.show()



fig, ax = plt.subplots()
index = np.arange(4)
bar_width = 0.35
opacity = 0.4

y3 = (retransmisiones[0], retransmisiones[1], retransmisiones[2], retransmisiones[3])
y4 = (retransmisiones_hp[0], retransmisiones_hp[1], retransmisiones_hp[2], retransmisiones_hp[3])

rects1 = plt.bar(index, y3, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Flooding')
 
rects2 = plt.bar(index + bar_width, y4, bar_width,
                 alpha=opacity,
                 color='m',
                 label='HP-Flooding')

plt.xlabel('Tamanyo en Bytes del mensaje')
plt.ylabel('Numero de retransmisiones')
plt.title('Numero de retransmisiones vs. tamanyo del mensaje en Bytes')
plt.xticks(index + bar_width, ('5', '10', '15', '20'))
plt.legend()
 
plt.tight_layout()
plt.show()
