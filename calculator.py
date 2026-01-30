'calculator'
print('''-:rules:-
      *: multiplication
      /: divide
      +: addition
      -: subtraction
      !: remainder
      ^: exponent
      %: percentage
      2: square
      &: average
      3:cube
      ''')
print("choose operation")
o=(input())

if (o=="*"):
    print("multiply")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a*b)
    
elif(o=="/"):
    print("divide")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a/b)
elif(o=="+"):
    print("addition")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a+b)
elif(o=="-"):
    print("subtraction")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a-b)
elif(o=="!"):
    print("remainder")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a%b)
elif(o=="^"):
    print("exponent")
    a=int(input("enter the number"))
    b=int(input("enter the power "))
    print(a**b)
elif(o=="%"):
    print("percentage")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print((a/b)*100)
elif(o=="2"):
    print("square")
    a=int(input("enter the number"))
    print(a*a)
elif(o=="&"):
    print("average")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print((a+b)/2)
elif(o=="3"):
    print("cube")
    a=int(input("enter the number"))
    print(a*a*a)
