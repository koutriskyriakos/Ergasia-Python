def bad_good_letters(c):
    ct_good = 0
    ct_bad = 0
    bad = ('f', 'c', 'k', 'r')
    good = ('q', 'w', 't', 'p', 's', 'd', 'g', 'h', 'j',  'l', 'z', 'x', 'v', 'b', 'n', 'm')
    for x in c.lower():
        if x in good:                             #an uparxei kapoio apo ta kala fwnhenta sth leksh, prosthese 1 sto metrhth ct_good
          ct_good += 1
        if x in bad:                              #an uparxei kapoio apo ta kaka fwnhenta sth leksh, prosthese 1 sto metrhth ct_bad
          ct_bad += 1
    if ct_good < ct_bad: 
      print('this is a bad word:', c)


f = open('/test.txt' , 'r')
data = f.read().split()
f.close()

for n in data: bad_good_letters(n)                 #kalei th synarthsh
