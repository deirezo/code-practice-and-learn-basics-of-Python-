
ingresos = salario = 1700
ingresos == salario

gastos = 1200
ingresos != gastos
balance = ingresos - gastos
cuenta_corriente = plata_del_banco = 1500
comisiones = 12//4 * 100##se cobran 4 trismestres al año
capital = balance + plata_del_banco - comisiones
print ("Dinero que se dispone:" + str (capital))

deuda = 2000
intereses = 0.25
deuda_con_intereses = deuda + deuda * intereses
print ("Deuda con intereses:" + str (deuda_con_intereses))
print 

##el bonus viene a ser lo que paga el 
#servicio de prestamo, el cual es un 
#monto a pagar si es que el cliente
#paga antes de tiempo, entonces se 
#hacen diversas comparaciones

bonus = deuda_con_intereses * 0.9
print("Si decide pagar antes de tiempo el bonus es de:" + str (bonus))

## se supone que 1200 representaria lo que
# se necesita para vivir, entonces se hace 
# la comparacion, si el capital es mayor a los gastos + deudas, 
# y si la deuda es mayor a los gastos, para 
# ver si se puede vivir con ese dinero y para
# ver si se puede permitir la deuda


comparacion_and = (capital > gastos) and (deuda < capital) #caso 1 comparativa cerrada a funciones
comparacion_or = (capital > gastos) or (deuda > capital) #caso 2 comparativa abierta a funciones 
definicion_not = not (capital > gastos) #caso 3 si negaramos la comparacion de valores entre la 
                                        #capital y los gastos
print (comparacion_and)

if comparacion_and == True:
    print ("Se puede vivir con el capital disponible")
else: 
    print ("No se puede vivir con el capital disponible")

if deuda_con_intereses >= capital:
    print ("No se puede pagar la deuda con el capital disponible")
elif deuda_con_intereses < capital and deuda_con_intereses > bonus:
    print ("Se debe de pagar el bonus para pagar menor deuda")

else: print ("Se puede pagar la deuda con el capital disponible")

if capital>deuda:
    print ("Se puede pagar la deuda con el capital disponible")
elif capital==deuda_con_intereses:
    print ("La deuda con intereses inclluidos es igual al capital")
else: print ("La deuda con intereses es mayor al capital disponible")  

deudas = [deuda, deuda_con_intereses, bonus]
print("La cantidad a pagar dependiendo del tipo de deuda es:")
print(deudas [0])
print(deudas [1])
print(deudas [2])
