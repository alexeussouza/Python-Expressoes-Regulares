# https://docs.python.org/3/library/re.html
# https://docs.python.org./3/howto/regex.html#regex-howto

import re

# Findall => encontra todas ocorrencias do padrão pesquisado no texto
# search => retorna o indice da primeira ocorrência encontrada no texto
# sub => substitui um valor dentro do texto
# compile => compila expressoes regulares

string = 'Este é um teste de expressões regulares.'

print(re.search(r'teste', string)) # usar re.funcao(r'valor procurado', variavel)
# retorna uma expressão Match informando onde a palavra inicia e onde termina dentro da string



