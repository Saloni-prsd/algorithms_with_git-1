def reverse_fxn(n):     #function to return reverse number
   rev_num=0
   while n!=0:
      r=n%10
      rev_num=rev_num*10+r
      n=n//10
   return rev_num

flag=1
while flag==1:
   list1=[]
   a=int(input("Enter the no. of numbers you want to enter "))
   for i in range(0,a):
      n=int(input("Enter number: "))
      num=n                                  #num stores value of n
      n_rev=reverse_fxn(n)           #n_rev is reverse of n
      sq_n_rev=n_rev**2             #sq_n_rev is square of reverse of n
      
      if num**2==reverse_fxn(sq_n_rev):          
         list1.append(num)
      
   print("Adam numbers are: ")
   for x in list1:
      print(x,end=" ")
   if len(list1)==0:
      print("None")
   flag = int(input("\nEnter 1 to continue or any other key to quit: "))
