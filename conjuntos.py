# Vantagens em usar Conjuntos

# Unicidade dos Elementos: Conjuntos armazenam apenas elementos únicos, eliminando automaticamente duplicatas. Isso é útil quando você 
# precisa garantir que uma coleção de dados não tenha valores repetidos.

# Operações Matemáticas: Conjuntos suportam operações matemáticas como união, interseção, diferença e diferença simétrica de forma eficiente. 
# Essas operações são úteis em diversas aplicações, como análise de dados e manipulação de conjuntos.

# Verificação Rápida de Pertencimento: Verificar se um elemento está em um conjunto é muito rápido devido à implementação interna baseada em 
# tabelas hash. Isso torna os conjuntos ideais para operações que envolvem muitas verificações de pertencimento.

# Desempenho: Conjuntos são geralmente mais rápidos que listas para operações que envolvem a verificação de existência de elementos e 
# eliminação de duplicatas.

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

numeros = {1, 2, 3, 2}

# Se for preciso acessar o íncide, é preciso transformar em uma lista
numeros = list(numeros)

print(numeros[0])

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Métodos da classe set
conjunto_a = {1, 2}
conjunto_b = {3, 4}

# União do os dois conjuntos
conjunto_a.union(conjunto_b) # {1, 2, 3, 4}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Interseção do os dois conjuntos
conjunto_a.intersection(conjunto_b) # {2, 3}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Diferença entre o conjunto A e o conjunto B e vice-versa
conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

# Diferença dos conjuntos A e B
conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Conjunto A está contido no conjunto B?
conjunto_a.issubset(conjunto_b) # True

# Conjunto B está contido no conjunto A?
conjunto_b.issubset(conjunto_a) # False

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Conjunto A contêm conjunto B?
conjunto_a.issuperset(conjunto_b) # False

# Conjunto B contêm conjunto A?
conjunto_b.issuperset(conjunto_a) # True

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# A função "isdisjoint" verifica se os conjuntos não possuem elementos em comum
conjunto_a.isdisjoint(conjunto_b) # True, não possuem elementos em comum
conjunto_a.isdisjoint(conjunto_c) # False, possuem elementos em comum

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# Limpa todos os elementos do conjunto
sorteio.clear()

sorteio = {1, 23}

# Copia os elementos do conjunto
sorteio.copy()

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard(1)
numeros # {0, 2, 3, 4, 5, 6, 7, 8, 9}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# A função "remove", diferente da função "discard", o elemento é removido somente se existir no conjunto
numeros.remove(0) # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros) # 10

1 in numeros # True
10 in numeros # False

# Exemplo de uso de conjuntos:

# Listas de clientes de duas lojas diferentes
clientes_loja1 = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
clientes_loja2 = ["Carlos", "Fernanda", "Gabriel", "Ana", "Helena"]

# Convertendo listas em conjuntos
conjunto_loja1 = set(clientes_loja1)
conjunto_loja2 = set(clientes_loja2)

# Encontrando clientes comuns entre as duas lojas
clientes_comuns = conjunto_loja1.intersection(conjunto_loja2)

print("Clientes comuns:", clientes_comuns)