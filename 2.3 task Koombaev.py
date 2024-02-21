# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


year=int(input())
if(year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('year - високосный год')
else:
    print('year- не високосный год')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
