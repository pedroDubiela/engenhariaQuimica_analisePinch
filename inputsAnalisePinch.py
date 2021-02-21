import pandas as pd

class Correntes_cp():
    #Atributos:
    def __init__(self,T_in, T_out,cp):
        self.T_in = T_in # K ou °C
        self.T_out = T_out # K ou °C
        self.cp = cp #MW/°C
        self.dH =  self.cp*(abs(self.T_out-self.T_in)) # MW

class Correntes_dH():
    #Atributos:
    def __init__(self,T_in, T_out, dH):
        self.T_in = T_in # K ou °C
        self.T_out = T_out # K ou °C
        self.dH = dH
        self.cp =self.dH/abs(self.T_out-self.T_in)
# %%--------------------------------------------------------------------------------------------
def menu_selecao():
    print('##################-Menu-##################')
    opt = 0
    while (opt != 1 and opt != 2):
        print('Selecione a opção desejada:')
        print('1 - Entrar com CPs (MW/°C)')
        print('2 - Entrar com Qs (MW)')
        opt = int(input(':'))
    return opt

def info_correntes(opt):
    num_correntes = int(input('Insira o número de correntes de processo: '))
    if opt == 1:
        return gera_correntes_cp(num_correntes)
    else:
        return gera_correntes_dH(num_correntes)
          
def gera_correntes_cp(num_correntes):
    matriz_de_correntes = []
    for i in range(1,num_correntes+1):
        print('\n------------------------------------------')
        print('Para corrente',i)
        Tin = float(input('Insira a temperatura de entrada (°C): '))
        Tout = float(input('Insira a temperatura de saída (°C): ')) 
        cp = float(input('Insira CP = m*cp (MW/°C): '))
        corrente_cp = Correntes_cp(Tin,Tout,cp)
        matriz_de_correntes.append(corrente_cp)
    return matriz_de_correntes
    
def gera_correntes_dH(num_correntes):
    matriz_de_correntes = []
    for i in range(1,num_correntes+1):
        print('\n------------------------------------------')
        print('Para corrente',i)
        Tin = float(input('Insira a temperatura de entrada (°C): '))
        Tout = float(input('Insira a temperatura de saída (°C): ')) 
        dH= float(input('Insira a Entalpia (MW): '))
        corrente_dH = Correntes_dH(Tin,Tout,dH)
        matriz_de_correntes.append(corrente_dH)
    return matriz_de_correntes
        
def transfere_DT(matriz_de_correntes):
    Tin = []
    Tout = []
    cp = []
    DH = []
    tipo = []
    Tin_mod = []
    Tout_mod = []
    for i in range(len(matriz_de_correntes)):
        Tin.append(matriz_de_correntes[i].T_in)
        Tout.append(matriz_de_correntes[i].T_out)
        cp.append(matriz_de_correntes[i].cp)
        DH.append(matriz_de_correntes[i].dH)
        tipo.append('')
        Tin_mod.append('')
        Tout_mod.append('')
        
    return pd.DataFrame({'T_in':Tin, 'T_out':Tout, 'CP':cp,'DH':DH, 'Tipo':tipo , 'T_in_mod':Tin_mod, 'T_out_mod':Tout_mod})

def insere_deltaT(dt):
    deltaT = float(input('Insira o valor de delta T min (°C): '))
    dt.Tipo[dt.T_out > dt.T_in] = 'Fria'
    dt.Tipo[dt.T_out < dt.T_in] = 'Quente'
    dt.T_in_mod[dt.Tipo == 'Fria'] = dt.T_in + deltaT/2
    dt.T_out_mod[dt.Tipo == 'Fria'] = dt.T_out + deltaT/2
    dt.T_in_mod[dt.Tipo == 'Quente'] = dt.T_in - deltaT/2
    dt.T_out_mod[dt.Tipo == 'Quente'] = dt.T_out - deltaT/2
    return deltaT
    
def cria_cascata (dt):
    cascata_T_mod = []
    cascata_T_mod.extend(dt.T_in_mod )
    cascata_T_mod.extend(dt.T_out_mod)
    cascata_T_mod.sort(reverse=True)
    sem_rep = []
    for i in range(len(cascata_T_mod)):
        if cascata_T_mod[i] not in sem_rep:
            sem_rep.append(cascata_T_mod[i])
    return sem_rep
def balanco_energia(cascata,dt):
    cascata1 = cascata[0:-1]
    cascata2 = cascata[1:]
    dic = {'intervalo_M':cascata1, 'intervalo_m':cascata2 }
    dt_BE = pd.DataFrame(dic)
    lin_deltaT = []
    lin_f = []
    lin_q = []
    lin_dif_cp = []
    lin_BE = []
    
    for lin_dt_BE in range(len(cascata1)):
        soma_fria = 0
        soma_quente = 0
        for lin_dt in range(len(dt.T_in)):
            if dt.loc[lin_dt, 'Tipo'] == 'Fria':
                if dt.loc[lin_dt,'T_in_mod'] <= dt_BE.loc[lin_dt_BE,'intervalo_m'] and dt.loc[lin_dt,'T_out_mod'] >= dt_BE.loc[lin_dt_BE,'intervalo_M']:
                    soma_fria += dt.loc[lin_dt,'CP']
            if dt.loc[lin_dt, 'Tipo'] == 'Quente':
                if dt.loc[lin_dt,'T_in_mod'] >=dt_BE.loc[lin_dt_BE,'intervalo_M'] and dt.loc[lin_dt,'T_out_mod'] <= dt_BE.loc[lin_dt_BE,'intervalo_m']:
                    soma_quente += dt.loc[lin_dt,'CP']
        lin_deltaT.append(dt_BE.loc[lin_dt_BE,'intervalo_M'] - dt_BE.loc[lin_dt_BE,'intervalo_m'])
        lin_f.append(soma_fria)
        lin_q.append(soma_quente)
        lin_dif_cp.append(soma_fria-soma_quente)
        lin_BE.append(lin_deltaT[lin_dt_BE] * lin_dif_cp[lin_dt_BE])
      
    dt_aux1 = pd.DataFrame({'deltaT':lin_deltaT,'cp_f':lin_f,'cp_q':lin_q,'dif_CP':lin_dif_cp,'DH':lin_BE })
    dt_BE = dt_BE.join(dt_aux1)
    return dt_BE

def cascatas_finais(cascata, dt_BE, delta_t_min):
    lista_DH_original = [] 
    lista_fake = []
    lista_factivel = []
    #Criando a cascata original "0" + DH:
    for i in range(len(cascata)):
        if i == 0:
            lista_DH_original.append(i)
            lista_fake.append(i)
        else:
            lista_DH_original.append(dt_BE.loc[i-1,'DH'])
            lista_fake.append(lista_fake[i-1]-lista_DH_original[i])
    #Criando a cascata factivel:
    menor = abs(min(lista_fake))
    for i in range(len(cascata)):
        if i == 0:
            lista_factivel.append(menor)
        else:
            lista_factivel.append(lista_factivel[i-1]-lista_DH_original[i])
    
    dic ={'Intervalos':cascata,'DH intervalos':lista_DH_original, 'Fake':lista_fake,'Factivel':lista_factivel} 
    dt_cascata = pd.DataFrame(dic)
    demanda_Q = lista_factivel[0] 
    demanda_F = lista_factivel[-1] 
    temp_Pinch = dt_cascata.Intervalos.loc[dt_cascata.Factivel <= 0 ]
    temp_Pinch = list(temp_Pinch)
    if temp_Pinch[0] == 0 :
        resultado = [demanda_Q , demanda_F,['Sem ponto de Estrangulamento']]
    else:
        temp_Pinch = float(temp_Pinch[0])
        t_p_q = temp_Pinch + delta_t_min/2
        t_p_f = temp_Pinch - delta_t_min/2
        resultado = [demanda_Q , demanda_F,temp_Pinch, t_p_q, t_p_f]
    dic_1 = {'resultado':resultado}
    dt_results = pd.DataFrame(dic_1)
    return dt_cascata, dt_results

def saida_dados(dt,dt_BE,dt_results):
    print('=============================================================')
    print('Dados Inseridos:\n',dt)
    print('Resultado:\n',dt_results)
   
def imp_excel(dt,dt_BE,dt_results):
    dt.to_excel('entrada.xlsx')
    dt_BE.to_excel('balancoBE.xlsx')
    dt_results.to_excel('resultado.xlsx')
    
