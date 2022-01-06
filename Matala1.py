#QUESTION 1
sum=0
for i in range(1, 1000):
    if(i%5==0)or (i%3==0):
        sum+=i
print(sum)
#QUESTION 2
print("enter a number:")
number =int(input()) 
if (number%4==0): #EXTRE
    print("The number is multiple of 4")
elif (number%2==0): 
    print("Even")
else:
  print("Odd")
#EXTRE
variable=int(input())
dividor=int(input())
if(dividor%variable==0):
    print("the dividor divides evenly into variable")
else:
    print("dividor does not divides evenly into variable")
