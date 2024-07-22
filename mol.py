type = int(input("chose the one of the factors blow that you want to use:\n1-(P/F,i%,n)\n2-(F/P,i%,n)\n3-(P/A,i%,n)\n4-(A/P,i%,n)\n5-(A/F,i%,n)\n6-(F/A,i%,n)\n7-(P/G,i%,n)\n8-(A/G,i%,n)\n9-(F/G,i%,n)\nenter the numbe of factor:"))

if type == 1 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = 1 / ((i+1) ** n)
    print("(P/F,",int(i*100),"%,",n,") = ",t)

if type == 2 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = ((i+1) ** n)
    print("(F/P,",int(i*100),"%,",n,") = ",t)


if type == 3 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = ((((1+i)**n)-1)/((i)*((1+i)**n)))
    print("(P/A,",int(i*100),"%,",n,") = ",t)

if type == 4 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = (((i)*((1+i)**n)) / (((1+i)**n)-1))
    print("(A/P,",int(i*100),"%,",n,") = ",t)

if type == 5 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = ((i)/(((1+i)**n)-1))
    print("(A/F,",int(i*100),"%,",n,") = ",t)


if type == 6 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = ((((1+i)**n)-1)/i)
    print("(F/A,",int(i*100),"%,",n,") = ",t)

if type == 7 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = (1/i)*(((((1+i)**n)-1)/((i)*((1+i)**n))) - ((n)/((1+i)**n)))
    print("(P/G,",int(i*100),"%,",n,") = ",t)

if type == 8 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = (1/i)+((n)/(((1+i)**n)-1))
    print("(A/G,",int(i*100),"%,",n,") = ",t)

if type == 9 :
    i = int(input("enter the parameter (i):"))/100
    n = int(input("enter the parameter (n):"))
    t = (1/i)*(((((1+i)**n)-1)/i)-n)
    print("(F/G,",int(i*100),"%,",n,") = ",t)
