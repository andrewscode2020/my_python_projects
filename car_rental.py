"""
PROGRAM THAT FINDS THE LEAST EXPENSIVE WAY TO TRAVEL FROM ONE PLACE TO ANOTHER,
GIVEN DIFFERENT CAR PRICES, CAPACITIES AND THE CONDITION THAT EACH CAR CAN ONLY 
BE RENTED IF ALL ITS SEATS ARE OCCUPIED

"""

''' GIVEN DATA'''
vehicles = [
    {'capacity': 1, 'cost': 15},
    {'capacity': 4, 'cost': 40},
    {'capacity': 7, 'cost': 55},
    {'capacity': 10, 'cost': 70},
    {'capacity': 15, 'cost': 100},
    {'capacity': 20, 'cost': 120},
    {'capacity': 35, 'cost': 200},
]

'''FUNCTIONS'''

def organize_data(vehicles):
    cap_cost = {}
    capacities = []
    for i in vehicles:
        cap = i['capacity']
        cos = i['cost']
        capacities.append(cap)
        cap_cost.update({cap:cos}) 
    return capacities, cap_cost

def least_expensive(num_people, vehicles):
    
    (capacities, cap_cost) = organize_data(vehicles)
    aux = num_people
    capacities.reverse()
    cars_per_cap = {}
    
    for i in capacities:
        if num_people//i > 0:
            num_of_cars = num_people//i
            num_people = num_people%i
            cars_per_cap.update({i:num_of_cars})
        else:
            cars_per_cap.update({i:0})
    
    total_cost = 0
    for i in capacities:
        total_cost += cap_cost[i]*cars_per_cap[i]
    
    for i in capacities:
        if cars_per_cap[i] != 0:
            print(f'> Rent {cars_per_cap[i]} cars with {i} seats for {cap_cost[i]} USD each')
    
    print(f'\nThe total cost would be {total_cost} USD ({round(total_cost/aux,2)} USD per person)')

def wrong_input():
    print('\nThe entered value must be:\n')
    print('> An integer')
    print('> Not negative')
    print('> Not zero')
    print('\nPlease try again')

'''MAIN PROGRAM'''

print('\n***WELCOME TO OUR APP***')

str_people = ''
num_people = 0
while str_people.isdigit() == False or num_people == 0:
    
    str_people = input('\nEnter number of people traveling to the PyCon Medellín: ')
    
    if str_people.isdigit() == False or int(str_people) == 0:
        wrong_input()
    else:
        num_people = int(str_people)
        print(f'\nThe least expensive way to send {num_people} people from Bogotá to Medellín is:\n')
        least_expensive(num_people, vehicles)
