from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = [ "*","/","-","+"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

print(f"Veremos cuanto tardas en responder estas {times} operaciones")
print("Tip: Redondea para abajo los resultados de la division")

# Declaro 3 variables inicializadas en 0. 
auxResult = 0 # resultado auxiliar 
cor = 0 # catidad de correctas e incoreectas
inc = 0
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(1)
    operator = choice(operators)

    if operator == "+":
        auxResult = number_1 + number_2
    elif operator == "-":
        auxResult = number_1 - number_2
    elif operator == "*":
        auxResult = number_1 * number_2
    else:
        while number_2 == 0: # Al no poder dividirse por 0. Si number_2 = 0, se busca un nuevo valor
            number_2 = randrange(10) # y se saca un nuevo resultado. 
        auxResult = number_1//number_2

    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))

    # Determina que resultado fue correcto o no y suma acontador
    if result == auxResult:
        print(" RESULTADO CORRECTO")
        cor+=1
    else:
        print(" RESULTADO INCORRECTO")
        inc+=1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos y resultados correctos e incorrectos. 
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Total de resultados CORRECTOS {cor}.")
print(f"\n Total de resultados INCORRECTOS {inc}.")