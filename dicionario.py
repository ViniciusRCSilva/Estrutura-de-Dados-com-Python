# Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor, permitindo acesso rápido aos valores através de suas chaves. 
# Eles são extremamente versáteis e úteis em diversas situações.

# Chaves Únicas: Cada chave em um dicionário deve ser única. Se você tentar adicionar uma chave que já existe, o valor correspondente será atualizado.
# Mutabilidade: Diferente das tuplas, os dicionários são mutáveis, o que significa que você pode alterar, adicionar ou remover itens após a criação.
# Acesso Rápido: Acesso aos valores é muito rápido, pois os dicionários são implementados usando tabelas hash.

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

pessoa["telefone"] = "3333-1234" # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

dados["nome"]     # "Guilherme"
dados["idade"]    # 28
dados["telefone"] # "3333-1234"

dados["nome"] = "Maria"    
dados["idade"] = 18 
dados["telefone"] = "9988-1781"

dados # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-9871"},
    "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"] # "3333-2121"

# Funciona, porém não é a mais recomendada
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# Os dois laços retornam:
# guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-1234'}
# giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3333-2121'}  
# chappie@gmail.com {'nome': 'Chappie', 'telefone': '3333-9871'}    
# melanie@gmail.com {'nome': 'Melanie', 'telefone': '3333-7766'}

# Métodos
contatos.clear()
contatos # {}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"] # {"nome": "Gilherme", "telefone": "3333-2221"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}

# Nessa situação, a função "fromkeys" é criar chaves no dicionário e não vincular valores
dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

# Nessa situação, a função "fromkeys" é criar chaves no dicionário e padronizar os valores
dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

# O valor "chave" não existe no dicionário, portanto irá ocasionar um erro
# contatos["chave"] # KeyError

contatos.get("chave") # None
contatos.get("chave", {}) # {}
contatos.get("guilherme@gmail.com", {}) # {"nome": "Gilherme", "telefone": "3333-2221"}

contatos.items() # dict_items([("guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"})])

contatos.keys() # dict_keys(["guilherme@gmail.com"])

# A função "pop" remove e retorna o valor removido
contatos.pop("guilherme@gmail.com") # {"nome": "Gilherme", "telefone": "3333-2221"}
# Se caso o valor não existir, ele irá retornar {}
contatos.pop("guilherme@gmail.com", {}) # {}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

# O "popitem" não é passado uma chave de referência; a função remove os itens em sequência
contatos.popitem() # ("guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"})
# contatos.popitem() # KeyError

contato = {
    "nome": "Guilherme", "telefone": "3333-2221"
}

contato.setdefault("nome", "Giovanna") # Guilherme
contato # {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("idade", 28) # 28
contato # {"nome": "Guilherme", "telefone": "3333-2221", "idade": 28}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos # {"guilherme@gmail.com": {"nome": "Gui"}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-8181"}})
contatos # {"guilherme@gmail.com": {"nome": "Gui"}, "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-8181"}}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-9871"},
    "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"},
}

contatos.values() # dict_values([{"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-1234"}, "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2121"}, "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-9871"}, "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-7766"}}])

"guilherme@gmail.com" in contatos # True
"megui@gmail.com" in contatos # False
"idade" in contatos["guilherme@gmail.com"] # False
"telefone" in contatos["giovanna@gmail.com"] # True

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3333-2121'}, 'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '3333-7766'}}