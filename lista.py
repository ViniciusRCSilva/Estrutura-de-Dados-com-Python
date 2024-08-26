# Lista
frutas = ["laranja", "maca", "uva"]

frutas[0] # laranja
frutas[2] # uva
frutas[-1] # uva
frutas[-2] # maca

letras = list("python")
# ['p', 'y', 't', 'h', 'o', 'n']

numeros = list(range(5))
# [1, 2, 3, 4, 5]

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# Matriz
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# Métodos da lista
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ['t', 'h', 'o', 'n']
lista[:2] # ['p', 'y']
lista[1:3] # ['y', 't']
lista[0:3:2] # ['p', 't']
lista[::] # ['p', 'y', 't', 'h', 'o', 'n']
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

l1 = [1, "Python", [40, 30, 20]]

print(f"Lista 1: {l1}") # [1, 'Python', [40, 30, 20]]

# Garante a cópia exata da lista, porém o ID será diferente de l1, podendo fazer operações individuais dentro da lista de l2
l2 = l1.copy()

l3 = l1

# Se l3 alterar um valor, l1 irá receber esse valor
l3[0] = 3

l2[0] = 2

print("Depois da alteração de l3")
print(f"Lista 1: {l1}") # [3, 'Python', [40, 30, 20]]
print(f"Lista 2: {l2}") # [2, 'Python', [40, 30, 20]]
print(f"Lista 3: {l3}") # [3, 'Python', [40, 30, 20]]

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

linguagens = ["python", "js", "c"]

print(linguagens)

# Insere tudo que passar entre parênteses no final da lista, ignorando duplicatas
linguagens.extend(["java", "csharp", "c"])

print(linguagens)

# Mostra o índice do elemento
linguagens.index("java") # 3
linguagens.index("python") # 0

# Retira o último elemento da lista
linguagens.pop() # c

linguagens.remove("java") # ["python", "js", "c", "csharp"]

linguagens = ["python", "js", "c", "csharp"]

# Ordena em ordem alfabética
linguagens.sort() # ['c', 'csharp', 'js', 'python']

linguagens = ["python", "js", "c", "csharp"]

# Ordena em ordem alfabética reversa
linguagens.sort(reverse=True) # ['python', 'js', 'csharp', 'c']

linguagens = ["python", "js", "c", "csharp"]

# Ordena do menor para o maior
linguagens.sort(key=lambda x:len(x)) # ['c', 'js', 'python', 'csharp']

linguagens = ["python", "js", "c", "csharp"]

# Ordena do maior para o menor
linguagens.sort(key=lambda x:len(x), reverse=True) # ['python', 'csharp', 'js', 'c']

len(linguagens) # 4

linguagens = ["python", "js", "c", "csharp"]

# Função "sorted" não altera a variável da lista
sorted(linguagens, key=lambda x:len(x)) # ['c', 'js', 'python', 'csharp']

sorted(linguagens, key=lambda x:len(x), reverse=True) # ['python', 'csharp', 'js', 'c']