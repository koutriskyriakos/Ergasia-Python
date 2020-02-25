#ASKHSH 8

import random 


l1 = ['light_one', 'light_two']
l2 = ['light_one', 'light_three']
l3 = ['light_two', 'light_three']
all_lights = ['light_one', 'light_two', 'light_three']

light_one = random.randint(1, 10)                                               #dinei tuxaies times apo 1-10 sth metavliti
light_two = random.randint(1, 10)
light_three = random.randint(1, 10)
i = 1
flag = 0

if light_one == light_two and light_one != light_three and light_one > light_three:                         #dialegw tuxaia poio fanari tha ginei prasino se periptwsi isotitas se oles tis priptwseis
  random_light = random.choice(l1)
  if random_light == 'light_one':
    flag = 1
  elif random_light == 'light_two':
    flag = 2
elif light_one == light_three and light_one != light_two and light_one > light_two:
  random_light = random.choice(l2)
  if random_light == 'light_one':
    flag = 1
  elif random_light == 'light_three':
    flag = 3
elif light_three == light_two and light_three != light_one and light_three > light_one:
  random_light = random.choice(l3)
  if random_light == 'light_two':
    flag = 2
  elif random_light == 'light_three':
    flag = 3
elif light_one == light_two and light_one == light_three:
  random_light = random.choice(all_lights)
  if random_light == 'light_one':
    flag = 1
  elif random_light == 'light_two':
    flag = 2
  elif random_light == 'light_three':
    flag = 3

while i < 6:                                                                                    #ginetai epanalipsi 5 fores
  if (light_one > light_two and light_one > light_three) or flag == 1:               #elegxos gia to pio fanari exei perissotera autokinhta wste na to kanoume prasino
    print('The first light has', light_one, 'cars.')
    print('The second light has', light_two, 'cars.')
    print('The third light has', light_three, 'cars.')
    print('The first light goes green.')
    print('The second light goes red.')
    print('The third light goes red.')
    value1 = random.randint(0, 5)
    value2 = random.randint(5, 10)
    value3 = random.randint(5, 10)
    light_one = light_one - value1                                    #afairw mia tuxaia timi apo to prasino fanari gia na dw posa amaksia tha fugoun
    light_two = light_two + value2                                    #prosthetw mia tuxaia timi sta kokkina fanaria gia na dw posa amaksia tha erthoun 
    light_three = light_three + value3
    i += 1
    print('The first light is green and has', light_one, 'cars.')
    print('The second light is red and has', light_two, 'cars.')
    print('The third light is red and has', light_three, 'cars.')
    print(value1, 'cars left from the first light.')
    print(value2, 'cars came at the second light.')
    print(value3, 'cars came at the third light.')
    
  elif (light_two > light_one and light_two > light_three) or flag == 2: 
    print('The first light has', light_one, 'cars.')
    print('The second light has', light_two, 'cars.')
    print('The third light has', light_three, 'cars.')
    print('The first light goes red.')
    print('The second light goes green.')
    print('The third light goes red.')
    value1 = random.randint(0, 5)
    value2 = random.randint(5, 10)
    value3 = random.randint(5, 10)
    light_one = light_one + value2
    light_two = light_two - value1
    light_three = light_three + value3
    i += 1
    print('The first light is red and has', light_one, 'cars.')
    print('The second light is green and has', light_two, 'cars,')
    print('The third light is red and has', light_three, 'cars.')
    print(value2, 'cars came at the first light.')
    print(value1, 'cars left from the second light.')
    print(value3, 'cars came at the third light.')

  elif (light_three > light_two and light_three > light_one) or flag == 3: 
    print('The first light has', light_one, 'cars.')
    print('The second light has', light_two, 'cars.')
    print('The third light has', light_three, 'cars.')
    print('The first light goes red.')
    print('The second light goes red.')
    print('The third light goes green.')
    value1 = random.randint(0, 5)
    value2 = random.randint(5, 10)
    value3 = random.randint(5, 10)
    light_one = light_one + value3
    light_two = light_two + value2
    light_three = light_three - value1
    i += 1
    print('The first light is red and has', light_one, 'cars.')
    print('The second light is red and has', light_two, 'cars.')
    print('The third light is green and has', light_three, 'cars.')
    print(value3, 'cars came the first light.')
    print(value2, 'cars came at the second light.')
    print(value1, 'cars left from the third light.')
