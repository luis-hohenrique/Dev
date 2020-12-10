def exibir_menu():
    print('''Escolha uma opção:

    1.  Cadastrar Paciente
    2.  Mostrar pacientes cadastrados
    3.  Buscar paciente
    ''')

def cadastrar(pessoas):
    identificador = input('Defina um id para este paciente: ')
    nome = input('Nome: ')
    idade = int(input('Idade do paciente: '))
    peso = int(input('Qual é o peso do paciente? '))
    altura = float(input('Qual é a altura do paciente? '))
    imc = peso / altura**2
    pessoas.append((identificador, nome, idade, peso, altura,imc))
    

def listar(pessoas):
    for pessoa in pessoas:
        identificador, nome, idade, peso, altura, imc = pessoa
        print(f' id: {identificador} Nome: {nome}, idade: {idade}, peso:{peso}, altura:{altura}, Indice de massa corporal:{round(imc,2)}  ')

def buscar(pessoas):
    identificador_desejado = input('informe o id: ')
    for pessoa in pessoas:
        identificador, nome, idade, peso, altura, imc = pessoa
        if identificador == identificador_desejado:
            print(f'id: {identificador} Nome: {nome}, idade: {idade},peso:{peso}, altura:{altura}, Indice de massa corporal:{round(imc,2)}' )
            break
    else:
        print(f'Não existe paciente com id {identificador_desejado} cadastrado')

def main():
    pessoas = []

    while True:
        exibir_menu()
        opcao = int(input('opção: '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        else:
            print('Opção inválida')

main()