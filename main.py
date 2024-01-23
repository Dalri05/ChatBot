from time import sleep
from os import system

def chat():
    print('''
    [1] - O que a Techsolutions faz?
    [2] - Quantos anos a TechSolution tem no mercado?
    [3] - Qual o diferencial da TechSolution?
    [4] - Como a empresa foi fundada?
    [5] - Como faço para ingressar?
    ''')
    resposta = input("Digite:")
    if resposta == "1":
        print("A TechSolutions é especializada no desenvolvimento de softwares personalizados para atender às necessidades específicas de seus clientes. Seu portfólio abrange desde aplicativos móveis e plataformas web até soluções empresariais de última geração. A empresa é reconhecida por proporcionar inovação, eficiência e escalabilidade em cada projeto.")
        sleep(3)
        system("cls")
        chat()
    elif resposta == "2":
        print("Atualmente, a TechSolutions está celebrando seus 12 anos no mercado. Ao longo dessa jornada, a empresa construiu uma sólida reputação pela entrega de projetos bem-sucedidos e pela constante adaptação às mudanças tecnológicas.")
        sleep(3)
        system("cls")
        chat()
    elif resposta == "3":
        print("O diferencial da TechSolutions está na abordagem centrada no cliente e na busca incessante pela excelência técnica. A empresa prioriza a compreensão profunda das necessidades de seus clientes, oferecendo soluções que não apenas atendem às expectativas, mas também superam as barreiras tradicionais da inovação.")
        sleep(3)
        system("cls")
        chat()
    elif resposta == "4":
        print("A ideia da TechSolutions começou a ganhar forma quando os fundadores perceberam a lacuna entre as soluções existentes no mercado e as necessidades específicas de diversas indústrias. Com uma visão compartilhada de criar uma empresa que abraçasse a inovação e a personalização, os fundadores combinaram suas habilidades complementares em desenvolvimento de software, design e gestão de projetos para dar vida à TechSolutions.")
        sleep(3)
        system("cls")
        chat()
    elif resposta == "5":
        print("Se você está interessado em fazer parte da equipe TechSolutions, a empresa valoriza profissionais apaixonados por tecnologia, criatividade e colaboração. As oportunidades de emprego são anunciadas no site oficial da empresa e em plataformas de recrutamento. A TechSolutions busca talentos que compartilhem sua visão de superar desafios e impulsionar a inovação. Fique atento às vagas disponíveis e envie sua candidatura para se juntar a essa equipe dedicada e visionária.")
        sleep(3)
        system("cls")
        chat()
    else:
        print("Não entendi oque você quer saber, digite outra opção.")
        sleep(3)
        system("cls")
        chat()



def bot():
    print("Ola! Seja bem-vindo, espero que esteja bem! Aqui é a central de informações da TechSolutions")
    nome = input("Por gentileza, como você se chama?: ")
    sleep(3)
    system("cls")
    print("Certo,",nome,"o que gostaria de saber sobre nossa empresa?")
    chat()

bot()
