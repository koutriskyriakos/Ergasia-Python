#ASKHSH 12

from datetime import datetime
import datetime

today = datetime.datetime.now()                                                 #apothikeuw tin simerimi imerominia sto today

users_date = input("Input date in this form: DD/MM/YYYY  ")                     #zitaw apo to xristi na mou dwsei tin imerominia pou thelei sti zitoumeni morfi

users_date = datetime.datetime.strptime(users_date, '%d/%m/%Y')                 #metatrepw tin imerominia pou edwse o xristis(se string) se morfi date, gia na ginetai h afairesi

till_day = users_date - today                                                   #afairw tin simerini imerominia apo ayti pou edwse o xristis, gia na vrw poses meres exoun diafora
till_day = till_day.total_seconds()                                             #metatrepw tis meres se seconds

                                                               
day = till_day // (24 * 3600)                                                   #metatrepw ta seconds se meres, wres, lepta kai seconds
till_day = till_day % (24 * 3600)
hour = till_day // 3600
till_day %= 3600
minutes = till_day // 60
till_day %= 60
seconds = till_day

month = users_date.month                                                        #apothikeuw ton mhna sto month
year = users_date.year                                                          #apothikeuw to etos sto year  

print("days:hours:minutes:seconds -> %d:%d:%d:%d" % (day, hour, minutes, seconds))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: print('The month you are looking for has 31 days')
if month == 2 and year%4 == 0: print('The month you are looking for has 29 days')                                      #auto ginetai se periptwsi disektou etous
if month == 2 : print('The month you are looking for has 28 days')
if month == 4 or month == 6 or month == 9 or month == 11: print('The month you are looking for has 30 days')
