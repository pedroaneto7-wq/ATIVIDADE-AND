import os


os.system ('cls')



login =input('digiten seu login: ')
senha =input('digite sua senha: ')


login_salvo = 'jkl'
senha_salva = '123456'

login_esta_correto = login == login_salvo
senha_esta_correta = senha == senha_salva

if login_esta_correto and senha_esta_correta:
    print('bem vindo ' )
else:
    print(' login ou senha invalidos ')
