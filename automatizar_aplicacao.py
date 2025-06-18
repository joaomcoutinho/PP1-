import time
print('==== INICIANDO SISTEMA DE AUTOMATIZAÇÃO ====')
time.sleep(1)
import datetime
hoje = datetime.date.today()
dia_da_semana = hoje.weekday()
ativo = True
while ativo:

    if dia_da_semana == 5:
        print('Processo continuará para as próximas etapas!')
        time.sleep(1)
    elif dia_da_semana == 6:
        print('Processo continuará para as próximas etapas!')
        time.sleep(1)
    else:
        print('Dia inválido, deixando o programa off-line!')
        break
    conexao_wifi = True
    if conexao_wifi:
        print('Conexão estabelecida e aplicações sendo iniciadas!')
        time.sleep(1)
        break
    else:
        print('Problema de conexão detectado!')
        solucao = True
        if solucao:
            print('Problema resolvido e aplicações iniciadas!')
            time.sleep(1)
            break       
        else:
            print('Aguardando ações externas e fechando o programa!')  
            break