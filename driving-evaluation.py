country = input('please give your nation: ')
age = input('please give your age: ')
age = int(age)
if country == 'China':
    if age >= 18:
        print('you can have a driving license test')
    else:
        print('you can not have a driving license test')
elif country == 'America':
    if age >= 16:
        print('you can have a driving license test')
    else:
        print:('you can not have a driving license test')
else:
    print('I Am Sorry')
