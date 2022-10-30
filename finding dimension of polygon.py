def input_fun(s1,s2,s3):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c)**0.5)
    print("The area of triangle is: ",area)
    print("The perameter of triangle is: ",s)
    if(a+b<c):
        print("C is greater.")
    elif(b+c<a):
        print("A is greater.")
    elif(a+c<b):
        print("B is greater.")
      

a=float(input("Enter the length of Side1: "))
b=float(input("Enter the length of Side2: "))
c=float(input("Enter the length of Side3: "))
input_fun(a,b,c)

