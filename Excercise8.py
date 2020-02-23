#ASKHSH 8

import random 

light_one = random.randint(1, 10)                                   #dinei tuxaies times apo 1-10 sth metavliti
light_two = random.randint(1, 10)
light_three = random.randint(1, 10)
value1 = random.randint(0, 5)
value2 = random.randint(5, 10)
value3 = random.randint(5, 10)

if light_one > light_two and light_one > light_three:               #elegxos gia to pio fanari exei perissotera autokinhta wste na to kanoume prasino
  light_one = light_one - value1                                    #afairw mia tuxaia timi apo to prasino fanari gia na dw posa amaksia tha fugoun
  light_two = light_two + value2                                    #prosthetw mia tuxaia timi sta kokkina fanaria gia na dw posa amaksia tha erthoun 
  light_three = light_three + value3
  print('There are', light_one, 'cars at the green light')
  print('There are', light_two, 'cars at the first red light')
  print('There are', light_three, 'cars at the second red light')
  print(value1, 'cars left from the green light')
  print(value2, 'cars came at the first red light')
  print(value3, 'cars came at the second red light')
  
elif light_two > light_one and light_two > light_three: 
  light_two = light_two - value1
  light_one = light_one + value2
  light_three = light_three + value3
  print('There are', light_two, 'cars at the green light')
  print('There are', light_one, 'cars at the first red light')
  print('There are', light_three, 'cars at the second red light')
  print(value1, 'cars left from the green light')
  print(value2, 'cars came at the first red light')
  print(value3, 'cars came at the second red light')

elif light_three > light_two and light_three > light_one: 
  light_three = light_three - value1
  light_two = light_two + value2
  light_one = light_one + value3
  print('There are', light_three, 'cars at the green light')
  print('There are', light_one, 'cars at the first red light')
  print('There are', light_two, 'cars at the second red light')
  print(value1, 'cars left from the green light')
  print(value2, 'cars came at the first red light')
  print(value3, 'cars came at the second red light')
