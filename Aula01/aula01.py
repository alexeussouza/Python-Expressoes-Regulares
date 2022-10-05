# https://docs.python.org/3/library/re.html  => Documentação python sobre expressoes regulares
# https://docs.python.org./3/howto/regex.html#regex-howto => Documentação howto sobre expressoes regulares

import re  # usar esta importação para expressoes regulares

# Findall => encontra todas ocorrencias do padrão pesquisado no texto
# search => retorna o indice da primeira ocorrência encontrada no texto
# sub => substitui um valor dentro do texto
# compile => compila expressoes regulares

string = 'Este é um teste de expressões regulares, este teste pode ser util.'

print(re.search(r'teste', string)) # usar re.funcao(r'valor procurado', variavel)
# retorna uma expressão Match informando onde a palavra inicia e onde termina dentro da string

print(re.findall(r'teste', string)) # usar re.funcao(r'valor procurado', variavel)
# pesquisa a palavra teste na string e retorna uma lista com o resultado da expressão 

print(re.sub(r'teste', 'ABCD', string)) # usar re.funcao(r'valor procurado', variavel)
# substitui a palavra teste por ABCD na string informada na expressão 

