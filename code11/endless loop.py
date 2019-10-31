#PythonProgramForEndlessLooping Example
n1=int(input("Enter the number of stocks purchased: "))
p1=float(input("Money paid per stock(in $)"))
a1=n1*p1
c1=0.02*a1
print("Have U sold any stocks?")
print("1.YES")
print("2.NO")
ch=int(input("Tell me:"))
if ch==1:
    n2=int(input("Enter the number of stocks sold: "))
    p2=float(input("Money got per stock: "))
    a2=n2*p2
    c2=0.02*a2
else:
    print ("No. of stocks purchased by you are ", n1)
    print ("Money you paid per stock: $",p1)
    print ("Money You paid for all stocks purchased: $",a1)
    print ("Money paid to the agent for purchase: $",c1)
    
if ch==1:    
    print ("No. of stocks you sold were ",n2)
    print ("Money you got from stocks sold:",a2)
    print ("Commission to the agent for stocks sold:",c2)
    
    
