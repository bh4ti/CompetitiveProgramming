def sequence(x):
    number = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       number.append(x)    
    return len(number)

var1=input("enter a number")   
if (int(var1)>10000 or int(var1)<0):
    var1=input("enter again")
else:
    print(sequence(int(var1)))
var2=input("enter another number")
if int(var2)>10000 or int(var2)<0:
    print("invalid number.Reenter")
    var2=input("enter again")
else:
    print(sequence(int(var2)))
check=[]
for i in range(int(var1),int(var2)):
    check.append(sequence(i))
t=max(check)
print(int(var1),"",int(var2),"",int(t))
   
  
   
