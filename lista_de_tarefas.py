import time
print('==== Bem-vindo ao To do List! ====')
tarefa_afazer = []
tarefa_executado = []
tarefa_pronta = []
qntd_exec = 0
def adicionar():

    """FUNÇÃO PARA ADICIONAR TAREFAS DE ACORDO COM O CRITÉRIO DE CARACTERES"""

    while True:
        tarefa = input('Digite aqui o nome da sua tarefa : ').strip().lower()
        if len(tarefa) > 80:
            print('Número de caracteres excedido! Tente novamente')
        else: 
            print('Tarefa adicionada à aba "A fazer!" ')
            tarefa_afazer.append(tarefa)
            print('Você está indo ao menu!')
            time.sleep(1)
            break



def menu():
        """MENU INTERATIVO COM 4 OPÇÕES : PARA LEVAR À TAREFA PARA AS ABAS EXECUTANDO ; PRONTA ; EXCLUIR TAREFA OU ADICIONAR UMA NOVA """

        global qntd_exec
        while True:
            opcoes = '1 - Marcar tarefa como Executando\n2 - Marcar tarefa como Pronta\n3 - Excluir tarefa\n4 - Adicionar tarefa'
            print(opcoes)   
            decisao = input('O que deseja fazer ? Digite o número correspondente : ')
            if decisao == '1': 
                def executando():

                    """FUNÇÃO PARA LEVAR À TAREFA PARA A ABA EXECUTANDO, VERIFICANDO SE A TAREFA EXISTE E ESTÁ EM UMA ABA EXISTENTE
                    E SE ATINGIU O LIMITE PRÉ-ESTABELECIDO DE NO MÁXIMO 10 TAREFAS EM EXECUÇÃO"""


                    global qntd_exec
                    while True:  
                        print(f'Tarefas disponíveis:\n{','.join(tarefa_afazer)}')  
                        tarefa_ft_exec = input('Digite o nome exato da tarefa que deseja mover para a aba "Executando": ')
                        if tarefa_ft_exec in tarefa_afazer:
                            tarefa_executado.append(tarefa_ft_exec)
                            tarefa_afazer.remove(tarefa_ft_exec)  # ERRO AQUI !!!
                        else:
                            decisao_1 = input('Digite uma tarefa existente ou digite 1 para retornar ao menu: ')
                            if decisao_1 == '1':
                                print('Indo ao menu...')
                                time.sleep(1)
                                break
                            else:
                                if tarefa_ft_exec in tarefa_afazer:
                                    tarefa_executado.append(tarefa_ft_exec)
                                    tarefa_afazer.remove(tarefa_ft_exec)
                                    print('Tarefa adicionada à aba "Executando" e indo ao menu!')
                                    time.sleep(1)
                                    break 
                                else:
                                    print('Digite uma tarefa existente! ')
                                    time.sleep(1)
                                    continue
                        qntd_exec += 1
                        if qntd_exec <= 10:
                            
                            time.sleep(1)
                            print(f'Tarefa {tarefa_ft_exec} adicionada à aba de executando com sucesso!')
                            print('Retornando ao menu...')
                            break
                        else:
                            print('Limite de 10 tarefas em execução atingido, retornando ao menu!')
                            tarefa_executado.remove(tarefa_ft_exec)
                            time.sleep(1)
                            break
                executando()
            elif decisao == '2': # Informar a lista completa e perguntar ao usuario qual quer marcar como pronta
                def pronta():

                    """FUNÇÃO PARA INSERIR TAREFAS NA ABA PRONTA, VERIFICANDO A EXISTÊNCIA DA TAREFA NAS ABAS DO SISTEMA
                    E APRESENTANDO AO USUÁRIO AS OPÇÕES DISPONÍVIEIS"""


                    while True:
                        print(f'Tarefas disponíveis:\n{','.join(tarefa_afazer + tarefa_executado)}')
                        tarefa_ft_pronta = str(input('Digite aqui o nome exato da tarefa a ser movida para a aba "Pronta" : '))
                        
                        if tarefa_ft_pronta in tarefa_afazer:
                            tarefa_pronta.append(tarefa_ft_pronta)
                            tarefa_afazer.remove(tarefa_ft_pronta)
                            print(f'Tarefa {tarefa_ft_pronta} adicionada à aba de prontas com sucesso!')
                            time.sleep(1)
                            print('Retornando ao menu...')
                            break
                        elif tarefa_ft_pronta in tarefa_executado:
                            tarefa_pronta.append(tarefa_ft_pronta)
                            tarefa_executado.remove(tarefa_ft_pronta)
                            print(f'Tarefa {tarefa_ft_pronta} adicionada à aba de prontas com sucesso!')
                            time.sleep(1)
                            print('Retornando ao menu...')
                            break
                        else:
                            print('Digite uma tarefa válida! ou digite 1 para retornar ao menu:  ')
                            print(f'Tarefas disponíveis:\n{tarefa_afazer + tarefa_executado}')
                            tarefa_ft_pronta = str(input('Digite aqui o nome exato da tarefa a ser movida para a aba "Pronta" : '))
                            if tarefa_ft_pronta == '1':
                                print('Indo ao menu...')
                                break
                            else:
                                continue
                pronta()    
            elif decisao == '3':
                def excluir(): 
                    
                    """FUNÇÃO PARA EXCLUIR UMA TAREFA EXISTENTE QUE ESTEJA EM QUALQUER UMA DAS TRÊS ABAS DO SISTEMA"""

                    while True:
                        print(f'Tarefas disponíveis:\n{','.join(tarefa_afazer + tarefa_executado + tarefa_pronta)}')
                        excluir = str(input('Digite a tarefa a ser excluída: '))
                        if excluir in tarefa_afazer:
                            tarefa_afazer.remove(excluir)
                            print(f'Tarefa {excluir} excluida com sucesso!')
                            print('Retornando ao menu...')
                            time.sleep(1)
                            break
                        elif excluir in tarefa_executado:
                            tarefa_executado.remove(excluir)
                            print(f'Tarefa {excluir} excluida com sucesso!')
                            print('Retornando ao menu...')
                            time.sleep(1)
                            break
                        elif excluir in tarefa_pronta:
                            tarefa_pronta.remove(excluir)
                            print(f'Tarefa {excluir} excluida com sucesso!')
                            print('Retornando ao menu...')
                            time.sleep(1)
                            break
                        else:
                            decisao = input('Digite uma tarefa válida ou digite 1 para retornar ao menu : ')
                            if decisao == '1':
                                print('Indo ao menu...')
                                time.sleep(1)
                            else:
                                continue
                excluir()                
            elif decisao == '4':
                adicionar()
menu()


   