country = input('please give your nation: ')
age = input('please give your age: ')
age = int(age)
if country == 'China':
    if age >= 18:
        print('you can have a driving license test')
    else:
        print('you are not allowed to have a driving license test')
elif country == 'America':
    if age >= 16:
        print('you can have a driving license test')
    else:
        print:('you are not allowed to have a driving license test')
else:
    print('Sorry, this version only support China as well as America')
