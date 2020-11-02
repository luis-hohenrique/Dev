a= int(input("Informe o valor de A: "))
b= int(input("Informe o valor de B: "))
c= int(input("Informe o valor de C: "))
if a>b+c or b>a+c or c>a+b:
    print("Não forma um triangulo")
else:
    a==b or a==c or b==a or b==c or c==a or c==b
    area=a*b or a*c or b*a or b*c or c*a or c*b / 2
    print(f"Eles formam um triangulo, então a  area do triangulo é {area}")