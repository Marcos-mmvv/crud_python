
chaves = ('Nome', 'CPF', 'Telefone', 'Email', 'Profissão', 'Empresa')

cadastro = {}

def menu ():
    print(f'{'-'*30} MENU {'-'*30}\n')
    print('1 - Realizar o cadastro: ')
    print('2 - Imprimir cadastro: ')
    print('3 - Digite o nome que deseja localizar: ')
    print('4 - Atualizar cadastro: ')
    print('5 - Digite o nome que deseja deletar do cadastro:')
    print('6 - sair ')
    print()

import os

#Inicio do loop
while True:
    menu()
    
    escolha = input('Escolha a opção desejada: ')
        
    if escolha == '1':
        
        lista = [
            {
        'nome': input('Infome o seu nome: '),
        'cpf': input('Infome o CPF: '),
        'telefone': input('Infome o seu telefone: '),
        'email': input('Infome o seu e-mail: '),
        'profissao': input('Infome o seu profissão: '),
        'empresa': input('Infome a sua empresa : ')
        }
        ]
        lista.append(lista)
        #lista.sort()
        print('Cadastro Realizado com sucesso!!!')
      
    elif escolha == '2':
        for cad in lista:
            print(f'{cad}: {cad.get(cad)}')
            

    elif escolha == '3':
        cad = input('Insira o nome que deseja localizar: ')
        if cad in lista:
            print(f'O nome {cad} foi localizado na lista.')
            
    elif escolha == '4':
        novo_nome = input('Insira o novo nome: ')
        lista.append(novo_nome)
        lista.sort()
        if novo_nome in lista:
                print()
                print(f'O nome {novo_nome} foi inserido na lista com sucesso.')
                
    elif escolha == '5':
        deletar = input('Digite o nome a ser deletado: ')
        if deletar in lista:
            try:
                lista.remove(deletar)
                print(f'O nome {deletar} foi excluído com sucesso.')
                print()
                print(f'{'-'*10} LISTA ATUALIZADA {'-'*10}')

            except:
                print('Não foi possível deletar! ')
            for novo_nome in range(len(lista)):
                print(f'{novo_nome +1 }º - {lista[novo_nome]}')
                
    elif escolha =='6':
        os.system('cls')
        break
        
    else:
        escolha == ''
        print('Opção inválida ')
        continue