def linha():
	print("="*70)

def conhecendo_usuario():
    print("Antes de começarmos, precisamos saber um pouco sobre você.")
    nome = input("Qual o seu nome: ")

    return nome.capitalize()

def veiculo(profissao):
    if (profissao == "motoboy"):
        return "moto"
    else:
        return "caminhão"

def historia(nome):
    
    print(f"""
    Em uma galáxia não tão distante assim, {nome} se vê em uma enrascada no planeta Terra. \nUm vírus ataca novamente, e dizima grande parte dos lacradores e mitadores mundiais.
    Graças aos Joãozinhos tranca rua, ele perdeu seu emprego de garçon, \ne agora precisa procurar um novo emprego rápido, antes que sua familia morra de fome.\n
    Agora, {nome} pode ser um motoboy, e ser aclamado por toda população mundial, \nou ser um caminhoneiro e ser esquecido de todo horizonte imaginativo da sociedade.
    """)
    linha()
    resposta_profissao = int(input("Você quer ser motoboy ou caminhoneiro? (1) motoboy (2) caminhoneiro\nDigite o código = "))
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
        Depois de um longo dia de trabalho entregando comida para funcionários públicos trancados em seus flats, ficou com fome.\n
        Percebeu que a melhor lanchonete da cidade fica um pouco longe, mas que sua querida vovó morava ali perto.
        """)

        linha()
        resposta = int(input("Você quer ir pra casa da vovó ou pra lanchonete? (1) lanchonete (2) vovó)\nDigite o código = "))
        linha()

        if (resposta == 1):
            historia_lanchonete(nome, profissao)
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

def historia_lanchonete(nome, profissao):

    print(f"""
    {nome} foi então a melhor lanchone da cidade, a Pobr's fast food. Fez seu pedido favorito, um 'hamburgão topzera'.\n
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
        {nome}, uma pessoa muito prudente e inteligente, perguntou se seria uma boa coisa sair daquele lugar e ir se vacinar logo, para que voltasse a ter uma vida minimamente normal.
        Porém, ao mesmo tempo lembrou que seu semestre na universidade ia começar hoje, mais precisamente daqui a 1 hora teria sua primeira aula.
        """)

        linha()
        resposta = int(input(
            "Você quer ir se vacinar agora ou ir pra universidade? (1) vacinar (2) universidade\nDigite o código = "))
        linha()
        if (resposta == 1):
            historia_posto_saude(nome, profissao)
        elif (resposta == 2):
            historia_universidade(nome)
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


def tomar_vacina(nome, profissao):

    print(f"""
    {nome}, com toda sua sabedoria de um bom {profissao}, aceita ser vacinado, com esperança que aquele ato fosse fazer que sua vida voltasse ao normal.\n
    - "Qual vacina deseja tomar {nome}?", disse a enfermeira.
    """)

    linha()
    codigo_vacina = int(input("Qual vacina você quer?\n(1) CORONAVAC\n(2) OXFORD\n(3) PFIZER\n(4) Sputnik V\nDigite o código = "))
    linha()

    print(f"""
    A enfermeira pegou a seringa, mas não tinha nada dentro. Ela pegou a famosa 'vacina de vento'.\n
    Além disso, ela nem apertou o êmbolo da seringa na hora de aplicar a vacina.\n
    """)

    if (codigo_vacina == 1):
        print(f"""
        {nome}, prontamente avisou a enfermeira que aquela era a 'vacina de vento', e não o que tinha pedido.\n
        A enfermeira, constrangida com o ocorrido, pediu mil desculpas e foi correndo pegar a CORONAVAC.\n
        Quando foi aplicada a vacina chinesa, ao qual era a mesma coisa que jogar 'cara ou coroa' (50% de se dar bem ou de se ferrar), \n
        de repente {nome} se sentiu estranho, como se algo estivesse acontecendo com seu corpo.\n
        {nome} virou um jacaré comunista diante dos olhos da enfermeira. Mas, porém, contudo, todavia, entretanto, no entanto, não obstante,\n
        {nome} estava naquele momento imunizado contra covid-19, e era tudo o que importava.
        """)

        imprime_mensagem_vencedor(f"Parabéns, você foi vacinado e venceu!!! Agora {nome} é um jacaré comunista :)")
    elif (codigo_vacina == 2):
        print(f"""
        {nome}, prontamente avisou a enfermeira que aquela era a 'vacina de vento', e não o que tinha pedido.\n
        A enfermeira, constrangida com o ocorrido, pediu mil desculpas e foi correndo pegar a vacina OXFORD.\n
        Quando foi aplicada a vacina, ao qual já vem com um microchipe de rastreamento dentro,\n de repente {nome} se sentiu estranho, como se algo estivesse acontecendo com seu corpo.\n
        {nome} virou um jacaré comunista seguidor de Putin diante dos olhos da enfermeira. Mas, porém, contudo, todavia, entretanto, no entanto, não obstante,\n
        {nome} estava naquele momento imunizado contra covid-19, e era tudo o que importava.
        """)

        imprime_mensagem_vencedor(f"Parabéns, você foi vacinado e venceu!!! Agora {nome} é um jacaré comunista microchipado, e será rastreado pelo nova ordem mundial pelo resto da vida :)")
    elif (codigo_vacina == 3):
        print(f"""
        {nome}, prontamente avisou a enfermeira que aquela era a 'vacina de vento', e não o que tinha pedido.\n
        A enfermeira, constrangida com o ocorrido, pediu mil desculpas e foi correndo pegar a vacina PFIZER.\n
        Quando foi aplicada a vacina, ao qual muitos médicos diziam que utilizava uma técnologia nova que podem alterar o DNA e RNA,\n 
        de repente {nome} se sentiu estranho, como se algo estivesse acontecendo com seu corpo.\n
        {nome} virou um jacaré mutante socialista de Iphone diante dos olhos da enfermeira. Mas, porém, contudo, todavia, entretanto, no entanto, não obstante,\n
        {nome} estava naquele momento imunizado contra covid-19, e era tudo o que importava.
        """)

        imprime_mensagem_vencedor(f"Parabéns, você foi vacinado e venceu!!! Agora {nome} é um jacaré mutante socialista, e será estudado pelo Instituto Butantan :)")
    elif (codigo_vacina == 4):
        print(f"""
        {nome}, prontamente avisou a enfermeira que aquela era a 'vacina de vento', e não o que tinha pedido.\n
        A enfermeira, constrangida com o ocorrido, pediu mil desculpas e foi correndo pegar a vacina Sputnik V.\n
        Quando foi aplicada a vacina, ao qual muitos médicos diziam que por ser uma ditadura que gosta de manipular dados para favorecer sua ideologia,\n 
        de repente {nome} se sentiu estranho, como se algo estivesse acontecendo com seu corpo.\n
        {nome} virou um jacaré comunista, espião de Putin e adorador de xi jinping diante dos olhos da enfermeira. Mas, porém, contudo, todavia, entretanto, no entanto, não obstante,\n
        {nome} estava naquele momento imunizado contra covid-19, e era tudo o que importava.
        """)

        imprime_mensagem_vencedor(f"Parabéns, você foi vacinado e venceu!!! Agora {nome} é um jacaré comunista espião de Putin em solo tupiniquim :)")
    else:
        imprime_mensagem_perdedor("Puxa, {nome} recebeu a 'vacina de vento', saiu todo feliz, porém pegou coronga e se ferrou :( VOCÊ PERDEU!!!")



def historia_posto_saude(nome, profissao):

    veiculo_usuario = veiculo(profissao)

    print(f"""
    {nome}, com toda sua prudencia e sofisticação, usando 2 mascaras e respeitando o isolamento social, chegou de {veiculo_usuario} ao posto de saúde para se vacinar.\n
    Antes de aplicarem a vacina, a enfermeira o avisou que a farmacêutica da vacina tem 'isenção de responsabilidade',\n 
    ou seja, não tem responsabilidade por eventuais efeitos colaterais da vacina. {nome} achou tudo muito estranho.\n
    - "Isso é estrano, não? seria como se eu vende-se uma TV pra você, e quando você liga-se em sua casa, eu fala-se 'problema é seu!'...", disse {nome}.
    - "Pera aí, você é um negacionista terra planista minion? Vou ligar pra policia das idéias é já!...", disse a enfermeira.
    - "Não, não, calma...não sou isso não, apenas estava comentando o que um colega meu me disse outro dia.", disse {nome} nervoso com a situação.
    - "A tá. Entendi. Mas e aí, vai tomar a vacina ou não?"
    """)

    linha()
    resposta = int(input("Você quer ser vacinado? (1) sim (2) não\nDigite o código = "))
    linha()
    if (resposta == 1):
        tomar_vacina(nome, profissao)
    else:
        print(f"""
        Puxa, como {nome} não se vacinou, pegou coronga na lanchonete e se ferrou :(\n
        Porém, devido ao tratamento precoce, felizmente {nome} conseguiu se livrar do coronga.\n
        Entretanto, infelizmente {nome} morre de cancer pouco tempo depois.\n
        Devido a pandemia, seu tratamento de quimioterapia foi cancelado pois só existia uma doença no mundo em 2020.\n
        """)
        imprime_mensagem_perdedor(f"Ou seja, {nome} se ferrou :( VOCÊ PERDEU!!!")


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

nome = conhecendo_usuario()
linha()

historia(nome)


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

# Condições de derrota (pelo menos 4)
# 1: Sair de casa sem mascara, sem distanciamento social
# 2: Fazer manifestação agloberando
# 3: Ir pra casa da vovó
# 4: Jogar futebol com os amigos (felipe neto)
# 5: Comer comida em pé pega covid, mas se sentar não pega
# 6: Pegar onibus ou metro em determinado horario não pega, mas depois das 10h pega
