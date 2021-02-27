'''
Autor: Thiago S. Farias
Título: O Jacaré Mutante Comunista
Projeto Módulo 1 - Jogo satírico sobre a pandemia do covid-19 no Brasil.
'''

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
    else:
        historia_parte_2(nome, "caminhoneiro")
    

def historia_parte_2(nome, profissao):
    
    if profissao == 'motoboy':
        print(f"""
        Graças a campanha 'fique em casa, deixe um {profissao} morrer por você', {nome} conseguiu um emprego rápido para poder ajudar sua familia.\n
        Depois de um longo dia de trabalho entregando comida para funcionários públicos trancados em seus flats, ficou com fome.\n
        Percebeu que a melhor lanchonete da cidade fica um pouco longe, mas que sua querida vovó morava ali perto.
        """)
    else:
        print(f"""
        Graças a campanha 'fique em casa, deixe um {profissao} morrer por você', {nome} conseguiu um emprego rápido para poder ajudar sua familia.\n
        Ao dirigir o caminhão pelas cidades do seu estado, percebeu que não ficou apenas sem o prestígio da população mundial, mas como também sem almoço.\n
        Vários Joãozinhos tranca rua fecharam os restaurantes de seu percurso, o que se não fosse os moradores que distribuiam marmitex nas BRs, estaria ferrado e com anorexia.\n
        Viu pessoas sendo presas por estarem sentadas em praça publica, mesmo usando 2 mascaras, e pensou que o mundo foi pro buraco.\n        
        Ao ver toda aquela picaretagem, concordou com a famosa frase de Jordan Peterson: "Life is suffering" (A vida é sofrimento).\n 
        Pois parece que nada é tão ruim, que não possa ser piorado por um Joãozinho tranca rua de calças apertadas, pois agora terá toque de recolher e rastreamento de celular.\n
        Ao pensar em tudo isso, ficou com fome, e ao notar que estava passando por sua cidade natal, ficou feliz da vida.\n
        Percebeu que a melhor lanchonete da cidade fica um pouco longe, mas que sua querida vovó morava ali perto.\n
        """)
    
    linha()
    resposta = int(input("Você quer ir pra casa da vovó ou pra lanchonete? (1) lanchonete (2) vovó\nDigite o código = "))
    linha()

    if (resposta == 1):
        historia_lanchonete(nome, profissao)
    else:
        historia_casa_vovo(nome)
        

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
    else:
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




while (True):
    linha()
    print("O JACARÉ MUTANTE COMUNISTA".center(50))
    linha()

    nome = conhecendo_usuario()
    linha()

    historia(nome)

    resposta = int(input("\nQuer começar o jogo novamente? (1) sim ou (2) não = "))
    if (resposta == 2):
        break
    

print("\n============= FIM DE JOGO =============\n")
