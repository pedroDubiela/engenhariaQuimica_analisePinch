import inputsAnalisePinch as iap
'''
 Software para obter as demandas maximas e minimas pelo método
 tabular aplicado na análsie Pinch.
 Também é enconrtado o ponto Pinch.
 Sempre entrar com valores de entalpia (calor) absolutos
'''

def main():
    '''Entrada de dados:'''
    #Chamada do menu de seleção: Escolhe se entra com CP ou DH
    opt = iap.menu_selecao()
    print('------------------------------------------')
    #Chamda da função que coleta o número de correntes: Insere so dados 
    matriz_de_correntes = iap.info_correntes(opt)
    print('------------------------------------------')
    
    '''Tratamento matemático:'''
    #Converte os dados em dataframe:
    dt = iap.transfere_DT(matriz_de_correntes)
    
    #Classifica como quente e frio e insere deltaT
    delta_t_min = iap.insere_deltaT(dt)
    
    #Cria a casca de T*, ordena e tira repetidos:
    cascata = iap.cria_cascata(dt) 
    
    #Cria a tabela do BE:
    dt_BE = iap.balanco_energia(cascata,dt)
    
    #Cria as cascatas finais:
    dt_cascata, dt_results = iap.cascatas_finais(cascata,dt_BE,delta_t_min)
    
    #Preparando saida dos dados:
    op = int(input('0 - Para impimir na tela\n1 - Gerar Excel: \n'))
    if op == 0:
        iap.saida_dados(dt,dt_BE,dt_results)
    else:
        iap.imp_excel(dt,dt_BE,dt_results)
      
    return dt, cascata, dt_BE, dt_cascata, dt_results


dt, cascata, dt_BE, dt_cascata, dt_results = main()



