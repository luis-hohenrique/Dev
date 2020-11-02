data_nascimento=int(input("Qual ano você nasceu? "))
idade_em_anos= 2020 - data_nascimento
idade_em_dias= idade_em_anos * 365 
idade_em_meses= idade_em_dias / 48
print(f'Sua idade é {idade_em_anos} anos, {round(idade_em_meses)} meses e {idade_em_dias} dias.')