# Hacer un programa que pida 3 numeros y determine cual de el es el mayor 

num1 = int(input("Digite numero 1: "))
num2 = int(input("Digite numero 2: "))
num3 = int(input("Digite numero 3: "))

if num1>=num2 and num1>=num3:
   print(f"El mayor es: {num1}")
   
elif num2>=num1 and num2>=num3:
   print(f"El mayor es: {num2}")

elif num3>=num1 and num3>=num2:
    print(f"El mayor es: {num3}")
    
           

