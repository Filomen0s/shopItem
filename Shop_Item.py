import csv
import os
import time
import main

arquivo_csv_usuarios = 'cadastrosUsuarios.csv'
arquivo_csv_senhas = 'cadastrosSenhas.csv'

def guardar(nomeUsuario, senhaUsuario):
    
    if(not nomeUsuario or not senhaUsuario):
        print('\nInsira um valor válido no cadastro!')
        cadastrar()
    
    if(os.path.getsize(arquivo_csv_usuarios) == 0): 
        with open('cadastrosUsuarios.csv', 'a') as file:
            file.write(f'{nomeUsuario}')

        with open('cadastrosSenhas.csv', 'a') as file:
            file.write(f'{senhaUsuario}')
    else:
        with open('cadastrosUsuarios.csv', 'a') as file:
            file.write(f',{nomeUsuario}')

        with open('cadastrosSenhas.csv', 'a') as file:
            file.write(f',{senhaUsuario}')
            
    print('\nCadastro concluido, faça o login!')
    time.sleep(0.8)
    
    login()

def cadastrar():
    with open('cadastrosUsuarios.csv', 'r') as file:
        leitorUsuarios_csv = csv.reader(file)

        for linhaUsuarios in leitorUsuarios_csv:
            pass
        
    cadastroUsuario = input('\nCadastre o seu nome de usuário: ')
    
    while(' ' in cadastroUsuario or ',' in cadastroUsuario or '[' in cadastroUsuario or ']' in cadastroUsuario or '(' in cadastroUsuario or ')' in cadastroUsuario or '.' in cadastroUsuario or ';' in cadastroUsuario or ' ' in cadastroUsuario):
        cadastroUsuario = input('\nInsira um usuário válido (Utilize só numeros, letras e "_"): ')
    
    while(os.path.getsize(arquivo_csv_usuarios) != 0 and cadastroUsuario in linhaUsuarios):
        print('\nEste nome de usuário ja está sendo utilizado!')
        cadastroUsuario = input('\nInsira um nome de usuário válido (Utilize só numeros, letras e "_"): ')
        
    cadastroSenha = input('Cadastre sua senha: ')
    
    while(len(cadastroSenha) < 8 or cadastroSenha.lower() == cadastroSenha or not any(char.isdigit() for char in cadastroSenha)):
        cadastroSenha = input('\nSua senha deve conter no minimo 8 caracteres, letra maiuscula e um numero: ')
        
        while(' ' in cadastroSenha or ',' in cadastroSenha or '[' in cadastroSenha or ']' in cadastroSenha or '(' in cadastroSenha or ')' in cadastroSenha or '.' in cadastroSenha or ';' in cadastroSenha or ' ' in cadastroSenha): # 
            cadastroSenha = input('\nInsira uma senha válida (sem [], {}, (), ., ",", ou espaços): ')

    time.sleep(0.8)
    
    guardar(cadastroUsuario, cadastroSenha)

def login():    

    with open('cadastrosUsuarios.csv', 'r') as file:
        leitorUsuarios_csv = csv.reader(file)

        for linhaUsuarios in leitorUsuarios_csv:
            pass

    with open('cadastrosSenhas.csv', 'r') as file:
        leitorSenhas_csv = csv.reader(file)

        for linhaSenhas in leitorSenhas_csv:
            pass

    tentativaSenha = 0
    
    while(True):
        loginUsuario = input('\nInsira seu nome de usuário: ')
        loginSenha = input('Insira sua senha: ')
               
        if(loginUsuario in linhaUsuarios and loginSenha in linhaSenhas and linhaUsuarios.index(loginUsuario) == linhaSenhas.index(loginSenha)):
            print('\nAcesso autorizado!')
            time.sleep(0.8)
            addProduto = input('\nDeseja adicionar um item à lista? (s/n): ')
            while(addProduto != 's' and addProduto!= 'n'):
                addProduto = input('\nInsira um valor válido! (s/n): ')
    
            if(addProduto == 's'):
                inserirProduto()
                break
            else:
                print('Concluido!')
                break
            
        else:
            print('\nUsuário ou senha incorretos, insira novamente!')
            tentativaSenha += 1
            
            if(tentativaSenha == 3):
                redefinirSenha = input('\nRedefinir a sua senha? (s/n): ')
                
                while(redefinirSenha != 's' and redefinirSenha != 'n'):
                    redefinirSenha = input('\nInsira um valor válido! (s/n): ')
                    
                if(redefinirSenha == 's'):
                    nomeUsuario = input('\nInsira seu nome de usuário: ')
                    
                    while(nomeUsuario not in linhaUsuarios):
                        nomeUsuario = input('\nNome de usuário não encontrado, insira um nome válido: ')
                    
                    novaSenha = input('Insira a sua nova senha: ')
                    
                    while(len(novaSenha) < 8 or novaSenha.lower() == novaSenha or not any(char.isdigit() for char in novaSenha)):
                        novaSenha = input('\nSua senha deve conter no minimo 8 caracteres, letra maiuscula e um numero: ')
        
                        while(' ' in novaSenha or ',' in novaSenha or '[' in novaSenha or ']' in novaSenha or '(' in novaSenha or ')' in novaSenha or '.' in novaSenha or ';' in novaSenha or ' ' in novaSenha): # 
                            novaSenha = input('\nInsira uma senha válida (sem [], {}, (), ., ",", ou espaços): ')
                    
                    with open('cadastrosSenhas.csv', 'r') as arquivo, \
                        open('cadastrosSenhas.csv', 'w') as file:
                            
                        leitorSenhas_csv = csv.reader(arquivo)
                        inserirSenhas_csv = csv.writer(file)
                        
                        for linhaSenhas in leitorSenhas_csv:
                            if linhaSenhas.index(nomeUsuario) == loginUsuario.index(nomeUsuario):
                                linhaSenhas[linhaUsuarios.index(nomeUsuario)] = novaSenha
                                
                                inserirSenhas_csv.writerow(linhaSenhas)
                    
                    tentativaSenha = 0

                    print('\nSenha subistituida, conclua o login!')
                    time.sleep(0.8)
                else:
                    tentativaSenha = 0
                    
def possuiCadastro():
    possuiCadastro = input('\nPossui cadastro? (s/n): ')

    while(possuiCadastro != 's' and possuiCadastro != 'n'):
        possuiCadastro = input('\nInsira um valor válido! (s/n): ')
    try:
        
        if(possuiCadastro == 'n'):
            cadastrar()
        elif(os.path.getsize(arquivo_csv_usuarios) == 0):
            print('Nenhum usuário cadastrado!')
            cadastrar()
        else:
            login()

    except FileNotFoundError:
        print('\nNenhum arquivo encontrado...\n')
        time.sleep(0.8)
        
        with open('cadastrosUsuarios.csv', 'a') as file:
            file.write('')

        with open('cadastrosSenhas.csv', 'a') as file:
            file.write('')
            
        print('Criando arquivos...')
        time.sleep(1.2)
        
        cadastrar()

def inserirProduto():
    contador = int(input('Insira a quantidade de produtos que você quer adicionar na lista: '))
    
    item = main.shopItem()
    lista = main.shopList()
    
    for i in range(contador):

        print(f'\n{i + 1}º item:')
        item.name = input('Insira o nome do item: ')
        item.qnt = int(input('Insira a quantidade do item: '))
        item.value = float(input('Insira o valor do produto: '))
    
        lista.shopList.append(item)
        print('Item adicionado!')
        
    num = 0
    for item in lista.shopList:
        num += 1
        print(f'\n{num}º item: \nNome: {item.name}\nquantidade: {item.qnt}\nValor: R${item.value}')
    
        
def inicio():
    possuiCadastro()

inicio()