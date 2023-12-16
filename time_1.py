import time

t = time.strftime("%H:%M")
t = input()

if "12:00" > t > "06:00":
    print('Good Morning')
elif '12:00' < t < '18:00':
    print('Good Afternoon')
elif '18:00' < t < '24:00':
    print('Good Evening')
elif t == '12:00':
    print('Its Noon')
else:
    print('Enter valid Time')
# print(t)




