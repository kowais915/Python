#This program simply calculates the year when the user will turn 100
name =input("Please enter your name: ")
age = input("Please enter your age: ")

#Here is how you calculate the year: 22 + x =100, x =100+22, 2020 + x
year = 2020 + (100 - int(age))
print(f'{name}, You will turn 100 in year {year}')
