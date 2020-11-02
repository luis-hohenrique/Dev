num1= int(input("Digite o primeiro valor: "))
num2= int(input("Digite o segundo valor: "))
num3= int(input("Digite o terceiro valor: "))
menor= num1

if num2 < menor:
    print(f'{num2} é menor')
if num3 < menor:
    print(f'{num3} é menor')
else:
    print(f'{menor} é menor')
