####
# Supón que abres una cuenta de ahorros que tiene una tasa de interés anual del 4%. Este interés se aplica al final de cada año sobre el balance total de la cuenta. Comienzas depositando $1000.
# 
# Tu reto es calcular y mostrar lo siguiente:
# 
# ¿Cuánto dinero tendrás en la cuenta al final del primer año?
# ¿Cuánto dinero tendrás en la cuenta al final del segundo año?
# ¿Cuánto dinero tendrás en la cuenta al final del tercer año?
###

funds = 1000
interest_rate = 0.04
years =int(input("How many years do you want to use?"))

while years >= 1:
    funds += (funds * interest_rate)
    years = years - 1
print(funds)


