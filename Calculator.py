num1= int(input("Enter the first value: "))
num2= int (input("Enter the second value: "))
opr= input ("Enter the opr(+,-,*,/)")
if opr== "+":
  print( "The addition of two numbers", num1+num2)

elif opr=="-":
  print("The substraction of two numbers is", num1-num2)

elif opr== "*":
    print ("The multiplication of two numbers is", num1*num2)
elif opr=="/":
   print ("The division of two numbers is", num1/num2)

else:
   print( "Invalid opr" )