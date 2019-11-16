num = int(input("Enter a number: "))  
sumNumber = 0  
chack = num
while chack > 0:  
   digit = chack % 10  
   sumNumber = sumNumber + digit ** 3  
   chack = chack/10  
  
if num == sumNumber:  
   print(num," that is your Armstrong number")  
else:  
   print(num,"it's not Armstrong number")  