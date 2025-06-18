import time
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite sua cidade: ')
estado = input('Digite seu estado: ')
qntd_livros_digitais = int(input('Quantidade de livros digitais lidos no último ano: '))
qntd_livros_fisicos = int(input('Quantidade de livros físicos lidos no último ano: '))
preferência = input('Prefere "Digital" ou "Físico": ')
horas_livro_estudo = int(input('Número de horas que dedica aos livros por estudo por semana: '))
horas_livro_entretenimento = int(input('Número de horas que dedica aos livros por entretenimento por semana: '))
ano_inicial = int(input('Digite aqui com quantos anos começou a ler frequentemente :  '))

print(f'=== Boas-vindas ao menu caro {nome}! ===')
time.sleep(1)
def estimativa(): 

    estimativa_5anos_digitais = qntd_livros_digitais * 5
    estimativa_5anos_fisicos = qntd_livros_fisicos * 5
    estimativa_total = estimativa_5anos_digitais + estimativa_5anos_fisicos
    if qntd_livros_fisicos + qntd_livros_digitais >= 12:
        print(f'Parabéns! Você está lendo muitos livros, em média 1 ou mais livros por mês\nSua estimativa para os 5 anos seguintes é de {estimativa_total} livros no total')
        time.sleep(1)
    elif 6 < qntd_livros_digitais + qntd_livros_fisicos < 12:
        print(f'Você está em uma boa média de leitura, mas pode melhorar!\nSua estimativa para os 5 anos seguintes é de {estimativa_total} livros no total')
        time.sleep(1)
    elif qntd_livros_fisicos + qntd_livros_digitais < 6:
        print(f'Você está lendo pouco, sugiro começar a criar um hábito mais constante!\nSua estimativa para os 5 anos seguintes é de {estimativa_total} livros no total')
        time.sleep(1)

"""Estimativa para a quantidade de livros lidos nos próximos 5 anos de acordo com o hábito atual, além de considerar o nível de leitura
            do usuário"""

def classificacao_leitor():
        
        """Calculo de quantos anos o usuário pratica a leitura e classificando de acordo com o nível que está, utilizando o número de livros
                    lidos no último ano"""

        anos_leitura = idade - ano_inicial
        if 3 < anos_leitura < 6 and qntd_livros_digitais + qntd_livros_fisicos >= 12:
            print('Você está bem consistente e disciplinado, lendo 1+ livros por mês! Continue assim para não parar mais!\nVocê é um Leitor Intermediário')
            time.sleep(1)
        if 3 < anos_leitura < 6 and qntd_livros_digitais + qntd_livros_fisicos < 12:
            print('Você está bem consistente e disciplinado, continue assim para chegar na marca de 1 livro ou mais por mês!\nVocê é um Leitor Intermediário')
            time.sleep(1)
        elif anos_leitura <= 3 and qntd_livros_fisicos + qntd_livros_digitais >= 12:
            print('Você está em uma etapa crucial, na qual a disciplica e a consistência devem se aliar a você rapidamente, se aprimore mais ainda!\nVocê é um Leitor Iniciante')
            time.sleep(1)
        elif anos_leitura <= 3 and 6 < qntd_livros_fisicos + qntd_livros_digitais < 12:
            print('Você está indo bem, mesmo no início está se esforçando para atingir o marco de 1 livro por mês durante o ano!\nVocê é um Leitor Iniciante')
            time.sleep(1)
        elif 3 < anos_leitura < 6 and 6 < qntd_livros_fisicos + qntd_livros_digitais >= 12:
            print('Um bom início você construiu! Basta apenas manter esse hábito de leitura para ultrapassar a marca de 1+ livros por mês!\nVocê é um Leitor Intermediário')
            time.sleep(1)
        elif anos_leitura > 6 and qntd_livros_digitais + qntd_livros_fisicos >= 12:
            print('Sua disciplina e força de vontade em aprender é surpreendente! Está no caminho certo para uma vida sábia e bem desenvolvida\nVocê é um Leitor Avançado')
            time.sleep(1)


def menu(): 
    menu_l = True
    while menu_l: 

        """Menu interativo com diversas opções de funcionalidades especializadas de acordo com as informações do usuário"""

        opcoes = '1- Frequência de leitura e estimativa para os próximos 5 anos\n' \
        '2 - Cálculo de leitura por estudo no ano\n' \
        '3 - Cálculo de leitura por entretenimento no ano\n' \
        '4 - Perspectiva de continuar a leitura de acordo com a idade\n' \
        '5 - O que sua preferência pode nos dizer sobre você e quais os benefícios\n '
        print(opcoes)
        decisao = input('Digite aqui a opção desejada: ')
        time.sleep(1)
        if decisao == '1':
            estimativa()
        
        elif decisao == '2':

            """Cálculo de horas direcionadas a leitura por estudo no ano"""

            estudo_por_ano = horas_livro_estudo * 52
            print(f'Você dedica {estudo_por_ano} horas de estudo por ano!')
            time.sleep(1)
        elif decisao == '3':
            """Cálculo de horas direcionadas a leitura por entretenimento por ano!"""

            entretenimento_por_ano = horas_livro_entretenimento * 52
            print(f'Você dedica {entretenimento_por_ano} horas de leitura por entretenimento no ano inteiro')
            time.sleep(1)
        elif decisao == '4':

            """Calculo de quantos anos o usuário pratica a leitura e classificando de acordo com o nível que está, utilizando o número de livros
            lidos no último ano"""
            classificacao_leitor()
            
        elif decisao == '5':

            """Classificando o perfil do usuário de acordo com sua preferência de leitura, além de mostrar alguns benefícios e malefícios disso"""

            if preferência.capitalize() == 'Digital':
                print('Você é uma pessoa moderna, que gosta de adquirir conhecimento de forma tecnológica e automatizada!\nTem seus benefícios, como o rápido acesso à livros e a praticidade\nPorém possui alguns malefícios, como o vício em tela!\nEntão cuidado!')

            elif preferência.capitalize() == 'Físico':
                print('Você é uma pessoa tradicional, que gosta do padrão e dos livros como foram originados, adquirindo conhecimento puramente na origem\nTem seus benefícios, como uma melhor capacidade de retenção de conhecimento\nPorém possui malefícios, como o custo de compra e a fadiga ocular das pequenas letras\nEntão cuidado! ')

        else:
            print('Digite uma opção válida!')
            time.sleep(1)
menu()