def linha():
	print("="*70)

def conhecendo_usuario():
    print("Antes de começarmos, precisamos saber um pouco sobre você.")
    nome = input("Qual o seu nome: ")
    idade = int(input("Qual a sua idade: "))

    return nome.capitalize(), idade

def historia_parte_1(nome):
    
    print(f"""
    Em uma galáxia não tão distante assim, {nome} se vê em uma enrascada no planeta Terra. \nUm vírus ataca novamente, e dizima grande parte dos lacradores e mitadores mundiais.
    Graças aos Joãozinhos tranca rua, ele perdeu seu emprego de garçon, \ne agora precisa procurar um novo emprego rápido, antes que sua familia morra de fome.\n
    Agora, {nome} pode ser um motoboy, e ser aclamado por toda população mundial, \nou ser um caminhoneiro e ser esquecido de todo horizonte imaginativo da sociedade.
    """)
    linha()
    resposta_profissao = int(input("Você quer ser motoboy ou caminhoneiro? (digite 1 para motoboy ou 2 para caminhoneiro)\nDigite o código = "))
    linha()

    if (resposta_profissao == 1):
        historia_parte_2(nome, "motoboy")
    elif (resposta_profissao == 2):
        historia_parte_2(nome, "caminhoneiro")
    else:
        codigo_invalido()


def historia_parte_2(nome, profissao):
    
    if profissao == 'motoboy':
        print(f"""
        Graças a campanha 'fique em casa, deixe um motoboy morrer por você', {nome} conseguiu um emprego rápido para poder ajudar sua familia.\n
        Depois de um longo dia de trabalho entregando comida para funcionarios publicos trancados em casa, ficou com fome.\n
        Percebeu que a melhor lanchonete da cidade fica um pouco longe, mas que sua querida vovó morava ali perto.
        """)

        linha()
        resposta = int(input("Você quer ir pra casa da vovó ou pra lanchonete? (1) lanchonete (2) vovó)\nDigite o código = "))
        linha()

        if (resposta == 1):
            historia_lanchonete(nome)
        elif (resposta == 2):
            historia_casa_vovo(nome)
        else:
            codigo_invalido()
    else:
        print(f"""
        {nome} - {profissao}
        """)
    

def codigo_invalido():
    print("*** Código inválido ***".center(50))
    resposta = int(input("Quer começar o jogo novamente? (1) sim ou (2) não = "))
    if (resposta == 1):
        pass
    else:
        print("\n============= FIM DE JOGO =============\n")

def historia_lanchonete(nome):

    print(f"""
    {nome} foi então a melhor lanchone da cidade, a Pobr's fast food. Fez seu pedido favorito, um hamburgão topzera.\n
    Então, como tinha ficado muito tempo sentado durante o dia, teve vontade de comer em pé no balcão da lanchonete.
    Porém, se deparou com um dilema.  
    """)

    linha()
    resposta = int(input(
    	"Você quer comer sentado ou em pé no balcão da Pobr's fast food? (1) em pé (2) sentado\nDigite o código = "))
    linha()

    if (resposta == 1):
        print(f"""Ao comer em pé, {nome} se esqueceu da noticia que assistiu na rede gróbis, ao qual falava que em estabelecimentos como aquele,\n 
        ao ficar em pé pega coronga, mas se esta sentado está a salvo de tudo. Como ficou de pé, pegou Coronga e se ferrou :(
        """)
        imprime_mensagem_perdedor("Puxa, como você não tem fisico de atleta, você morreu!!!")
    elif (resposta == 2):
        print(f"""
        Comendo tranquilamento sentado o seu hamburgão, quando de repente uma ótima noticia apareceu no canal da rede gróbis, em uma TV a sua frente.\n
        Um militante falava que naquele mesmo dia, perto de onde estava {nome}, havia um posto de saúde que estava vacinando pessoas contra peste chinesa.\n
        {nome}, uma pessoa muito prudente e inteligente, perguntou se seria uma boa coisa sair daquele lugar e ir se vacinar logo, para que você a ter uma vida minimamente normal.
        """)

        linha()
        resposta = int(input(
            "Você quer ir se vacinar agora? (1) sim (2) não\nDigite o código = "))
        linha()
        if (resposta == 1):
            historia_posto_saude(nome)
        else:
            imprime_mensagem_perdedor(f"Puxa, como {nome} não se vacinou, pegou coronga na lanchonete e se ferrou :( VOCÊ PERDEU!!!")

    else:
        codigo_invalido()

    

def historia_universidade(nome):
    print(f"""
    Ao chegar na universidade, {nome} se deu conta que fica quase impossivel manter o distanciamento social naquele lugar.\n
    Porém, como sempre vai a academia 3 dias por semana, pensou que se pegar coronga, não iria sentir quase nada e poderia seguir com seus estudos.\n
    Dito e feito, ou quase isso, {nome} pegou coronga sim, mas vai estudar deitado assim como faz em casa, só que estará deitado em um lugar mais pacífico.\n
    Um cemitério :(
    """)

    linha()

    imprime_mensagem_perdedor("Puxa, como você não tem fisico de atleta, você morreu!!!")

def historia_casa_vovo(nome):
    
    print(f"""
    Ao chegar a casa dá vovó, {nome} comeu o seu prato favorito, pois como toda vovó, o obrigou a comer feito um condenado.\n
    Porém, {nome} se esqueceu que sua querida vovó faz parte do grupo de risco, graças a sua idade e suas comorbidades.\n
    Devido {nome} sair para trabalhar, de alguma forma, ele passou a peste chinesa para sua vovó, que veio a falecer.
    """)

    linha()

    imprime_mensagem_perdedor("Puxa, você ferrou com sua vovó. VOCÊ PERDEU!!!")


def historia_posto_saude(nome, idade): 
    print(f"""
    Antes de aplicarem a vacina, a enfermeira o avisou que a farmacêutica da vacina tem 'isenção de responsabilidade',\n 
    ou seja, não tem responsabilidade por eventuais efeitos colaterais da vacina. {nome} achou tudo muito estranho.""")
    imprime_mensagem_perdedor("Parabéns, você foi vacinado e venceu!!!")


def imprime_mensagem_vencedor(mensagem):
    print(f"{mensagem}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(mensagem):
    print(f"{mensagem}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


linha()
print("O JACARÉ MUTANTE COMUNISTA".center(50))
linha()

nome, idade = conhecendo_usuario()
linha()

historia_parte_1(nome)


# ser entregador do iFood ou Caminhoneiro (escolha, ser ovacionado pela imprensa como entregador, ou esquecido por ser um Caminhoneiro)
# ele cria uma conta no nubank pra sua avó. Ele envia dinheiro pra ela poder comprar no Ifood comida, e conversa com ela todo dia pelo zoom.
# ele ve a noticia que pode se vacinar, porem ele escolhe ir pra casa da vovo e pega covid e mata a veia e ele mesmo.
# ele ve a noticia que pode se vacinar, porem ele escolhe ir na lanchonete comer algo, porem fica em pé e não sentado, e pega covid e morre.

'''
print("1. CORONAVAC")
print("2. OXFORD")
print("3. PFIZER")
vacina russa Sputnik V - vira comunista
fisico de atleta

vacina = int(input("Qual vacina você tomou? Digite 1, 2 ou 3: "))

if (vacina == 1) or (vacina == 2) or (vacina == 3):
    print("Parabéns, você está protegido!")
    if vacina == 1:
        print("E você virou um jacaré!")
    elif vacina == 2:
        print("E agora você está microchipado")
    else:
        print("E agora você é mutante!")
else:
    print("Você não está protegido! #Ficaemcasa")
'''

# Um tema específico: Vacinação Covid 19

# Enredo:

# Título: O Jacaré mutante

# Locais diferentes (pelo menos 3)
# 1: Posto de saude
# 2: Universidade
# 3: Casa da vóvó
# 4: Lanchonete

# Personagens diferentes (pelo menos 3)
# 1: Usuário
# 2: Vovó
# 3: Médico
# 4: Caminhoneiros
# 5: Entregador Ifood

# Condições de vitória (pelo menos 2)
# 1: Tomar vacina
# 2: Isolamento social
# 3: Torcer para o time certo (corinthians)

# Condições de derrota (pelo menos 4)
# 1: Sair de casa sem mascara, sem distanciamento social
# 2: Fazer manifestação agloberando
# 3: Ir pra casa da vovó
# 4: Jogar futebol com os amigos (felipe neto)
# 5: Comer comida em pé pega covid, mas se sentar não pega
# 6: Pegar onibus ou metro em determinado horario não pega, mas depois das 10h pega
