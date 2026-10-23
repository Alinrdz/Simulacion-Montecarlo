import random

# Primero ponemos los datos que vamos a usar para nuestra inversion
# Empezamos con 10000 pesos y cada mes vamos a agregar 1000 pesos
# Queremos saber cuanto dinero podriamos tener despues de 30 años
# Rendimiento y volatilidad son suposiciones
# Simulaciones: cuantas veces vamos a repetir el calculo de nuestra inversion

inversion_inicial = 10000
aportacion_mensual = 1000
años = 30
rendimiento_promedio = 0.08
volatilidad = 0.15
simulaciones = 1000

# Estas variables nos van a servir para guardar los resultados
# Asi podremos saber cual fue el mejor, el peor y el promedio

suma_resultados = 0
resultado_mayor = 0
resultado_menor = 0

# Vamos a repetir el proceso 1000 veces
# Cada simulacion puede dar un resultado diferente, porque el rendimiento de la inversion no siempre es igual

for i in range(simulaciones):

    dinero = inversion_inicial

    # En cada simulacion vamos a calcular el dinero año por año
    # Esto se repite hasta completar los 30 años
    
    for año in range(años):

        # Generamos un rendimiento aleatorio para cada año
        # Usamos un promedio de 8% pero puede variar
        
        rendimiento = random.gauss(rendimiento_promedio, volatilidad)

        # Multiplicamos nuestro dinero por el rendimiento obtenido
        # De esta manera sabemos si la inversion gano o perdio dinero
        
        dinero = dinero * (1 + rendimiento)

        # Agregamos los 1000 pesos de cada mes
        # Como son 12 meses, en total agregamos 12000 pesos al año
        
        dinero = dinero + aportacion_mensual * 12

        # Si por alguna razon el dinero queda negativo
        # lo dejamos en cero para que no aparezcan cantidades negativas
        
        if dinero < 0:
            dinero = 0

    # Guardamos el dinero final de cada simulacion
    # Despues usaremos esta suma para calcular el promedio
    
    suma_resultados = suma_resultados + dinero

    # En la primera simulacion guardamos el resultado
    # como el mayor y el menor para poder compararlos despues
    
    if i == 0:
        resultado_mayor = dinero
        resultado_menor = dinero

    # Revisamos si encontramos una cantidad mayor a la anterior
    
    if dinero > resultado_mayor:
        resultado_mayor = dinero

    # Tambien revisamos si encontramos una cantidad menor
    
    if dinero < resultado_menor:
        resultado_menor = dinero

# Dividimos la suma de todos los resultados entre las 1000 simulaciones
# Asi obtenemos un promedio de cuanto dinero podriamos tener

promedio = suma_resultados / simulaciones

# Por ultimo mostramos los datos que usamos y los resultados
# Redondeamos las cantidades a 2 decimales para que sea mas facil leerlas

print("SIMULACION DE MONTECARLO")
print("-------------------------")
print("Inversion inicial: $", inversion_inicial)
print("Aportacion mensual: $", aportacion_mensual)
print("Años de inversion:", años)
print("Simulaciones realizadas:", simulaciones)

print("\nRESULTADOS")
print("Promedio final: $", round(promedio, 2))
print("Mejor resultado: $", round(resultado_mayor, 2))
print("Peor resultado: $", round(resultado_menor, 2))