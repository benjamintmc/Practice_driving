# Country and age
country = input('Which country are you from? ')
age = input('How old are you? ')
age = int(age)

if country == 'Taiwan':
    if age >= 18:
        print('You can get a driver license!')
    else:
        print('You are too young for a driver license...')

elif country == 'US':
    if age >= 16:
        print('You can get a driver license!')
    else:
        print('You are too young for a driver license...')

else:
    print('Pleae enter only US or Taiwan in country')