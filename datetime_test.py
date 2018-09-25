from datetime import datetime, timedelta, date


x = datetime.now()
z = datetime(x.year, x.month, x.day)

string1 = str(z).replace('-','')
string2 = string1.replace(' ', '')
string3 = string2.replace(':', '')

print(string3)

print(z)
print(x)
print(x.year)
print(x.strftime("%A")) #WeekDay ex:Monday
print(x.strftime("%a")) #shortWeekDay ex:Mon
print(x.strftime("%B")) #Month ex:September
print(x.strftime("%b")) #shortMonth ex:Sep

print(x.strftime("%d")) #day
print(x.strftime("%j")) #day number of year (1-365)


print(x.strftime("%U")) #Week Number of Year (week starts Sunday)
print(x.strftime("%W")) #Week Number of Year (week starts Monday)



print(x.strftime("%H")) #Hour
print(x.strftime("%I")) #Hour 0-12
print(x.strftime("%M")) #Minute
print(x.strftime("%S")) #Second
print(x.strftime("%p")) #AM/PM


y = datetime(2020, 5, 24).timestamp()

print(y)

print(datetime.fromtimestamp(y))


data = 1590303600.0 - 1589698800.0
print(data)

z = datetime.now().timestamp() + data
print(datetime.fromtimestamp(z))


str(1590303600.0) 