#ASKHSH 1

lista = []
max_words_list = []
i = 1


def afairei_fwnienta(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")    #an uparxei kapoio fwnhen to afairei

    return newstr

f = open('/test.txt' , 'r')
data = f.read().split()
f.close()

for n in data: lista.append(n)                #create list 'lista'

while i < 6 :
  max_word = max(lista, key = len)            #find the biggest word in the list 'lista'
  max_words_list.append(max_word)             #vazw ti megaluterh leksi sth lista 'max_words_list'
  lista.remove(max_word)
  i += 1


for n in max_words_list:  
  k = afairei_fwnienta(n)                      #kalei th sunarthsh
  print(k[::-1])                               #emfanizw tis lekseis tis listas anapoda

