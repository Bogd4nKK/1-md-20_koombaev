# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


num=int(input('Укажите номер места в плацкартном вагоне'))
if(num>54):
    print('Такого номера не существует')
if(num>0 and num<37):
    print('Ваше место в купе')
else:
    print('Ваше место - боковое')
if (num%2==0):
    print(',верхнее')
else:
    print(',нижнее')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
