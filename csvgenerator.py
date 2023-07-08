import csv
import random

# Generar una lista de 15 números aleatorios
numeros = [random.randrange(1, 100) for _ in range(15)]
print(numeros)

# Convertir todos los números a cadena y unirlos con ', '
cadena_numeros = ', '.join(map(str,numeros))

# Imprimir la cadena final
print(cadena_numeros)
