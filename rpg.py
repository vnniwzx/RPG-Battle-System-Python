import random
 
def calculo_dano(ataque, defesa, critico):
    dano = ataque - defesa
    if dano < 0:
        dano = 0
    if critico == "sim" or critico == "Sim":
        dano = dano * 2
    return dano
 
def escolher_inimigo():
    print("ㅤ")
    print("!---| Escolha um oponente |---!")
    print("1 - Destruidor")
    print("2 - P. Diddy")
    print("3 - Bárbaro")
    print("4 - Lázaro Assassino")
    print("5 - Dragão")
    print("ㅤ")
    oponente = int(input("Digite o número de seu oponente: "))
 
    if oponente == 1:
        nome = "Destruidor"
        vida = random.randint(60, 90)
        ataque = random.randint(20, 30)
        defesa = random.randint(10, 20)
    elif oponente == 2:
        nome = "P. Diddy"
        vida = random.randint(55, 85)
        ataque = random.randint(30, 45)
        defesa = random.randint(5, 15)
    elif oponente == 3:
        nome = "Bárbaro"
        vida = random.randint(50, 90)
        ataque = random.randint(35, 50)
        defesa = random.randint(5, 10)
    elif oponente == 4:
        nome = "Lázaro Assassino"
        vida = random.randint(35, 60)
        ataque = random.randint(25, 30)
        defesa = random.randint(5, 10)
    elif oponente == 5:
        nome = "Dragão"
        vida = random.randint(80, 100)
        ataque = random.randint(40, 50)
        defesa = random.randint(20, 35)
    else:
        print("Escolha um oponente existente!")
        nome = ""
        vida = 0
        ataque = 0
        defesa = 0
    return nome, vida, ataque, defesa
 
def informacoes(nome, classe, poder, rank, inimigos):
    print("!---| Informações do Jogador |---!")
    print("Nome:", nome)
    print("Classe:", classe)
    print("Poder:", poder)
    print("Rank:", rank)
    print("Inimigos derrotados:", inimigos)
 
def batalha(nome, classe, poder, vida_jogador, rank, defesa_jogador):
    inimigos_derrotados = 0
    continuar = "sim"
 
    while continuar == "sim" or continuar == "Sim":
        nome_inimigo, vida_inimigo, ataque_inimigo, defesa_inimigo = escolher_inimigo()
        if nome_inimigo != "":
            print("ㅤ")
            print("Você irá lutar contra:", nome_inimigo)
            print("Vida do oponente:", vida_inimigo)
            critico_usado = 0
 
            while vida_inimigo > 0 and vida_jogador > 0:
                print("Sua vez!")
               
                critico = "nao"
                if critico_usado == 0:
                    print("ㅤ")
                    critico = input("Ataque crítico? (sim/não): ")
                    if critico == "sim" or critico == "Sim":
                        critico_usado = 1
                dano = calculo_dano(poder, defesa_inimigo, critico)
                vida_inimigo = vida_inimigo - dano
                print("ㅤ")
                print("Dano causado:", dano)
                print("Vida do inimigo:", vida_inimigo)
                if vida_inimigo <= 0:
                    break
                print("Vez do inimigo!")
                dano_inimigo = calculo_dano(ataque_inimigo, defesa_jogador, "nao")
                vida_jogador = vida_jogador - dano_inimigo
                print("Dano recebido:", dano_inimigo)
                print("Sua vida:", vida_jogador)
 
            if vida_jogador <= 0:
                print("ㅤ")
                print("Você morreu!")
                continuar = "nao"
            else:
                print("Inimigo derrotado!")
                inimigos_derrotados = inimigos_derrotados + 1
                continuar = input("Deseja continuar? (sim/não): ")
        else:
            continuar = "sim"
    informacoes(nome, classe, poder, rank, inimigos_derrotados)
 
def rpggame():
    print("!---| RPG |---!")
    nome = input("Informe seu nickname: ")
    print("ㅤ")
    print("!---| Escolha uma classe |---!")
    print("- Guerreiro")
    print("- Mago")
    print("- Arqueiro")
    classe = input("Informe sua classe: ")
   
    if (classe != "Guerreiro" and classe != "Mago" and classe != "Arqueiro" and
        classe != "guerreiro" and classe != "mago" and classe != "arqueiro"):
        print("Classe inválida!")
        return
 
    print("ㅤ")
    print("!---| Escolha sua força (1 a 20) |---!")
    forca = int(input("Escolha seu nível de força: "))
    if forca > 20 or forca <= 0:
        print("Valor inválido!")
        return
 
    print("ㅤ")
    print("!---| Escolha sua magia (1 a 20) |---!")
    magia = int(input("Escolha seu nível de magia: "))
    if magia > 20 or magia <= 0:
        print("Valor inválido!")
        return
 
    print("ㅤ")
    print("!---| Escolha sua agilidade (1 a 20) |---!")
    agilidade = int(input("Escolha seu nível de agilidade: "))
    if agilidade > 20 or agilidade <= 0:
        print("Valor inválido!")
        return
 
    dobroforca = forca * 2
    poder = dobroforca + magia + agilidade
    defesa_jogador = agilidade
 
    print("ㅤ")
    print("!---| Informações do Jogador |---!")
    print("Nome:", nome)
    print("Classe:", classe)
    print("Força:", dobroforca)
    print("Magia:", magia)
    print("Agilidade:", agilidade)
    print("Poder:", poder)
 
    if poder <= 20:
        vida = 50
    elif poder <= 40:
        vida = 100
    elif poder <= 60:
        vida = poder * 2.5
    else:
        vida = poder * 2.5
    print("Vida:", vida)
 
    if poder <= 20:
        rank = "Bronze"
    elif poder <= 40:
        rank = "Prata"
    elif poder <= 60:
        rank = "Ouro"
    else:
        rank = "Lendário"
    print("Seu rank:", rank)
    batalha(nome, classe, poder, vida, rank, defesa_jogador)
 
rpggame()
