
y=1
while(y==1):
   n=input("enter number of students")
   test=[]
   fin=[]
   i=0
   for i in range(0,int(n)):
       t=input("enter")
       test.append(float(t))
   add=0.0
   for i in range(0,int(n)):
       add+=float(test[i])
       avg=float(add)/int(n)
   for i in range(0,int(n)):
       y=float(test[i])-float(avg)
      fin.append(float(y))
     check=0
     j=0
  for j in range(0,int(n)):
      if(float(fin[j])>0):
         check+=float(fin[j])
  print("$"," ","\{:.2f\}".format(check));
  if(n==0):
     y=0

