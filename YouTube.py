name = input("Please enter your name : ")
def greet(name):
    print("Hello! " , name)
greet(name)

def add(a,b):
    return a*b
result = add(5,10)
print(result)
result = add(10,7)
print(result)

def greet1(name1 = "user"):
    print("Hello!", name1)
#greet()
greet1("Yatharth ")

def details(name, age):
    print(name , "is", age,"years old")
details(age = 25, name = "Yatharth")

#problem 1 :
def area_circle(radius):
    return 3.14156 *radius *radius 
print(area_circle(7))

