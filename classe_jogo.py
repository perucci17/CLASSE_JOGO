
nome_usario = input("insira seu nome: ")
idade_usuario = int(input("insira sua idade: "))
avatar_usuario = input("insira seu personagem: ")

personagens_conhecidos = ["ninja", "mago", "guerreiro", "monge"]

if avatar_usuario.lower() not in personagens_conhecidos:
    print("Personagem não reconhecido. Encerrando o programa.")
    exit()

if avatar_usuario == "ninja":
    ataque_usuario = "shuriken"
if avatar_usuario == "mago":
    ataque_usuario = "magia"
if avatar_usuario == "guerreiro":
    ataque_usuario = "espada"
if avatar_usuario == "monge":
    ataque_usuario = "golpes de artes marciais"


class Heroi:
    def __init__(self, nome, idade, tipo, ataque):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.ataque = ataque

    def atacar(self):
        print(f" O {self.tipo} atacou usando {self.ataque} ")


heroi1 = Heroi(nome=nome_usario, idade=idade_usuario, tipo= avatar_usuario, ataque=ataque_usuario)



heroi1.atacar()

