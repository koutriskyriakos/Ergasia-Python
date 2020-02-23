#ASKHSH 8

import random 

light_one = random.randint(1, 10)
light_two = random.randint(1, 10)
light_three = random.randint(1, 10)
value1 = random.randint(0, 5)
value2 = random.randint(5, 10)
value3 = random.randint(5, 10)

if light_one > light_two and light_one > light_three: 
  print(light_one)
  print(light_two)
  print(light_three)
  light_one = light_one - value1
  light_two = light_two + value2
  light_three = light_three + value3
  print('There are', light_one, 'cars at the green light')
  print('There are', light_two, 'cars at the first red light')
  print('There are', light_three, 'cars at the second red light')
  print(value1, 'cars left from the green light')
  print(value2, 'cars came at the first red light')
  print(value3, 'cars came at the second red light')
  
elif light_two > light_one and light_two > light_three: 
  print(light_one)
  print(light_two)
  print(light_three)
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
  print(light_one)
  print(light_two)
  print(light_three)
  light_three = light_three - value1
  light_two = light_two + value2
  light_one = light_one + value3
  print('There are', light_three, 'cars at the green light')
  print('There are', light_one, 'cars at the first red light')
  print('There are', light_two, 'cars at the second red light')
  print(value1, 'cars left from the green light')
  print(value2, 'cars came at the first red light')
  print(value3, 'cars came at the second red light')
