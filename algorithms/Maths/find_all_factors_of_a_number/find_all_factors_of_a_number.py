print("Enter a number")
n=input()

if(n.isdigit()):
   n=int(n)
   print("The factors of given number are")
   for i in range(1,n+1):
      if n%i==0:
         print(i,end="    ")
 
else:
    print("Invalid Input ")
