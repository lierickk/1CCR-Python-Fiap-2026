# logica E (and)
# é a logica do login
# emial e a senha sejam True

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha

print(verifica_login)

if verifica_login:
    print("entrar no programa")

#Logica ou (or )
# sol do dom   jogo Br     churras do dom

Logica_ou = False or False or False
print(Logica_ou)

#not
negacao = not True
print(negacao)

if not verifica_login:
    print("acerta ai")

if not verifica_senha:
    print("senha errada")