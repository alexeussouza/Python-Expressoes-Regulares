# Meta caracteres: ^  $  ()
# *  0 ou n - existe 0 ou n vezes
# +  1 ou n - existe 1 ou n vezes
# ?  0 ou 1 - existe 0 ou 1 vezez
# {n}  - uma quantidade em especifido
# {5, 10,} permite entre 5 e 10 o
# {10,} permite 10 ou mais caracteres
# {, 10} - até 10 caracteres
# {10} apenas 10, valores a mais ou menos serão descartados
# {min, max} - um valor minimo e um maximo
# ()+  [a-\-zA-Z0-9]+  - literal é aplicado a todo conjunto entre parenteses ou colchetes

import re

texto = '''
João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo 5aria, a boa mineira que é, nunca esquece seu famoso
1aria de pão de queijo. 7aria.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeeeeeeeeem, veeeeeeeeemm, veeeeeeeeeeeeeemmm"!
'''

# []  (conjunto de caracteres) e flag=re.I (I = Ignorecase)
print(re.findall(r'jo+ão', texto, flags=re.IGNORECASE)) # seleciona intevalo de a ate z minusculo e A ate Z maiusculo
# procura a palavra joão no texto, o primeiro caracter o possui literal um ou muitos (+)

# []  (conjunto de caracteres) e flag=re.I (I = Ignorecase)
print(re.findall(r'jo+ão+', texto, flags=re.IGNORECASE)) # seleciona intevalo de a ate z minusculo e A ate Z maiusculo
# procura a palavra joão no texto, o 1º e o 2º caracter 'o' possuem literal um ou muitos (+)

# []  (conjunto de caracteres) e flag=re.I (I = Ignorecase)
print(re.findall(r've{,10}m{,5}', texto, flags=re.IGNORECASE)) # seleciona  a palavra 'vem' utilizando o conjunto <=é 10 para o literal 
# procura a palavra joão no texto, o primeiro caracter o possui literal um ou muitos (+)

# []  (conjunto de caracteres) e flag=re.I (I = Ignorecase)
print(re.findall(r've{10,}m{,5}', texto, flags=re.IGNORECASE)) # seleciona  a palavra 'vem' utilizando o conjunto >= 10 para o literal 
# procura a palavra joão no texto, o primeiro caracter o possui literal um ou muitos (+)

# []  (conjunto de caracteres) e flag=re.I (I = Ignorecase)
print(re.findall(r've{10}m{1,5}', texto, flags=re.IGNORECASE)) # seleciona  a palavra 'vem' utilizando o conjunto >= 10 para o literal 
# procura a palavra joão no texto, o primeiro caracter o possui literal um ou muitos (+)

print(re.sub(r'jo+ão+', 'Felipe', texto, flags=re.IGNORECASE)) # substitui a ocorencia joao por felipe

texto2 = 'joão ama ser amado'

print(re.findall(r'ama[do]{0,2}', texto2, re.IGNORECASE)) # busca a palavra ama que pode ter 'do'  0 ou 2 vezes

print(re.findall(r'ama[do]*', texto2, re.IGNORECASE)) # busca a palavra ama que pode ter 'do'  0 ou n vezes

print(re.findall(r'ama[do]*[-lo]*', texto2, re.IGNORECASE)) # busca a palavra ama que pode ter 'do'  0 ou n vezes e '-lo' 0 ou n vezes

