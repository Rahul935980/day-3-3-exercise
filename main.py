# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year%4==0:
  if year%100==0:
    if year%400==0:
      print('The Year {} is a leap year'.format(year))
    else:
      print(year, 'is not a leap year')
  else:
    print(year,'is a leap year')
else:
  print(year,'is not a leap year')
  


