"""
ATM machine that delivers the least amount of bills to fulfill 
the withdrawal request.

"""

'''Funciones'''

def input_validator():
    
    valid = False
    end_input = False
    count = 0
    while end_input == False:
        
        value = input('\nIngrese monto a retirar: ')
        
        if value.isdigit() == False or int(value)%10000 != 0 or int(value) == 0:
            print('\nEl monto solicitado es inválido')
            count += 1
            if count < 3:
                print('\nIntente nuevamente')
            else:
                print('\nUsted alcanzó el límite de intentos')
                end_input = True       
        else:
            valid = True
            end_input = True
            
    return valid, value

def bills_dispenser(amount):

    hundred_bills = amount//100000
    amount -= 100000*hundred_bills

    fifty_bills = amount//50000
    amount -= 50000*fifty_bills
                
    twenty_bills = amount//20000
    amount -= 20000*twenty_bills
            
    ten_bills = amount//10000
        
    print('\nPor favor retire su dinero:\n')
    if hundred_bills != 0:
        print('Billetes de 100 mil:', hundred_bills)
    if fifty_bills != 0:
        print('Billetes de 50 mil:', fifty_bills)
    if twenty_bills != 0:   
        print('Billetes de 20 mil:', twenty_bills)
    if ten_bills != 0:
        print('Billetes de 10 mil:', ten_bills)

''' Aplicación '''

print('\nBIENVENIDO AL CAJERO AUTOMÁTICO DEL BANCO PITÓN')
print('\nIngrese monto en múltiplos de 10.000')

valid, amount = input_validator()

if valid == True:
    bills_dispenser(int(amount))

print('\n\n***Transacción finalizada***')
print('\n¡Gracias por usar nuestros servicios!')

    