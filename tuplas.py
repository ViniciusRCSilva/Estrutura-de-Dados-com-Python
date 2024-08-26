# Vantagens de usar Tupla:

# Imutabilidade: Uma vez criada, uma tupla não pode ser alterada. Isso pode ser útil para garantir que os dados permaneçam constantes ao longo do tempo.
# Desempenho: Tuplas são geralmente mais rápidas que listas para acessar elementos, pois são imutáveis e têm menos sobrecarga.
# Uso de memória: Tuplas ocupam menos espaço em memória comparadas às listas.
# Chaves de dicionário: Tuplas podem ser usadas como chaves em dicionários, enquanto listas não podem, devido à sua imutabilidade.

frutas = ("laranja", "maca", "uva")

frutas[0] # laranja
frutas[2] # uva
frutas[-2] # maca
frutas[-1] # uva

letras = tuple("python") # ('p', 'y', 't', 'h', 'o', 'n')

numeros = tuple([1, 2, 3, 4]) # (1, 2, 3, 4)

numeros = tuple(range(1, 5)) # (1, 2, 3, 4)

pais = ("Brasil")

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

lista = ("p", "y", "t", "h", "o", "n")

lista[2:] # ['t', 'h', 'o', 'n']
lista[:2] # ['p', 'y']
lista[1:3] # ['y', 't']
lista[0:3:2] # ['p', 't']
lista[::] # ['p', 'y', 't', 'h', 'o', 'n']
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']

carros = ("gol", "celta", "palio")

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

cores = ("vermelho", "azul", "verde", "azul")

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1

linguagens = ("python", "js", "c", "java", "csharp")

linguagens.index("java") # 3
linguagens.index("python") # 0

len(linguagens) # 5

# Exemplo de uso da Tupla:

# Definindo uma tupla para armazenar informações do produto
produto1 = (101, "Camiseta", 29.99)
produto2 = (102, "Calça Jeans", 79.99)
produto3 = (103, "Tênis", 149.99)

# Lista de produtos em estoque
estoque = [produto1, produto2, produto3]

# Função para exibir informações do produto
def exibir_informacoes_produto(produto):
    codigo, nome, preco = produto
    print(f"Código: {codigo}, Nome: {nome}, Preço: R${preco:.2f}")

# Exibindo informações de todos os produtos em estoque
for produto in estoque:
    exibir_informacoes_produto(produto)

# Função para calcular o valor total do estoque
def calcular_valor_total_estoque(estoque):
    valor_total = sum(produto[2] for produto in estoque)
    return valor_total

# Calculando e exibindo o valor total do estoque
valor_total = calcular_valor_total_estoque(estoque)
print(f"Valor total do estoque: R${valor_total:.2f}")