year = int(raw_input('input year:'))
if not (year % 4) and ((year % 100) or not (year % 400)):
    print  'is leap'
else:
    print 'is not leap'