# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

# | (Ou)
print(re.findall(r'João|Maria', texto)) # seleciona João ou Maria na string Texto, Expressão case sensitive

# . (qualquer coisa) (com exceção da quebra de linha)
print(re.findall(r'p.o', texto)) # seleciona palavras iniciadas com p e terminadas com o 

# []  (conjunto de caracteres)
print(re.findall(r'[Jj]oão', texto)) # seleciona as palavras João e joão 

# []  (conjunto de caracteres)
print(re.findall(r'[a-zA-Z]aria', texto)) # seleciona intevalo de a ate z minusculo e A ate Z maiusculo 

# []  (conjunto de caracteres) e flag=re.I (I = Ignorecase)
print(re.findall(r'maria', texto, flags=re.IGNORECASE)) # seleciona intevalo de a ate z minusculo e A ate Z maiusculo

