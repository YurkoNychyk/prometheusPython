year = int(raw_input('input year:'))
if (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)):
    print  'is leap'
else:
    print 'is not leap'