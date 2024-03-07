def addition():
    sum =  num1 + num2
    print(sum)
    
def multiply():
    mult = num1 * num2
    print(mult)
    
def div():
    div = num1 / num2
    print(div)
    
def sub():
    sub = num1 - num2
    print(sub)
    

print("Welcome to Mukenya's calculator");

num1 = int(input("Kindly enter the first number: "));
num2 = int(input("Kindly enter the second number: "));

print("Select your desired option:")
print("1. Addition")    
print("2. Multiplication") 
print("3. Division")      
print("4. Subtrction")     

ans = int(input("Selct one: "))

if ans == 1:
    addition();
elif ans == 2: 
    multiply();
elif ans == 3:
    div();
else:
    sub();
