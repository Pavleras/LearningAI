'''
Eres el dueño de un cine y deseas automatizar la venta de boletos. Los boletos tienen un precio base de $10, pero hay algunas reglas para aplicar descuentos:

Niños menores de 12 años tienen un 50% de descuento.
Adultos mayores (65 años o más) tienen un 25% de descuento.
Los martes, todos los boletos tienen un 20% de descuento adicional.
Escribe un programa que haga lo siguiente:

Pida al usuario el día de la semana.
Pida al usuario la edad del cliente.
Calcule y muestre el precio del boleto, aplicando los descuentos correspondientes.
'''
age = 0
day = ''

def TicketPrice(age,day):
    price = 20
    if (age <= 12): 
        price = price - ((price * 50) / 100)
        print('El  precio calculado es: ', str(price))
    elif (age >= 65): 
        price = price - ((price * 25) / 100)
        print('El  precio calculado es: ', str(price))
    if (day.lower() == 'tuesday'): 
        price = price - ((price * 20) / 100)
        print('El  precio calculado es: ', str(price))
    return price

age = int(input('Introduce edad: '))
day = input('Día de la semana: ')
print ('El precio del ticket es ', str(TicketPrice(age,day)))

