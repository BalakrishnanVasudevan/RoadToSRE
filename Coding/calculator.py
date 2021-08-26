#simple calculator using python

def add(a,b):
    return int(a+b)
def sub(a,b):
    return int(a-b)
def mul(a,b):
    return int(a*b)
def div(a,b):
    return (float(a)/float(b))

list=["+","-","*","/"]
while True:
 operation = raw_input("What would you like to do: Add(+)/Subtract(-)/Multiply(*)/Divide(/): \n")
 if operation in list:
  break
 else:
  print('That was not an option')

while True:
    try:
        x = int(raw_input("First number: "))
        break
    except ValueError:
        print("Make sure to enter a number.")
while True:
    try:
        y = int(raw_input("Second number: "))
        break
    except ValueError:
        print("Make sure to enter a number...")

if operation=="+":
    print(add(x,y))
elif operation=="-":
    print(sub(x,y))
elif operation=="*":
    print(mul(x,y))
else:
    print(div(x,y))
